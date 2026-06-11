# RFC: AI Coding Management System / CMS Lite v0.1

## Summary

This RFC proposes CMS Lite v0.1, a lightweight control system for AI coding agents. It treats AI coding agents as fast, knowledgeable, but inexperienced workers that need target contracts, acceptance criteria, evidence gates, loop state, logs, and checker validation.

This is a research discussion, not a finished standard.

## Background

The proposal is based on practical experience in purchasing, new product development, food production, quality control, SOP design, risk prevention, abnormal handling, review, and action planning.

The working hypothesis:

> AI coding agents often fail not because they cannot write code, but because they lack stable working discipline and external management controls.

## CMS Lite v0.1

Required test files:

```text
Docs/
  TARGET.md
  ACCEPTANCE.md
  LOOP_STATE.md
  LOOP_LOG.jsonl
```

Checker:

```text
agent-loop-check.ps1
```

## Checker Scope

The checker should detect:

- Missing target.
- Missing acceptance criteria.
- Invalid loop state.
- Done without evidence.
- Done while failed checks exist.
- Continue without exactly one next action.
- Blocked without reason.
- Stop rule conflicts.
- Invalid JSONL log.
- Invalid scenario guess.
- Rough code size / changed file count.

The checker should not judge:

- Code elegance.
- Architecture quality.
- UI quality.
- Whether acceptance criteria are semantically perfect.
- Whether code size alone proves project type.

## Test Scenarios

| Scenario | Goal |
| --- | --- |
| Small bug fix | Check whether CMS Lite is too heavy |
| Medium feature | Check whether evidence gate reduces false Done |
| Long refactor | Check whether loop state prevents target drift |

## Questions for Review

1. Is the model of “AI Agent as fast but inexperienced worker” useful?
2. Is CMS Lite still too heavy?
3. Should small tasks use files, or only final response evidence?
4. Are `TARGET.md`, `ACCEPTANCE.md`, `LOOP_STATE.md`, and `LOOP_LOG.jsonl` the right MVP files?
5. Should `Invalid State` exist as checker-only status?
6. What evidence should be required for Done?
7. Should checker be deterministic only?
8. When should independent Evaluator be required?
9. Should MCP be delayed until checker and runner are stable?
10. What real scenario would disprove CMS Lite?

## Requested Feedback

Please provide:

- What should be removed.
- What should be simplified.
- What should be tested first.
- Which rules are too strict.
- Which rules are not strict enough.
- Any real task results if you test it.

