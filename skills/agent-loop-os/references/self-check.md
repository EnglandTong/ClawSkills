# Loop Self-Check

Run this checklist before ending each loop.

## Required Questions

- Did I read only the minimum state needed for this loop?
- Is the current action still aligned with `Docs/TARGET.md`?
- Are `Docs/TARGET.md` and `Docs/ACCEPTANCE.md` consistent?
- Did I preserve non-goals?
- Did I run or update the appropriate verification commands?
- Did I record automatic verification evidence?
- Did I record functional verification evidence or explain why it is unavailable?
- Did I update `Docs/EVALUATION.md`, `Docs/PENDING.md`, `Docs/NEXT_ACTIONS.md`, and `Docs/LOOP_RUNS.jsonl`?
- If I stopped, did I name the exact stop rule and human decision needed?
- If I claimed `Done`, do I have dual evidence?

## Failure Handling

If any required answer is no, do not claim `Done`. Use `Continue`, `Done with Risk`, or `Blocked` and record the missing evidence.
