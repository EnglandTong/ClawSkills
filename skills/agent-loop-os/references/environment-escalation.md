# Environment Escalation

Use this file when an AI coding loop hits dependency, configuration, runtime, permission, or infrastructure issues.

## Agent May Handle Automatically

The agent may proceed without asking when the change is project-local, reversible, and verifiable:

- Install dependencies declared by the project manifest or lockfile.
- Restore dependency consistency using the project's package manager.
- Fix test, typecheck, lint, build, import, or script errors caused by the current task.
- Adjust project-local config, test config, mock config, or script paths.
- Resolve local port conflicts by using another development port.
- Add or update mocks, fixtures, sample data, and tests needed for verification.
- Regenerate project-local generated files when the repository already uses that generator.
- Fix regressions introduced by the current loop.

## Must Ask A Human

Stop and ask before:

- Reading, creating, changing, or requesting secrets, tokens, passwords, OAuth sessions, cookies, SSH keys, or `.env` values.
- Accessing production databases, real customer data, paid cloud resources, billing settings, or external accounts.
- Installing system packages, drivers, browser extensions, or anything requiring administrator permissions.
- Changing operating-system, shell, browser, IDE, or global Git configuration.
- Performing deletion, migration, overwrite, history rewrite, force push, reset, or other irreversible actions.
- Replacing the technology stack or doing a major framework/runtime upgrade.
- Changing security posture, authentication, authorization, encryption, data retention, or audit policy.
- Continuing after repeated failures reach the budget in `LOOP_CONFIG.md`.

## Classification Report

When stopping, report:

```text
Environment status: Blocked
- Issue:
- Category:
- Why agent cannot proceed:
- Evidence:
- Human decision needed:
- Safe next action:
```

Also write the stop reason to `Docs/EVALUATION.md`, `Docs/PENDING.md`, `Docs/NEXT_ACTIONS.md`, and `Docs/LOOP_RUNS.jsonl`.
