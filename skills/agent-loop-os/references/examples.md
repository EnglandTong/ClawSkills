# Agent Loop OS Examples

## New Project

User asks to build a new app.

Expected behavior:

1. Create or propose `Docs/TARGET.md`.
2. Create or propose `Docs/ACCEPTANCE.md`.
3. Define non-goals and failure examples.
4. Start implementation only after the target contract is clear.

Do not begin coding from a vague idea.

## Bug Fix

User asks to fix a failing feature.

Expected behavior:

1. Read target and current status.
2. Reproduce or inspect the failure.
3. Make the smallest relevant fix.
4. Run automatic verification.
5. Run or describe functional verification.
6. Update evaluation and next actions.

## Environment Blocker

The agent needs an API key.

Expected behavior:

1. Stop immediately.
2. Do not ask the user to paste the key into chat unless the platform has a secure secret flow.
3. Write `Blocked` to evaluation and pending files.
4. Explain the exact human action needed.

## Context Overload

The agent needs too much history.

Expected behavior:

1. Read latest compressed context.
2. Read only recent loop records.
3. Summarize necessary facts.
4. If safe compression is impossible, stop with `Blocked`.

## Completion

The agent believes the work is complete.

Expected behavior:

1. Compare against `Docs/ACCEPTANCE.md`.
2. Confirm non-goals were preserved.
3. Require automatic verification and functional verification.
4. Use `Done`, `Done with Risk`, or `Blocked`.
5. Write evaluation and next action.
