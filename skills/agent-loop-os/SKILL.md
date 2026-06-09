---
name: agent-loop-os
description: "Use when an AI coding agent needs bounded development loops, persistent project-local Docs/ state, context budgeting, environment escalation rules, safe stop gates, and Done / Done with Risk / Blocked completion decisions across Codex, Claude Code, OpenCode, Cline, Qoder, CodeBuddy, Trae, Gemini CLI, Aider, GitHub Actions, or other AI coding agents."
---

# Agent Loop OS

Version: 1.0.0

## 中文快速说明

Agent Loop OS 是一个面向 AI Coding Agent 的编码循环总控 Skill。它把用户目标、验收标准、当前状态、待办、停止规则、完成判定和每轮记录保存在项目自己的 `Docs/` 目录中，让 Codex、Claude Code、OpenCode、Cline、Qoder、CodeBuddy、Trae、Gemini CLI、Aider、GitHub Actions 等不同 Agent 可以接力同一个开发工作。

核心原则：

- 状态保存在项目文件里，不依赖聊天记忆。
- Runner 可以替换，`Docs/` 协议不变。
- 每轮只做一个有边界的 coding loop。
- 遇到密钥、账号、生产数据、系统安装、不可逆 Git 操作、技术栈替换或方向冲突时必须停止并问人。
- 只有自动验证和功能验证等证据足够时，才可以标记 `Done`。
- 多 Agent 共用时必须串行写入或使用文件锁，不能同时改同一套 `Docs/` 状态文件。

推荐入口：

- 编码循环、长期实现、验证门禁、停止门禁：使用 `agent-loop-os`。
- 非编码研究、资料接入、知识治理：使用 `ai-workflow-os` 或 `web-search-rules`。
- 用户明确说 checkpoint、收工、交接：使用 `daily-workflow`，但要保留 Agent Loop OS 的 loop evidence。

## Purpose

Use this skill as the top-level controller for AI coding work only. The goal is to turn development into a managed loop:

```text
Target -> Plan -> Implement -> Verify -> Review -> Fix -> Evaluate -> Continue or Stop
```

Do not rely on chat history as memory. Persist the working state in the project's own `Docs/` directory so any agent can resume after context loss, a new session, or a different runner.

For non-coding workflow governance, research intake, knowledge-base work, or cross-source synthesis, use `ai-workflow-os`. For coding-loop control, implementation direction, stop gates, and completion gates, this skill is authoritative.

## Core Rule

State is stable. Runner is replaceable. Stop rules are universal.

- Store project goals, acceptance criteria, status, pending work, evaluation, and loop history in `Docs/`.
- Treat each agent run as one bounded loop, not an unlimited session.
- Read only the minimum project state needed for the current loop.
- Stop when a hard gate, budget gate, direction gate, or validation gate is triggered.
- Mark completion only when evidence supports it.
- Resolve state conflicts in this order: `TARGET.md` -> `ACCEPTANCE.md` -> `STATUS.md` -> `PENDING.md` -> `NEXT_ACTIONS.md`.
- Use canonical `Docs/` file names. Legacy aliases may be read for migration, but write canonical files only.

## Flow

```text
Bootstrap if Docs/ is missing
  -> Loop Start
  -> Verify target and acceptance
  -> Discover project verification commands
  -> Execute one bounded implementation loop
  -> Run automatic and functional verification
  -> Completion or stop gate
  -> Write state and user report
```

## Related Skills

Route to existing skills only when needed:

1. Use `project-lifecycle-navigator` when `Docs/TARGET.md` is missing, the user cannot state the goal in one sentence, multiple goals conflict, or MVP boundaries are unclear. If unavailable, use the bootstrap questions in `references/bootstrap.md` and stop for confirmation when the target remains unclear.
2. Use `ai-workflow-os` for multi-source research decisions, knowledge intake governance, cross-module audits, or non-coding workflow governance. Do not route pure code verification or bug-fix loops to it. If unavailable, keep coding-loop state in this skill and record unresolved governance work in `Docs/PENDING.md`.
3. Use `daily-workflow` when the user explicitly asks to checkpoint, wrap up, recover after context loss, or create a standalone handoff. During a coding loop, keep lightweight loop updates in this skill. If unavailable, write `Docs/HANDOFF.md` using `references/loop-state-protocol.md`.
4. Use `web-search-rules` when using external web pages, API docs, uploaded files, or other sources that require trust and provenance handling. If unavailable, use primary sources where possible and record source limits in `Docs/STATUS.md`. In a coding loop, write the short research conclusion to `Docs/STATUS.md` compressed context or `Docs/PENDING.md`; use the full intake path only when the task is research/governance-heavy.

