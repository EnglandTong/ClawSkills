# CMS, Context, and Memory

Use this reference when an AI coding loop needs context control, project memory,
knowledge retrieval, or a small assistant layer for memory distillation.

This reference is intentionally implementation-neutral. It does not assume a
specific product such as MyWork, OpenCode, Cursor, Claude Code, or Codex.

## 1. CMS Principle

Agent Loop Engineering treats a coding agent as:

```text
high knowledge + weak long-term memory + weak work discipline
```

The CMS exists to provide the missing work discipline:

- clear target;
- bounded work order;
- acceptance evidence;
- stop rules;
- context budget;
- durable state;
- role handoff;
- review and QA gates.

Do not solve CMS problems by adding more prompt text. Build a smaller, cleaner
work packet.

## 2. Layer Model

Keep these layers separate:

| Layer | Purpose | Examples |
| --- | --- | --- |
| Harness | safe single-agent execution | tools, permissions, hooks, logs, sandbox |
| Context | what the model sees now | current task packet, retrieved facts, non-goals |
| Loop | continue / retry / route / stop | completion gate, budget, stop rules |
| Orchestration | coordinate roles, models, agents, worktrees, schedules | future runner or multi-agent scheduler |

Rule:

```text
Do not build orchestration before harness and loop contracts are stable.
Do not mix runtime tool control with project completion authority.
```

## 3. Context Packet

Context is not a dump of everything the project knows. It is a current work
packet for one role.

Minimum shape:

```yaml
context_packet:
  role: Developer | Reviewer | QA | Controller | Archivist
  work_order: one current task
  target: only relevant goal and non-goals
  acceptance: only current acceptance rows
  constraints: stop rules and allowed scope
  recent_state: compressed latest status
  evidence: latest relevant validation only
  next_action: one intended action
  exclusions: what not to do
```

Good context is:

1. enough to avoid missing the target;
2. small enough to avoid confusion;
3. structured enough that the agent knows what to do with it.

Bad context:

- full chat history;
- full raw logs;
- stale plans;
- duplicate acceptance criteria;
- old failed attempts with no summary;
- entire reference folders read every loop;
- retrieved notes that conflict with the active work order.

## 4. Context Budget Tiers

Use tiers instead of "read everything".

| Tier | Use case | Suggested size | Suggested max project files |
| --- | --- | ---: | ---: |
| Lite | small bug, single file, clear acceptance | 3k-6k tokens | 3-5 |
| Standard | normal feature or review | 6k-12k tokens | 5-8 |
| Deep | repeated failure, architecture boundary, high-risk refactor | 12k-25k tokens | 8-12 |
| Rich | exceptional incident or design review | explicit approval | case by case |

Default:

```text
Start Lite. Escalate only when evidence shows missing context caused failure or risk.
```

## 5. Context Composition Ratio

For normal coding loops, aim for:

| Context type | Target share |
| --- | ---: |
| Task authority: work order and acceptance | 30-40% |
| Current code facts | 30-40% |
| State and evidence | 10-20% |
| Rules and guardrails | 10-15% |
| External reference / general theory | 0-5% |

If rules, history, or reference material dominate the packet, the agent is more
likely to confuse priorities.

## 6. Memory Products

Do not treat "memory" as one bucket.

| Memory product | Stores | Use |
| --- | --- | --- |
| Personal Memory | stable user preferences and working style | shape collaboration defaults |
| Context Essence Memory | distilled current-task facts that must survive compaction | preserve continuity |
| Specialist Knowledge Base | curated external or domain knowledge | inform planning and implementation |

Rules:

```text
Personal Memory shapes how to work.
Context Essence Memory preserves what matters now.
Specialist Knowledge Base informs what might help.
Current WORK_ORDER / ACCEPTANCE / STOP_RULES decide what must be done.
```

## 7. Memory Authority

Use this authority order:

```text
Current work order
-> current acceptance criteria
-> stop rules
-> current compressed status
-> retrieved project memory
-> specialist knowledge
-> personal preference
-> external general reference
```

