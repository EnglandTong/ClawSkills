# Project Memory / 项目记忆工作流

## Role / 角色

This module preserves project context so the user or another AI can resume work accurately.

本模块保存项目上下文，让用户或下一任 AI 可以准确恢复工作。

When `agent-loop-os` is actively controlling a coding loop, defer loop-specific writes to it. This module may read and summarize `STATUS.md`, `PENDING.md`, `NEXT_ACTIONS.md`, `ACCEPTANCE.md`, `EVALUATION.md`, and `LOOP_RUNS.jsonl`, but it must not overwrite acceptance evidence, latest verification, stop-gate decisions, or loop run records. Use Daily Workflow only for explicit checkpoint, wrap-up, or handoff requests.

当 `agent-loop-os` 正在控制编码循环时，本模块不抢写 loop 专用状态。可以读取和总结 `STATUS.md`、`PENDING.md`、`NEXT_ACTIONS.md`、`ACCEPTANCE.md`、`EVALUATION.md` 和 `LOOP_RUNS.jsonl`，但不得覆盖验收证据、最近验证、停止门禁决策或循环记录。只有用户明确要求 checkpoint、收工或交接时，才交给 Daily Workflow。

## Core Files / 核心文件

```text
Docs/PROJECT.md
Docs/TARGET.md
Docs/STATUS.md
Docs/COMPLETED.md
Docs/PENDING.md
Docs/NEXT_ACTIONS.md
Docs/HANDOFF.md
Docs/CONFIG.md
Docs/archive/YYYY-MM.md
```

## Workflow / 工作流程

### Start Work / 开工

Read existing project files. If none exist, create the minimum project memory set.

读取现有项目文件。如不存在，创建最小项目记忆文件组。

### Checkpoint / 中段检查

Update current status, decisions, blockers, and next actions.

更新当前状态、已做决策、阻碍和下一步。

### Wrap Up / 收工

Summarize completed work, pending work, risks, next actions, and handoff notes.

总结已完成、待办、风险、下一步和交接信息。

### Handoff / 交接

Create a compact, actionable handoff note for the next AI or human.

为下一任 AI 或人员创建简洁可执行的交接说明。

## Legacy Migration / 旧版迁移

If legacy Daily Workflow files exist, migrate by mapping:

如果发现旧版 Daily Workflow 文件，按以下方式迁移：

```text
PROJECT_TARGET.md  -> TARGET.md
PROJECT_STATUS.md  -> STATUS.md
COMPLETED_JOBS.md  -> COMPLETED.md
PENDING_JOBS.md    -> PENDING.md
NEXT_STEPS.md      -> NEXT_ACTIONS.md
SCHEDULE.md        -> NEXT_ACTIONS.md or compatibility alias
```

Do not delete old files automatically.

不要自动删除旧文件。
