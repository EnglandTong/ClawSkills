# Runner Adapters

Runner adapters explain how different AI coding agents can run the same loop. They must not replace the shared `Docs/` state protocol.

## Universal Adapter Contract

Every runner must:

- Start by reading the minimum `Docs/` set.
- Execute one bounded loop.
- Respect hard and budget stop rules.
- Write `EVALUATION.md`, `PENDING.md`, `NEXT_ACTIONS.md`, and `LOOP_RUNS.jsonl` before exiting.
- Avoid storing product-specific state as the only copy of project memory.

## Codex

Use heartbeat or automation when available. Each wakeup should instruct Codex to:

```text
Use $agent-loop-os in this workspace. Read Docs/LOOP_CONFIG.md and Docs/NEXT_ACTIONS.md, run one bounded loop, then write evaluation and stop/continue status.
```

## Claude Code

Use scheduled prompts or loop workflows. Keep Claude-specific commands outside project state. The prompt should ask Claude to read `Docs/` first, run one loop, and stop on hard gates.

```text
Use the local Agent Loop OS protocol. Read only the minimum Docs/ files, run one bounded loop, update EVALUATION/PENDING/NEXT_ACTIONS/LOOP_RUNS, and stop on hard or budget gates.
```

## OpenCode

Use an external scheduler or command loop. The wrapper should call OpenCode with a prompt pointing to `Docs/NEXT_ACTIONS.md` and a maximum loop budget.

```text
Continue the project from Docs/NEXT_ACTIONS.md. Do one bounded implementation and verification loop. Do not continue after a hard stop; write Blocked state to Docs/.
```

## Cline

Use the VS Code workspace as the execution surface. Cline should treat `Docs/NEXT_ACTIONS.md` as the current task and `Docs/EVALUATION.md` as the stop report.

```text
Read Docs/TARGET.md, Docs/ACCEPTANCE.md, and Docs/NEXT_ACTIONS.md. Execute the next action in this workspace, then update the loop state files before ending.
```

## Qoder

Use project documents as persistent context. Ask Qoder to read only the minimum `Docs/` set and to update loop state before ending the task.

```text
Use project Docs/ as persistent state. Do not rely on prior chat memory. Run one loop, verify, and classify the result as Continue, Done, Done with Risk, or Blocked.
```

## CodeBuddy

Use task decomposition plus project state files. CodeBuddy should not continue from chat memory alone; it should resume from `Docs/STATUS.md` and `Docs/NEXT_ACTIONS.md`.

```text
Resume from Docs/STATUS.md and Docs/NEXT_ACTIONS.md. Keep the work inside Docs/TARGET.md and update EVALUATION.md with evidence before stopping.
```

## Trae

Use workspace tasks and check commands. Trae should run one bounded implementation/verification loop and write the same shared state files.

```text
Read the Agent Loop OS Docs/ files, execute the immediate next action, run discovered verification commands, and stop if any hard gate is triggered.
```

## Gemini CLI and Aider

Use an outer script, manual command, or scheduler. Limit each run by time and failure count. Keep all durable state in `Docs/`, not in CLI history.

```text
Run one bounded coding loop from Docs/NEXT_ACTIONS.md. Use Docs/LOOP_CONFIG.md budgets. Write all durable state back to Docs/ before exiting.
```

## GitHub Actions

Use for CI checks, scheduled diagnostics, issue creation, and repair PRs. Do not use GitHub Actions to access secrets, production resources, or perform destructive changes unless explicitly approved.

Suggested use:

```text
schedule -> run checks -> summarize failure -> open issue or PR -> stop for review
```

## Adapter Selection

Choose the runner by environment availability. If no runner can safely continue, write `Blocked` and tell the user what setup is needed.
