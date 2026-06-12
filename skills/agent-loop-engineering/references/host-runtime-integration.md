# Host Runtime Integration and Feedback Governance

Use this reference when a coding host, editor, local agent app, CLI runner, or
automation service wants to integrate Agent Loop Engineering into its runtime.

This reference is generic. It must not contain active state from one dogfooding
project.

## 1. Three CMS Layers

Keep these layers separate:

| Layer | Storage | Purpose | Typical writer |
| --- | --- | --- | --- |
| Development CMS | project-local `Docs/` | manage AI coding work orders, acceptance, review, QA, handoff | Controller / Runner |
| Product Runtime CMS | product-owned runtime store | manage one end-user task/session: target, gate, tool action, evidence | host runtime adapter |
| Skill / Reference | skill repository | reusable rules, templates, scripts, methods | skill maintainer |

Rules:

- Development CMS decides whether a development work order is complete.
- Product Runtime CMS decides whether one product task/session should continue,
  stop, or ask for permission.
- Skill/reference decides whether a rule should be reused across projects.
- Do not edit an active project's `Docs/` state when the task is only to update
  reusable skill/reference guidance.

## 2. Feedback Classification

When receiving feedback from a real project or another agent, classify before
acting.

| Feedback type | Example | Default action |
| --- | --- | --- |
| Project code issue | test failure, type error, UI defect | act only when assigned project Developer/Controller role |
| Project state issue | duplicate AC IDs, bad JSONL, stale status | act only when assigned project state maintainer role |
| Skill/process issue | unclear role boundary, missing evidence rule | update skill/reference |
| Host integration issue | adapter hook missing, runtime gate wrong | update this reference or adapter spec |
| Runner/environment issue | missing runtime, path, dependency, command | update runner/environment guidance or project PENDING |
| Human decision issue | accept risk, change target, install system dependency | stop and ask human |

Default decision:

```text
If I am updating reusable governance, I must not modify the active project's Docs state.
```

## 3. Runtime Adapter Contract

Hosts should expose a stable adapter instead of making every agent understand
store paths, task IDs, gates, and context assembly.

Recommended interface:

```ts
interface AgentLoopRuntime {
  enabled(): boolean
  ensureState(input): Promise<TaskLoopState>
  buildSystemContext(input): Promise<string | undefined>
  gateAction(input): Promise<OutputGateResult>
  recordRun(input): Promise<void>
}
```

Recommended hooks:

| Hook | When | Responsibility |
| --- | --- | --- |
| `ensureState()` | first valid user task/session turn | create or load task state |
| `buildSystemContext()` / `beforePrompt` | before model prompt assembly | inject minimal target, acceptance, pending, next action, and stop rules |
| `gateAction()` / `beforeToolExecute` | before tools, browser, cloud calls, write actions, or data transfer | allow, warn, require confirmation, redirect, or block |
| `afterToolExecute()` | after tool execution | record result summary and evidence reference |
| `recordRun()` | loop end or important transition | append machine-readable run record |

Privacy, security, and production-data checks should happen before or inside
`gateAction()`, not only after a tool has already executed.

## 4. Initialization Boundary

Only a real user-driven task turn should initialize a new runtime target.

Do not silently create a new target from:

- internal tool calls;
- background jobs;
- synthetic messages;
- test fixtures;
- summarization or compaction jobs.

Long sessions should distinguish:

- stable user goal;
- current phase target;
- current subtask or work order.

Otherwise target state becomes too broad and later gates lose direction.

## 5. Evidence Layers

Every loop report, review, or handoff should separate evidence:

| Field | Meaning |
| --- | --- |
| `code_refs` | changed code files, functions, modules |
| `validation_refs` | tests, typecheck, build, manual run, E2E, screenshots |
| `doc_refs` | updated CMS, review, acceptance, handoff, reference files |
| `known_limits` | unverified paths, environment limits, skipped checks, residual risks |

Rules:

- Implemented is not verified.
- Typecheck passing is not full Done unless acceptance only requires typecheck.
- Missing tests, missing visual checks, or missing runtime verification should
  produce `Blocked` or `Done with Risk`, not plain `Done`.
- Evidence must name command, result, time or evidence path where possible.

## 6. Runtime Bypass Switch

Every product runtime integration should have a narrow rollback switch.

Examples:

| Integration | Example flag |
| --- | --- |
| CMS runtime | `MYAPP_CMS=0` |
| UI shell | `MYAPP_UI=0` |
| Privacy layer | `MYAPP_PRIVACY=0` |
| Web bridge | `MYAPP_WEBBRIDGE=0` |

Switch rules:

- Default behavior must be clear.
- Disabled mode should approximate the host's original behavior.
- Disabled behavior should be testable, such as returning `disabled` or not
  rendering the integration.

Use product-specific names in the product, not in this reusable reference.

## 7. Context Builder Boundary

The host context builder should produce a bounded Context Packet:

- current task/work order;
- relevant target and non-goals;
- current acceptance rows;
- current stop rules;
- latest compressed state;
- latest evidence summary;
- selected retrieved facts with sources;
- one next action.

It should not inject:

- full chat history;
- full logs;
- all reference files;
- stale plans;
- conflicting memories without warning;
- project-specific dogfooding notes from unrelated work.

For the detailed CMS memory model, see `cms-context-memory.md`.

## 8. Tool Classes

Host gates should distinguish tool classes:

| Tool class | Meaning | Default gate |
| --- | --- | --- |
| data | read-only context retrieval | allow with audit |
| action | file write, command, API call, external side effect | gate by risk |
| orchestration | call another agent, schedule work, start a loop | require role/budget policy |

Suggested metadata:

```yaml
tool_class: data | action | orchestration
side_effects: none | local_files | external_api | production_data
requires_gate: true
audit_level: low | medium | high
```

## 9. State Write Safety

Runtime state writes should be ACID-like where possible:

- write temp file first;
- validate JSON or schema;
- atomically replace when possible;
- append JSONL as one valid line;
- run a read-only checker after state updates;
- never store secrets, credentials, or raw private documents.

If a state write is interrupted, the next loop should recover from the highest
authority files first: target, acceptance, stop rules, latest valid state, then
logs.

## 10. What To Remove From Reusable References

Remove or do not add:

- active project status;
- project-specific paths;
- full dogfooding transcripts;
- exact provider secrets or account setup;
- one-off environment failures;
- raw external article text;
- product-specific feature flags unless shown only as examples;
- rules that cannot be generalized.

Promote only reusable patterns:

- hook contracts;
- evidence format;
- stop gates;
- context packet shape;
- memory classification;
- tool classes;
- checker/evaluator rules.

