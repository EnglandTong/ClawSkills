# Project Roadmap Review Prompt

Use this reference when the user asks for an Owner-facing project map, current-stage finish line, next-stage plan, or scope-control review.

The task is not to write code or dispatch new implementation work. The task is to make the overall plan, completed work, remaining work, boundaries, and finish criteria clear.

## Required Reading

Read:

1. `Docs/TARGET.md`
2. `Docs/ACCEPTANCE.md`
3. `Docs/STATUS.md`
4. `Docs/NEXT_ACTIONS.md`
5. `Docs/PENDING.md`
6. `Docs/COMPLETED.md`
7. `Docs/EVALUATION.md`
8. `Docs/LOOP_RUNS.jsonl`
9. `Docs/LOOP_CONFIG.md` if present
10. `Docs/STOP_RULES.md` if present
11. recent `Docs/MILESTONE_*.md`
12. recent `Docs/*PROGRAM*.md`
13. recent `Docs/DISPATCH_*_TO_DEVELOPER.md`
14. related `Docs/WORK_ORDER_*.md`
15. related `Docs/HANDOFF_*_DEVELOPER.md`
16. related `Docs/QA_*_ACCEPTANCE_*.md`
17. existing `Docs/DEVELOPMENT_REVIEW*.md` if present

If files are missing, do not infer their content. List missing files and impact.

## Core Questions

Answer:

1. What was the original project goal?
2. What is completed now?
3. Which completed items are core value versus supporting work?
4. What is not complete?
5. What is complete but risky or drifted?
6. What should continue now?
7. What should stop expanding now?
8. What requires Owner decision?
9. When can the current stage be considered complete?
10. What belongs in a future version instead of the current stage?

## Required Analysis

### 1. Project Overview

```markdown
| Area / Subsystem | Purpose | Current Status | Main Evidence | Risk |
|---|---|---|---|---|
```

Cover top-level governance docs, major product areas, shared services, evidence, reports, exports, approval, operator workflow, and other support modules relevant to the current project.

### 2. Milestone Inventory

```markdown
| Milestone | Planned Goal | Work Orders | Actual Delivery | QA Status | Remaining Gap |
|---|---|---|---|---|---|
```

QA Status must be one of:

- `Accepted`
- `Accepted With Risk`
- `Developer Complete`
- `QA Review`
- `Failed`
- `Blocked`
- `Unknown / Missing Evidence`

### 3. Completed Work Categories

Separate:

- Core Completed: directly supports the project target.
- Supporting Completed: governance, evidence, shared infrastructure, runbooks, UI support, configuration, or other support work.
- Completed With Risk: completed but missing evidence, production validation, end-to-end validation, or quality confidence.
- Misleading / Unclear Completion: status says complete but evidence or QA does not support that conclusion.

### 4. Not Completed / Still Open

```markdown
| Priority | Item | Why It Matters | Current Blocker | Required Next Action |
|---|---|---|---|---|
```

Priority values:

- `P0 Current Stage Must Finish`
- `P1 Current Stage Should Finish`
- `P2 Next Stage Candidate`
- `Future Version`
- `Blocked / Owner Decision Required`

### 5. Current Stage Finish Line

Define checkable completion criteria:

```markdown
## Current Stage Finish Line

Current stage can be considered complete only when:

1.
2.
3.
4.
5.

## Not Required For Current Stage

1.
2.
3.

## Must Not Continue Without Owner Decision

1.
2.
3.
```

### 6. Next Actions

```markdown
| Order | Next Action | Owner | Reason | Expected Output |
|---|---|---|---|---|
```

Next actions must be specific enough to become Work Orders. Avoid vague phrases such as "continue improving the system."

## Required Output Files

Create or update:

1. `Docs/PROJECT_ROADMAP_REVIEW_{YYYY-MM-DD}.md`
2. `Docs/CURRENT_STAGE_FINISH_LINE_{YYYY-MM-DD}.md`
3. `Docs/NEXT_STAGE_PLAN_{YYYY-MM-DD}.md`

If the project has a stable long-term roadmap index, optionally update:

- `Docs/PROJECT_ROADMAP.md`

## Roadmap Review Format

```markdown
# Project Roadmap Review

Date:
Reviewer: CMS-Controller-QA Project Roadmap Reviewer
Scope Reviewed:

## 1. Executive Summary

- Project original target:
- Current overall status:
- Most important completed work:
- Biggest remaining gap:
- Recommended next mode:
- Is current stage closeable now: Yes / No / Partial
- Owner decision required: Yes / No

## 2. Original Plan and Boundary

### Core Target

### Subsystem Boundary

### Non-Goals

### Current Stage Boundary

## 3. Milestone Inventory

| Milestone | Planned Goal | Actual Delivery | QA Status | Risk | Remaining Gap |
|---|---|---|---|---|---|

## 4. Most Important Completed Work

| Area | Completed Work | Why It Matters | Evidence | Status |
|---|---|---|---|---|

## 5. Supporting Completed Work

| Area | Completed Work | Purpose | Evidence | Status |
|---|---|---|---|---|

## 6. Completed With Risk

| Item | Risk | Evidence Gap | Impact | Required Fix |
|---|---|---|---|---|

## 7. Not Completed / Still Open

| Priority | Item | Why It Matters | Blocker | Required Next Action |
|---|---|---|---|---|

## 8. Possible Scope Creep / Should Stop Expanding

| Item | Why It May Be Scope Creep | Recommendation |
|---|---|---|

## 9. Current Stage Finish Line

Current stage can be considered complete only when:

1.
2.
3.
4.
5.

## 10. Not Required For Current Stage

The following should be moved to future backlog or next stage:

1.
2.
3.

## 11. Recommended Next Actions

| Order | Action | Owner | Output | Acceptance Evidence |
|---|---|---|---|---|

## 12. Developer Communication

- Continue:
- Correct:
- Stop:
- Do not touch:
- Evidence required:
- When to stop and report Blocked:

## 13. Owner Decisions Needed

| Decision | Options | Recommended Default | Reason |
|---|---|---|---|
```

## Limits

Do not write code. Do not modify product implementation files. Do not close unaccepted Milestones. Do not treat `Developer Complete` as `Accepted`. Do not treat `Accepted With Risk` as fully complete. Do not expand the project target.

If changing target, stop rules, system boundaries, production mode, external services, credentials, or real data policy is required, mark `Owner Decision Required`.
