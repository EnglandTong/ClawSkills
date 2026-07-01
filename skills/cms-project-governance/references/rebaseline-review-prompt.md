# Rebaseline Review Prompt

Use this reference when running a CMS project Rebaseline Review.

The task is not to write code or dispatch ordinary development work. The task is to review recent development, inspect drift, evaluate completion quality, organize risks, and recalibrate the next direction.

## Required Reading

Read and follow:

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
14. recent related `Docs/WORK_ORDER_*.md`
15. recent related `Docs/HANDOFF_*_DEVELOPER.md`
16. recent related `Docs/QA_*_ACCEPTANCE_*.md`
17. `Docs/RUBRIC.md` if UI/UX or operator-facing workflow is involved

If a file does not exist, do not guess. List the missing file and its impact.

## Review Scope

Review recent Milestones, Programs, Work Orders, Developer handoffs, QA acceptance records, accepted risks, failed items, blocked items, and open pending items.

Answer:

1. Where is the project now?
2. What was originally planned?
3. What was actually delivered?
4. Which Milestones are aligned, partially aligned, materially drifted, invalid, or blocked?
5. Which accepted risks accumulated into system-level debt?
6. Which completion claims are weak, misleading, or unsupported by evidence?
7. Which direction should the next Program take?
8. What must Developer stop, continue, or correct?
9. Which items require Owner decision?

## Required Analysis

Produce these analyses:

1. Milestone timeline: Milestone, Program, Work Orders, Developer handoff, QA status, and main delivery.
2. Completion assessment: accepted, accepted with risk, Developer Complete but not QA accepted, planned but incomplete, evidence missing, state inconsistent.
3. Plan vs actual drift: Scope Drift, Architecture Drift, Quality Drift, Evidence Drift, UX Drift, Data Drift, Governance Drift, Roadmap Drift.
4. Accepted-With-Risk debt: repeated risks or risks that became systemic.
5. Misleading completion claims: claims that need correction or evidence.
6. Rebaseline decision: choose one of `Continue`, `Correct First`, `QA Freeze`, `Refactor / Rebaseline`, or `Owner Decision Required`.
7. Developer communication: convert conclusions into a brief the Developer can execute.

## Required Outputs

Create or update:

1. `Docs/DEVELOPMENT_REVIEW_REBASELINE_{YYYY-MM-DD}.md`
2. `Docs/DEVELOPER_BRIEF_FROM_REVIEW_{YYYY-MM-DD}.md`

If the project already uses milestone-indexed names, use the existing pattern, for example:

- `Docs/DEVELOPMENT_REVIEW_M{CURRENT}_REBASELINE_{YYYY-MM-DD}.md`
- `Docs/DEVELOPER_BRIEF_M{NEXT}_FROM_REVIEW_{YYYY-MM-DD}.md`

Optionally recommend updates to:

- `Docs/STATUS.md`
- `Docs/NEXT_ACTIONS.md`
- `Docs/PENDING.md`
- `Docs/EVALUATION.md`
- current role or instruction files used by the project

## Development Review Format

```markdown
# Development Rebaseline Review

Date:
Reviewer: CMS-Controller-QA Rebaseline Reviewer
Scope Reviewed:

## 1. Executive Summary

- Current overall status:
- Main conclusion:
- Recommended next mode:
- Owner decision required: Yes / No

## 2. Milestone Timeline Reviewed

| Milestone | Planned Goal | Actual Delivery | QA Status | Risk Level | Alignment |
|---|---|---|---|---|---|

## 3. Completion Assessment

| Area | Planned | Delivered | Evidence | Gap | Decision |
|---|---|---|---|---|---|

## 4. Plan vs Actual Drift

| Drift Type | Finding | Evidence | Severity | Required Action |
|---|---|---|---|---|

## 5. Accepted-With-Risk Debt

| Item | First Appeared | Repeated In | Current Impact | Required Fix |
|---|---|---|---|---|

## 6. Incomplete / Misleading Completion Claims

| Claim | Source | Problem | Correction |
|---|---|---|

## 7. Architecture / Scope Boundary Check

- Still aligned with TARGET.md: Yes / No / Partial
- Boundary violations:
- Potential hidden coupling:
- Protected files or Owner-only decisions involved:

## 8. QA and Evidence Health

- Automatic verification status:
- Functional verification status:
- Browser/UI evidence status:
- Missing evidence:
- Risk of false completion:

## 9. Recommended Rebaseline Decision

Decision:

Reason:

Required corrections before next Milestone:

1.
2.
3.

Allowed next development direction:

1.
2.
3.

Not allowed next:

1.
2.
3.

## 10. Updates Required

- STATUS.md:
- NEXT_ACTIONS.md:
- PENDING.md:
- EVALUATION.md:
- Future Work Orders:
```

## Developer Brief Format

```markdown
# Developer Brief From Rebaseline Review

Date:
From: CMS-Controller-QA Rebaseline Reviewer
To: CMS-Developer

## 1. Current Situation

## 2. What You Should Continue Doing

## 3. What You Must Correct

## 4. What You Must Stop Doing

## 5. Evidence Requirements Going Forward

## 6. Next Authorized Direction

## 7. Blockers / Owner Decisions

## 8. Updated Execution Rules For Next Program
```

## Limits

Do not write code. Do not modify product implementation files. Do not close a Milestone without evidence. Do not mark unverified work as Accepted. Do not create a new direction outside `Docs/TARGET.md`.

If the review requires changing `Docs/TARGET.md`, `Docs/STOP_RULES.md`, architecture boundaries, production mode, external services, credentials, or real data policy, mark `Owner Decision Required`.
