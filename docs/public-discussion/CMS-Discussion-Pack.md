# CMS Public Discussion Pack

状态：Draft  
日期：2026-06-10  
用途：公开讨论 AI Coding Management System, CMS。  

## Positioning

CMS is not presented as an invention or a finished framework. It is a research direction and practice discussion based on practical experience in purchasing, new product development, food production, quality control, SOP design, risk prevention, abnormal handling, review, and action planning.

中文定位：

> CMS 不是“发明”，而是把 20 年采购、新品研发、食品生产和品质管理经验迁移到 AI Coding Agent 管理的一次研究讨论。目标是邀请更多人一起验证、反驳和改进。

## Core Hypothesis

AI coding agents are best managed as fast, knowledgeable, but inexperienced workers:

- They know a lot.
- They execute quickly.
- They often lack working discipline.
- They may stop after one step.
- They may report Done without evidence.
- They may lose context.
- They may not escalate unsafe situations.

CMS asks:

> Can lightweight target contracts, acceptance criteria, loop state, audit logs, and a deterministic checker reduce false Done, target drift, and evidence-free delivery?

## What Is Being Shared

This pack supports public discussion around:

- The CMS concept.
- CMS Lite v0.1.
- The `agent-loop-engineering` Skill.
- The minimum templates.
- The `agent-loop-check.ps1` checker.
- Three test scenarios.

## Suggested Public Files

| File | Purpose |
| --- | --- |
| `CMS-Short-Post-ZH.md` | Chinese short post / article draft |
| `CMS-RFC-Template.md` | GitHub issue / discussion RFC |
| `CMS-Experiment-Report-Template.md` | Test result template |
| `CMS-Agent-Review-Prompt.md` | Prompt for other Agents to review CMS |

## Recommended Message

Use this tone:

> This is an early research draft, not a finished framework. I am exploring whether production-management experience can help manage AI coding agents. The first test is CMS Lite v0.1: four files and one checker to prevent false Done and evidence-free completion. Feedback and counterexamples are welcome.

## Current MVP

CMS Lite v0.1 uses:

```text
Docs/
  TARGET.md
  ACCEPTANCE.md
  LOOP_STATE.md
  LOOP_LOG.jsonl
```

and:

```text
agent-loop-check.ps1
```

The checker currently focuses on:

- Missing target.
- Missing acceptance criteria.
- Invalid state.
- Done without evidence.
- Continue without one clear next action.
- Blocked without reason.
- Invalid log JSONL.
- Invalid scenario guess.
- Rough code size.

## What Not To Claim

Avoid claiming:

- CMS solves all AI coding problems.
- CMS replaces human judgment.
- CMS proves TPS / HACCP / ISO directly apply to software.
- CMS is already a complete automation platform.
- CMS is a finished standard.

Better claim:

- CMS is a practical research direction.
- CMS Lite is a testable MVP.
- The goal is to reduce known Agent failure modes.
- The system should be judged by experiments.

## Discussion Questions

1. Is the “AI Agent as fast but inexperienced worker” model accurate?
2. Is CMS Lite still too heavy for small tasks?
3. Are four files too many for testing?
4. Is `LOOP_STATE.md` a better MVP than separate `STATUS.md`, `NEXT_ACTIONS.md`, and `EVALUATION.md`?
5. Is `Invalid State` useful as a checker-only state?
6. What should count as evidence for Done?
7. Can a deterministic checker reduce false Done?
8. When should independent Evaluator be required?
9. Should MCP wait until checker and runner are stable?
10. Which real scenarios can disprove CMS?

