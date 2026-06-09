# Loop State Protocol

Use project-local `Docs/` as the durable state source. Do not use global memory as the primary project state.

## Files

### `Docs/TARGET.md`

Store the stable goal contract. `TARGET.md` is the source of truth for what the project is trying to do and what is out of scope. Keep success criteria high-level here; put executable checks in `ACCEPTANCE.md`.

```markdown
# Project Target

## User Goal

## Success Criteria
- [High-level outcome, not a test command]

## Non-Goals
- [ ]

## Acceptance Evidence
- Automatic verification:
- Functional verification:
- Review/documentation evidence:

## Failure Examples
- [What would prove this is not complete]

## Last Confirmed
YYYY-MM-DD
```

### `Docs/ACCEPTANCE.md`

Store the executable completion contract. `ACCEPTANCE.md` is the source of truth for the completion gate and must be derived from `TARGET.md`.

```markdown
# Acceptance Contract

## Must Pass
- [ ] Requirement:
  Evidence required:
  Current evidence:

## Should Pass
- [ ] Requirement:
  Evidence required:
  Current evidence:

## Manual Confirmation Needed
- [ ] Item:
  Reason:

## Known Exclusions
- Item:
  Reason:
```

### `Docs/STATUS.md`

Keep only the latest working state and recent update history:

```markdown
# Project Status

## Current State

## Latest Verification
- Command/result:
- Functional check:
- Evidence path:

## Risks

## Compressed Context
- Target: 1-2 lines
- Decisions: up to 5 bullets
- Completed: up to 5 bullets
- Pending: up to 5 bullets
- Blockers: up to 5 bullets
- Files touched: paths only
- Commands/tests: command + result + short error summary
- Evidence paths: log, screenshot, fixture, or report path
- Immediate next action: exactly one action
```

### `Docs/PENDING.md`

Keep the active queue:

```markdown
# Pending Work

## Immediate
- [ ]

## Later
- [ ]

## Blockers and Decisions
- [ ]
```

### `Docs/NEXT_ACTIONS.md`

Keep one continuation path:

```markdown
# Next Actions

## Immediate Next Action
1.

## Stop/Resume Notes
- Stop state:
- Resume command or entry point:
- Needed human input:
```

### `Docs/LOOP_CONFIG.md`

Store loop policy:

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
allow_parallel_tasks: false
verification_commands:
  test: null
  typecheck: null
  build: null
  lint: null
  functional: null
allow_project_dependency_install: true
allow_project_config_changes: true
allow_system_install: false
allow_secret_access: false
allow_production_data_access: false
allow_destructive_changes: false
```

`allow_*` fields may make defaults stricter, but they must not loosen the hard stop rules in `environment-escalation.md` unless the user explicitly approves that run.

`max_consecutive_failures` counts consecutive loops where core verification fails or no measurable progress is made. It does not require the exact same command to fail each time.

### `Docs/STOP_RULES.md`

Store project-specific stop rules and overrides. Project-specific rules may be stricter than the skill defaults, but not looser unless the user explicitly approves.

```markdown
# Stop Rules

## Hard Stops
- Rule:
  Reason:
  Human decision needed:

## Budget Stops
- max_loops:
- max_consecutive_failures:
- max_runtime_minutes:

## Project-Specific Stops
- Rule:
  Severity: hard / soft
  Reason:

## Overrides
- Override:
  Approved by:
  Expiration:
```

### `Docs/EVALUATION.md`

Append each evaluation:

```markdown
## YYYY-MM-DD HH:mm Loop Evaluation

- State: Continue / Done / Done with Risk / Blocked
- Target alignment:
- Success criteria status:
- Automatic verification:
- Functional verification:
- Risks:
- Stop rule triggered:
- Next action:
```

### `Docs/LOOP_RUNS.jsonl`

Append one JSON object per loop. Keep it concise:

```json
{"run_id":"2026-06-09T17:30:00+08:00","state":"continue","goal_snapshot":"...","action":"...","verification":["typecheck passed"],"risks":[],"next_action":"..."}
```

Archive older records when record count exceeds `max_recent_loop_records` plus the number needed for the current investigation. Move older records to `Docs/archive/LOOP_RUNS_YYYY-MM.jsonl`.

### `Docs/HANDOFF.md`

Create only when a standalone handoff is needed:

```markdown
# Handoff

## Reason

## Current State

## Target and Acceptance Summary

## Key Decisions

## Completed Work

## Pending Work

## Blockers and Risks

## Verification Evidence

## Files Touched

## Next Agent Instructions
```

## Conflict Resolution

Use this priority when files disagree:

```text
TARGET.md -> ACCEPTANCE.md -> STATUS.md -> PENDING.md -> NEXT_ACTIONS.md -> LOOP_RUNS.jsonl
```

If `TARGET.md` and `ACCEPTANCE.md` disagree, stop before coding and reconcile them. If lower-priority files disagree, update them to match the higher-priority file and record the correction in `EVALUATION.md`.

## Write Rules

- Append to `LOOP_RUNS.jsonl` and `EVALUATION.md`.
- Preserve unresolved blockers in `PENDING.md`.
- Keep only the current continuation path in `NEXT_ACTIONS.md`.
- Never store secrets, full private documents, large logs, or full chat transcripts.
- Prefer writing state files in this order at loop end: `EVALUATION.md`, `PENDING.md`, `NEXT_ACTIONS.md`, `LOOP_RUNS.jsonl`.
- If a previous write was interrupted, recover by reading `TARGET.md` and `ACCEPTANCE.md` first, then reconciling lower-priority files.
