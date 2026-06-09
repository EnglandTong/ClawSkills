# Context Budget

Long-running coding agents fail when they reread too much history. Prefer progressive disclosure and compressed state.

## Minimum Read Set

At loop start, read only:

1. `Docs/LOOP_CONFIG.md`
2. `Docs/TARGET.md`
3. `Docs/ACCEPTANCE.md`
4. Latest compressed context from `Docs/STATUS.md`
5. Immediate and Blockers sections from `Docs/PENDING.md`
6. `Docs/NEXT_ACTIONS.md`

If `LOOP_RUNS.jsonl` is needed, read only the latest 3-5 records.

## Conditional Reads

- Read `completion-gate.md` only before declaring completion or risk.
- Read `environment-escalation.md` only when a command, dependency, permission, or environment issue appears.
- Read `runner-adapters.md` only when configuring or changing a runner.
- Read `web-search-rules` only for external sources, API docs, uploaded files, or knowledge intake.
- Read lifecycle skills only when scope, MVP, or project stage is unclear.

## Compression Rules

At the end of each loop, keep:

- Current target and whether it changed.
- Decisions made.
- Completed work.
- Verification evidence.
- Open blockers.
- Files touched.
- One immediate next action.

Remove:

- Repeated exploration notes.
- Full command logs.
- Full chat transcripts.
- Old failed attempts that no longer affect the next decision.
- Duplicate summaries.

## Context Stop Gate

Stop with `Blocked` when:

- The agent cannot identify the current target from compressed state.
- The next action depends on missing history that cannot be recovered from files.
- The required context exceeds the configured file or token budget and cannot be summarized safely.

Before stopping, update `PENDING.md`, `NEXT_ACTIONS.md`, `EVALUATION.md`, and `LOOP_RUNS.jsonl`.