Retrieved memory is a hint, not authority. If retrieved memory conflicts with
the current work order or acceptance criteria, stop as `Invalid State` or ask
the Controller/user.

## 8. Memory Distillation Pipeline

Raw input should not become long-term memory directly.

```text
raw interaction / command / article / finding
-> classify
-> extract candidate fact
-> verify or mark confidence
-> assign memory product
-> compress
-> store with source
-> retrieve only when relevant
```

Classification guide:

| Input | Default destination |
| --- | --- |
| stable user preference | Personal Memory |
| current task decision | Context Essence Memory |
| verified architecture fact | Project memory / Context Essence |
| external article insight | Specialist Knowledge Base |
| one-off command failure | loop log only |
| repeated command failure pattern | project memory after review |
| active blocker | pending/status, not long-term knowledge |

## 9. Memory Purity Rules

To avoid context pollution:

1. Store facts, not transcripts.
2. Store decisions with dates and source paths.
3. Mark confidence: `high`, `medium`, or `low`.
4. Mark scope: user, project, task, role, or domain.
5. Add expiry or superseded notes when facts may become stale.
6. Retrieve fewer, stronger facts instead of many weak facts.
7. Do not promote speculation to durable memory.
8. Do not let old memory override active project authority files.

Suggested fact shape:

```yaml
memory_fact:
  id:
  scope: personal | context_essence | specialist_knowledge
  statement:
  source:
  confidence: high | medium | low
  applies_when:
  expires_or_superseded_by:
  last_used_at:
```

## 10. Knowledge Retrieval Flow

Before adding prior knowledge to a loop:

```text
1. Extract query from current work order:
   goal, package, feature, role, risk, error class.
2. Search only relevant memory scopes.
3. Rank by current work relevance and freshness.
4. Compress into 3-7 facts.
5. Attach source paths.
6. Drop anything that does not change the next action.
```

Retrieval output:

```markdown
## Retrieved Facts

- Fact:
  Source:
  Why it matters now:
  Confidence: high / medium / low
```

Do not pass search dumps to the coding agent. Pass selected facts.

## 11. Memory & Context Steward

A small model or lightweight assistant can be useful, but only as a narrow
pre-processing layer.

Good Steward responsibilities:

- classify memory;
- extract concise facts;
- build a Context Packet;
- suggest next role;
- flag missing evidence or authority conflicts;
- compress loop feedback.

The Steward must not:

- write final code;
- make architecture decisions;
- override work order / acceptance / stop rules;
- mark final Done;
- silently update durable memory;
- decide high-risk privacy, cloud, production-data, or secret actions alone.

Recommended output style is JSON-only with:

- classification;
- facts with source and confidence;
- context packet include/exclude lists;
- route suggestion;
- risk flags;
- quality/conflict flags.

Do not fine-tune a Steward model until the schema is stable, an evaluator exists,
and at least 100 accepted examples exist. Until then, use prompt + schema +
evaluator.

## 12. What Does Not Belong In This Skill

Do not put these into the reusable Skill/reference layer:

- active project work-order status;
- product-specific file paths such as a single app's runtime directory;
- raw dogfooding logs;
- full external article summaries;
- one-off environment failures;
- agent self-praise or unverified claims;
- project-specific provider secrets, feature flags, or account setup;
- rules that only apply to one repository unless generalized.

Instead:

| Content | Destination |
| --- | --- |
| active project state | that project's `Docs/` |
| reusable method | Skill reference |
| one-off failure | loop log |
| repeated failure pattern | checker/test/lint/gate rule |
| external research | Specialist Knowledge Base summary with source |
| user preference | Personal Memory |

## 13. Implementation Order

Recommended sequence:

1. Define Context Packet shape.
2. Keep role-specific minimum read sets.
3. Require compressed loop feedback.
4. Add checker/evaluator rules for state and memory quality.
5. Add local index over selected project docs and specialist notes.
6. Retrieve top 3-7 facts for a work order.
7. Record which facts were used.
8. Add runtime session memory.
9. Add role/model routing.
10. Add multi-agent serial handoff and health UI.

Do not start with vector search, fine-tuning, or autonomous memory writes.