Do not load every related skill every loop. Load the narrow skill or reference file that answers the current question.

## Required Project State

Use project-local `Docs/` files. Create missing files conservatively from the schemas in `references/loop-state-protocol.md`.

Minimum reused files:

- `Docs/TARGET.md`
- `Docs/STATUS.md`
- `Docs/PENDING.md`
- `Docs/NEXT_ACTIONS.md`
- `Docs/HANDOFF.md` when a standalone handoff is needed

Agent Loop OS files:

- `Docs/LOOP_CONFIG.md`
- `Docs/ACCEPTANCE.md`
- `Docs/EVALUATION.md`
- `Docs/STOP_RULES.md`
- `Docs/LOOP_RUNS.jsonl`
- `Docs/COMPLETED.md`

Canonical file names are `TARGET.md`, `STATUS.md`, `COMPLETED.md`, `PENDING.md`, `NEXT_ACTIONS.md`, and `HANDOFF.md`. Read legacy aliases only for migration, such as `PROJECT_TARGET.md`, `PROJECT_STATUS.md`, `COMPLETED_JOBS.md`, `PENDING_JOBS.md`, `NEXT_STEPS.md`, or `SCHEDULE.md`; after migration, write the canonical files.

If `Docs/` does not exist or both `Docs/TARGET.md` and `Docs/ACCEPTANCE.md` are missing, follow `references/bootstrap.md` before coding.

## Loop Start

At the start of each loop:

1. Read `Docs/LOOP_CONFIG.md` if it exists; otherwise use the default budget below.
2. Check file consistency using the priority order in Core Rule.
3. Read `Docs/TARGET.md` and `Docs/ACCEPTANCE.md`.
4. Read only the latest compressed context in `Docs/STATUS.md`.
5. Read only Immediate and Blockers sections from `Docs/PENDING.md`.
6. Read `Docs/NEXT_ACTIONS.md`.
7. Read project manifests such as `package.json`, `pyproject.toml`, `Makefile`, `Cargo.toml`, `go.mod`, `pom.xml`, or repository docs to identify test, lint, build, typecheck, and functional verification commands. Record discovered commands in `Docs/LOOP_CONFIG.md`.
8. If the target or acceptance criteria are missing, create or propose them before coding.
9. If the next action conflicts with the target, stop and ask for direction unless the user explicitly requested a target revision.

Default budget:

```yaml
protocol_version: 1
runner: generic
max_loops: 5
max_consecutive_failures: 2
max_runtime_minutes: 60
max_context_files_per_loop: 8
max_recent_loop_records: 5
require_double_evidence_for_done: true
core_verification: test
max_compressed_context_lines: 40
log_directory: .agent/logs
verification_commands:
  test: null
  typecheck: null
  build: null
  lint: null
  functional: null
progress_signals:
  - new passing verification
  - narrower failing scope
  - changed root cause with evidence
  - implemented accepted next action
allow_parallel_tasks: false
allow_project_dependency_install: true
allow_project_config_changes: true
allow_system_install: false
allow_secret_access: false
allow_production_data_access: false
allow_destructive_changes: false
```

`max_consecutive_failures` counts only consecutive failures of `core_verification`. If core verification fails but a configured progress signal is present, do not increment the consecutive failure count for that loop. Other verification failures must be recorded in `Docs/EVALUATION.md`, but they do not consume this budget unless `Docs/LOOP_CONFIG.md` defines a stricter project-specific rule.

For simple bug fixes, use 3-5 loops. For multi-file features, 8-10 loops may be reasonable. Keep `max_loops` below 20 unless the user explicitly approves a longer run.

## Loop Execution

For coding work, run one bounded cycle:

```text
Select next action -> Implement minimal change -> Run verification -> Review result -> Fix if safe -> Evaluate status
```

The agent may automatically handle project-local problems listed in `references/environment-escalation.md`. The agent must stop and ask a human for anything outside that whitelist.

At the end of every loop, update the touched acceptance criteria in `Docs/ACCEPTANCE.md` under `Current evidence`. If a criterion is blocked, name the unmet criterion ID or heading in `Docs/EVALUATION.md` and `Docs/PENDING.md`.

Loop-end write contract:

1. Append the gate decision and evidence to `Docs/EVALUATION.md`.
2. Update `Docs/STATUS.md` compressed context and latest verification.
3. Update `Docs/ACCEPTANCE.md` current evidence for touched criteria.
4. Preserve blockers and decisions in `Docs/PENDING.md`.
5. Keep exactly one immediate continuation in `Docs/NEXT_ACTIONS.md`.
6. Append completed items to `Docs/COMPLETED.md` when a user-visible or verification-backed unit is finished.
7. Append one concise record to `Docs/LOOP_RUNS.jsonl`.

