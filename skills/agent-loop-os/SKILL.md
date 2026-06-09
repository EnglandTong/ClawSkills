---
name: agent-loop-os
description: "Agent Loop Operating System for AI coding agents. Use when Codex needs to control coding direction, run long-running or repeated development loops, preserve project goals and acceptance criteria in Docs/, reduce context usage, classify environment problems, stop safely on blockers, and decide Done / Done with Risk / Blocked across Codex, Claude Code, OpenCode, Cline, Qoder, CodeBuddy, Trae, Gemini CLI, Aider, GitHub Actions, or other AI coding agents."
---

# Agent Loop OS

Version: 1.0.0

## Purpose

Use this skill as the top-level controller for AI coding work. The goal is to turn development into a managed loop:

```text
Target -> Plan -> Implement -> Verify -> Review -> Fix -> Evaluate -> Continue or Stop
```

Do not rely on chat history as memory. Persist the working state in the project's own `Docs/` directory so any agent can resume after context loss, a new session, or a different runner.

## Core Rule

State is stable. Runner is replaceable. Stop rules are universal.

- Store project goals, acceptance criteria, status, pending work, evaluation, and loop history in `Docs/`.
- Treat each agent run as one bounded loop, not an unlimited session.
- Read only the minimum project state needed for the current loop.
- Stop when a hard gate, budget gate, direction gate, or validation gate is triggered.
- Mark completion only when evidence supports it.
- Resolve state conflicts in this order: `TARGET.md` -> `ACCEPTANCE.md` -> `STATUS.md` -> `PENDING.md` -> `NEXT_ACTIONS.md`.

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

1. Use `project-lifecycle-navigator` when `Docs/TARGET.md` is missing, the user cannot state the goal in one sentence, multiple goals conflict, or MVP boundaries are unclear.
2. Use `ai-workflow-os` when project governance, cross-source synthesis, workflow coordination, or multi-source decision tracking is needed.
3. Use `daily-workflow` when creating checkpoints, handoff summaries, compressed continuation context, or recovery after context loss.
4. Use `web-search-rules` when using external web pages, API docs, uploaded files, or other sources that require trust and provenance handling.

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
log_directory: .agent/logs
verification_commands:
  test: null
  typecheck: null
  build: null
  lint: null
  functional: null
allow_parallel_tasks: false
```

`max_consecutive_failures` means consecutive loops whose core verification still fails or makes no measurable progress. It counts across verification types unless `Docs/LOOP_CONFIG.md` defines a stricter project-specific rule.

For simple bug fixes, use 3-5 loops. For multi-file features, 8-10 loops may be reasonable. Keep `max_loops` below 20 unless the user explicitly approves a longer run.

## Loop Execution

For coding work, run one bounded cycle:

```text
Select next action -> Implement minimal change -> Run verification -> Review result -> Fix if safe -> Evaluate status
```

The agent may automatically handle project-local problems listed in `references/environment-escalation.md`. The agent must stop and ask a human for anything outside that whitelist.

If the user explicitly changes direction, update `Docs/TARGET.md`, regenerate affected acceptance criteria in `Docs/ACCEPTANCE.md`, append a `target_revision` entry to `Docs/EVALUATION.md`, and continue only after the new target is unambiguous. If the direction change is ambiguous, stop and ask.

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
- Destructive, irreversible, migration, deletion, overwrite, or history-rewrite operations.
- Technology-stack replacement or major framework upgrade.
- A direction change that conflicts with `Docs/TARGET.md`.

Stop on budget when:

- `max_loops` is reached.
- `max_consecutive_failures` is reached.
- `max_runtime_minutes` is reached.
- Context cannot be reduced enough to continue safely.

Record every stop in `Docs/EVALUATION.md`, `Docs/PENDING.md`, `Docs/NEXT_ACTIONS.md`, and `Docs/LOOP_RUNS.jsonl`.

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
