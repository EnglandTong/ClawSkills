# Bootstrap Protocol

Use this when a project has no usable `Docs/` loop state.

## Cold Start Decision

If `Docs/` is missing or both `Docs/TARGET.md` and `Docs/ACCEPTANCE.md` are missing:

1. Do not start coding.
2. Inspect lightweight project context, such as README, package manifests, route names, app name, or user request.
3. Draft a target summary and acceptance contract.
4. Ask the user to confirm or correct the target when the goal is not already explicit.
5. Create `Docs/` files only after the target is clear enough to avoid wasted work.

If the user gave a precise, low-risk task with clear acceptance criteria, the agent may create provisional files without a separate confirmation. Mark them as `Provisional` and record the assumption in `Docs/EVALUATION.md`.

## File Creation Order

Create files in this order:

1. `Docs/TARGET.md`
2. `Docs/ACCEPTANCE.md`
3. `Docs/LOOP_CONFIG.md`
4. `Docs/STOP_RULES.md`
5. `Docs/STATUS.md`
6. `Docs/PENDING.md`
7. `Docs/NEXT_ACTIONS.md`
8. `Docs/EVALUATION.md`
9. `Docs/LOOP_RUNS.jsonl`

Create `Docs/HANDOFF.md` only when a standalone handoff is needed.

## Bootstrap Questions

Ask only what is needed to write `TARGET.md` and `ACCEPTANCE.md`:

```text
- What is the user goal?
- What must be true for this to be complete?
- What is out of scope?
- What evidence should prove completion?
- What would count as failure?
```

## Bootstrap Output

After bootstrap, report:

```text
Bootstrap complete / needs confirmation
- Target:
- Success criteria:
- Non-goals:
- Verification plan:
- First next action:
```

Do not proceed to implementation until `TARGET.md` and `ACCEPTANCE.md` are present and not contradictory.