`daily-workflow` may create broader checkpoint or handoff summaries when explicitly triggered by the user, but it should not replace the loop-end write contract above.

If the user changes direction, classify it before editing:

- `scope_expansion`: affects no more than 2 `Must Pass` items and does not change `Non-Goals`. Add or adjust affected `Docs/ACCEPTANCE.md` items and record the expansion in `Docs/EVALUATION.md`.
- `target_revision`: changes the user goal, changes any `Non-Goals`, replaces the verification strategy, or affects more than 2 `Must Pass` items. Update `Docs/TARGET.md`, regenerate affected acceptance criteria, append a `target_revision` entry to `Docs/EVALUATION.md`, and continue only after the new target is unambiguous.

If the classification is ambiguous, stop and ask.

## Context Budget

Use progressive reading:

- Always start from the minimum `Docs/` set.
- Read `Docs/LOOP_RUNS.jsonl` only for the last 3-5 records unless debugging loop behavior.
- Do not paste full logs into context. Record command, result, key error summary, and log path.
- Do not paste full conversation transcripts into `Docs/STATUS.md`.
- Keep `Docs/STATUS.md` to the latest 5-10 updates and archive older material.
- Read detailed reference files only when their decision surface is active.

Read `references/context-budget.md` when context size becomes a risk or when designing a long-running loop.

## Stop Rules

Stop immediately and report `Blocked` when the loop needs:

- Secrets, credentials, OAuth, account login, or browser session access.
- Production databases, real user data, paid cloud resources, or external account changes.
- System-level installs, administrator permissions, drivers, or host-level configuration.
- Destructive, irreversible, migration, deletion, overwrite, force-push, reset, history-rewrite, or other irreversible Git operations.
- Technology-stack replacement or major framework upgrade.
- A direction change that conflicts with `Docs/TARGET.md`.

The built-in hard stops in this section and `references/environment-escalation.md` are authoritative. `Docs/STOP_RULES.md` may add stricter project rules. It may not loosen hard stops unless a human approval is recorded under `Docs/STOP_RULES.md` -> `Overrides` with scope and expiration, and that override still cannot permit secret exposure, production data access, or irreversible action without explicit human confirmation for that run.

The `allow_*` flags in `Docs/LOOP_CONFIG.md` cannot override hard stops. They only control whether otherwise safe, project-local whitelist actions are allowed by default.

Stop on budget when:

- `max_loops` is reached.
- `max_consecutive_failures` is reached.
- `max_runtime_minutes` is reached.
- Context cannot be reduced enough to continue safely.

Record every stop in `Docs/EVALUATION.md`, `Docs/PENDING.md`, `Docs/NEXT_ACTIONS.md`, and `Docs/LOOP_RUNS.jsonl`.

When `max_context_files_per_loop` would be exceeded, queue optional reads, summarize already-read material first, and continue only if the loop can still be completed safely. If the agent cannot decide without exceeding the budget, stop as `Blocked`.

## Completion Gate

Use only these states:

- `Done`: all success criteria are satisfied and at least two evidence classes support completion, including automatic verification and functional verification.
- `Done with Risk`: the core goal is met, but there are explicit unverified edges, skipped checks, or environment limits.
- `Blocked`: work cannot continue or completion cannot be judged without human input, permission, credentials, environment access, or a direction decision.
- `Continue`: bounded next action exists and no stop rule is triggered.

Read `references/completion-gate.md` before declaring `Done` or `Done with Risk`.

Before ending any loop, run the checklist in `references/self-check.md`.

## Runner Adapters

This skill is runner-neutral. Use `references/runner-adapters.md` when adapting the loop to Codex, Claude Code, OpenCode, Cline, Qoder, CodeBuddy, Trae, Gemini CLI, Aider, GitHub Actions, or a local scheduler.

All adapters must:

- Load state from `Docs/`.
- Respect stop rules.
- Write evaluation and loop records before exiting.
- Avoid product-specific assumptions in project state files.

## User Report

For each loop, report concisely:

```text
Loop status: Continue / Done / Done with Risk / Blocked
- Target alignment:
- Work completed:
- Verification:
- Risks/blockers:
- Files updated:
- Next action:
```

Use the user's language by default.

The chat report is for the user. Also append the decision and evidence to `Docs/EVALUATION.md`.
