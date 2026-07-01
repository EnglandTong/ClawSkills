---
name: cms-project-governance
description: Governance workflow for long-running AI coding projects using CMS-style Milestones, Programs, Work Orders, Controller/QA review, acceptance records, rebaseline reviews, roadmap reviews, and Developer briefs. Use when Codex is asked to plan or dispatch multi-step project work, review Developer handoffs, decide Accepted / Accepted With Risk / Failed / Blocked, audit evidence, run a milestone retrospective, define a current-stage finish line, or prevent project scope drift. Do not use for ordinary single coding loops; use agent-loop-engineering for lightweight implementation and verification.
---

# CMS Project Governance

## Overview

Use this skill as the full CMS governance layer for projects that have grown beyond a single lightweight coding loop. It coordinates planning, dispatch, QA acceptance, evidence review, rebaseline checks, and roadmap finish-line decisions.

This skill must stay project-neutral. Do not hard-code repository names, customer names, local absolute paths, product-specific subsystem names, credentials, or environment assumptions into skill files.

## Relationship To Agent Loop Engineering

- Use `agent-loop-engineering` for lightweight coding execution: target, acceptance, loop state, evidence, checker, and Done gates.
- Use `cms-project-governance` for higher-level project control: Milestones, Programs, Work Orders, Controller/QA review, Rebaseline Review, Roadmap Review, and Developer Briefs.
- Governance may dispatch work to a Developer, but this skill does not implement product code.

## Mode Selection

Choose exactly one mode for the current request.

| User need | Mode | Reference |
| --- | --- | --- |
| Review Developer handoff, rerun evidence, accept or reject work | Controller / QA Acceptance | `references/controller-qa-contract.md` |
| Plan a Milestone, Program, or ordered Work Orders | Program Planning / Dispatch | `references/controller-qa-contract.md` |
| Check drift after several Milestones or risk accumulation | Rebaseline Review | `references/rebaseline-review-prompt.md` |
| Summarize whole project roadmap, finish line, next stage | Project Roadmap Review | `references/project-roadmap-review-prompt.md` |

If the task is a normal implementation request with no Milestone, Program, Work Order, handoff, QA, or rebaseline language, do not use this skill; use the normal coding workflow or `agent-loop-engineering`.

## Required Governance Rules

- Do not write product implementation code in Controller/QA, Rebaseline, or Roadmap Review mode.
- Do not mark work accepted from Developer claims alone.
- Treat evidence as source of truth: tests, builds, logs, screenshots, API responses, files changed, and reproducible commands.
- Distinguish `Accepted`, `Accepted With Risk`, `Failed`, and `Blocked`.
- Treat `Developer Complete` as not accepted until Controller/QA records acceptance.
- Treat `Accepted With Risk` as debt that must remain traceable.
- Stop for Owner decision when scope, non-goals, production data, credentials, protected architecture boundaries, deployment, destructive operations, or external paid resources are involved.
- Keep generated governance files inside the active project workspace, normally under that project's `Docs/` folder.

## Source Of Truth

Before making governance decisions, read the relevant project-local docs that exist. Common files include:

- `Docs/TARGET.md`
- `Docs/ACCEPTANCE.md`
- `Docs/STATUS.md`
- `Docs/NEXT_ACTIONS.md`
- `Docs/PENDING.md`
- `Docs/COMPLETED.md`
- `Docs/EVALUATION.md`
- `Docs/LOOP_RUNS.jsonl`
- `Docs/STOP_RULES.md`
- `Docs/LOOP_CONFIG.md`
- `Docs/MILESTONE_*.md`
- `Docs/*PROGRAM*.md`
- `Docs/WORK_ORDER_*.md`
- `Docs/HANDOFF_*_DEVELOPER.md`
- `Docs/QA_*_ACCEPTANCE_*.md`

If a file is missing, do not invent its content. State the missing file and whether the missing file blocks the decision.

## Output Discipline

Governance outputs must be actionable. Every finding should include:

- affected Milestone, Program, Work Order, or acceptance criterion;
- observed evidence or evidence gap;
- decision or risk;
- required correction or next action;
- owner: Developer, Controller/QA, Owner, or blocked external party;
- verification required after correction.

When creating files, use project-neutral names from the selected reference unless the user's project already has a naming convention.
