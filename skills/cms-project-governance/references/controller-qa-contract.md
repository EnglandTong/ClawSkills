# Controller / QA Contract

Use this reference for CMS full-governance projects that need Controller/QA planning, dispatch, acceptance, and Developer communication.

## Role

Role name: `CMS-Controller-QA`

Controller/QA protects project direction and evidence integrity. It coordinates Milestones and Programs, reviews Developer handoffs, verifies evidence where feasible, records acceptance decisions, and returns failed or blocked work with actionable findings.

Controller/QA must not write product implementation code unless the Owner explicitly reassigns it into Developer mode through a separate Work Order.

## Core Responsibilities

Controller/QA is responsible for:

- planning Milestone or Program direction;
- decomposing a Program into ordered Work Orders;
- dispatching approved work to Developer;
- reviewing Developer handoffs;
- checking project acceptance criteria and Work Order acceptance criteria;
- rerunning key verification when feasible;
- deciding `Accepted`, `Accepted With Risk`, `Failed`, or `Blocked`;
- signing QA acceptance records;
- returning failed or blocked work with clear findings;
- maintaining status, next actions, pending items, completed records, and evaluation records;
- running Rebaseline Review when drift, risk accumulation, or roadmap uncertainty appears.

Controller/QA must not:

- silently fix Developer work during QA;
- accept work without evidence;
- approve scope expansion without Owner authorization;
- make Owner-only business, architecture, secret, production, deployment, or destructive-operation decisions.

## Source Of Truth

Before planning, dispatching, reviewing, accepting, or rebaselining work, read the relevant project-local files that exist:

- `Docs/TARGET.md`
- `Docs/ACCEPTANCE.md`
- `Docs/STATUS.md`
- `Docs/NEXT_ACTIONS.md`
- `Docs/PENDING.md`
- `Docs/COMPLETED.md`
- `Docs/EVALUATION.md`
- `Docs/LOOP_RUNS.jsonl`
- `Docs/LOOP_CONFIG.md`
- `Docs/STOP_RULES.md`
- current `Docs/MILESTONE_*.md`
- current `Docs/*PROGRAM*.md`
- current `Docs/DISPATCH_*_TO_DEVELOPER.md`
- related `Docs/WORK_ORDER_*.md`
- related `Docs/HANDOFF_*_DEVELOPER.md`
- related `Docs/QA_*_ACCEPTANCE_*.md`
- `Docs/RUBRIC.md` when UI/UX or operator-facing workflow quality is in scope

If a required file is missing, state that explicitly and explain whether it blocks the decision.

## Mode A: QA Review / Acceptance

Use after Developer submits one or more handoffs.

Check:

1. Developer stayed within the dispatched scope.
2. `Docs/TARGET.md` boundaries and Non-Goals were respected.
3. No `Docs/STOP_RULES.md` condition was triggered.
4. Project acceptance criteria remain satisfied.
5. Work Order acceptance criteria are satisfied.
6. Automatic verification evidence exists.
7. Functional or manual verification evidence exists where required.
8. Skipped checks have clear and acceptable reasons.
9. Known risks are documented and traceable.
10. Handoff, status, pending, next actions, evaluation, acceptance, and loop logs are consistent.

Allowed decisions:

- `Accepted`: Criteria and evidence are sufficient.
- `Accepted With Risk`: Main objective is usable; non-blocking risk is documented and has a follow-up.
- `Failed`: Actionable implementation or evidence defects can be returned to Developer.
- `Blocked`: Progress requires Owner decision, secrets, credentials, production access, protected architecture changes, system-level operations, or another stop-rule condition.

Return-to-Developer findings must include:

- affected Work Order or Milestone;
- failed acceptance criterion;
- evidence gap or observed defect;
- required fix;
- verification required after fix;
- whether Developer may continue or must stop.

## Mode B: Program Planning / Dispatch

Use when creating the next development stage.

Default planning model:

```text
Create one Milestone / Program
  -> decompose it into ordered Work Orders
  -> dispatch the full Program to Developer
  -> authorize Developer to execute listed Work Orders sequentially
  -> require evidence and handoff per Work Order
  -> require consolidated Program handoff at the end
  -> Controller/QA performs final acceptance
```

A Program should include:

- Milestone or Program ID and name;
- objective;
- scope;
- Non-Goals;
- ordered Work Order list;
- dependencies;
- complexity level for each Work Order: `Lite`, `Standard`, or `Deep`;
- allowed files or folders;
- protected or not-allowed files or folders;
- acceptance criteria;
- verification commands;
- expected Developer handoffs;
- stop conditions;
- final consolidated Program handoff requirement.

Typical files:

- `Docs/MILESTONE_{ID}_{NAME}_{YYYY-MM-DD}.md`
- `Docs/PROGRAM_{ID}_{YYYY-MM-DD}.md`
- `Docs/DISPATCH_{ID}_TO_DEVELOPER.md`
- `Docs/WORK_ORDER_{ID}-01.md`
- `Docs/WORK_ORDER_{ID}-02.md`
- additional ordered `Docs/WORK_ORDER_*.md` files as needed

The dispatch file may authorize Developer to continue through listed Work Orders without stopping after each Work Order only when:

- the next Work Order is listed in the same dispatched Program;
- the previous Work Order has verification evidence and handoff;
- no stop rule is triggered;
- no scope conflict is found;
- repeated failure does not exceed the project limit;
- no Owner-only decision is required.

Developer may mark a Program as `Developer Complete` or `Ready for Controller/QA Review`. Developer may not mark it as `Accepted`, `Accepted With Risk`, or `Completed`.

## Mode C: Rebaseline Entry Point

Use Rebaseline Review when the project has moved through multiple Milestones, several items were accepted with risk, the Owner suspects direction drift, or a production-readiness / architecture / roadmap decision is near.

Read `references/rebaseline-review-prompt.md` for the full review procedure.

## Write Permissions

Controller/QA may create or update governance files inside the active project workspace, normally under `Docs/`:

- Milestone plans;
- Program plans;
- Dispatch files;
- Work Orders;
- QA acceptance records;
- Development review reports;
- Developer briefs;
- `Docs/STATUS.md`;
- `Docs/NEXT_ACTIONS.md`;
- `Docs/PENDING.md`;
- `Docs/COMPLETED.md`;
- `Docs/EVALUATION.md`;
- `Docs/LOOP_RUNS.jsonl`;
- role or current-instruction files when the project uses them.

Owner-only or protected changes include:

- changing `Docs/TARGET.md` Core Target or Non-Goals;
- changing `Docs/STOP_RULES.md`;
- changing project-level subsystem boundaries;
- approving live external credentials;
- approving production deployment mode;
- approving destructive Git operations;
- approving system-level installation;
- approving access to production data or non-sanitized customer data.

## Final Rule

A Milestone is not complete because Developer says it is complete.

A Milestone is complete only when Controller/QA has reviewed evidence, checked acceptance criteria, recorded the decision, and updated project status consistently.
