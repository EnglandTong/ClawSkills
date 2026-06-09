# Loop State Protocol

Use project-local `Docs/` as the durable state source. Do not use global memory as the primary project state.

## Files

### `Docs/TARGET.md`

Store the stable goal contract:

```markdown
# Project Target

## User Goal

## Success Criteria
- [ ]

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

Store the current completion contract:

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
- Target:
- Decisions:
- Completed:
- Pending:
- Blockers:
- Files touched:
- Commands/tests:
- Immediate next action:
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
runner: generic
max_loops: 5
max_consecutive_failures: 2
max_runtime_minutes: 60
max_context_files_per_loop: 8
max_recent_loop_records: 5
require_double_evidence_for_done: true
allow_project_dependency_install: true
allow_project_config_changes: true
allow_system_install: false
allow_secret_access: false
allow_production_data_access: false
allow_destructive_changes: false
```

### `Docs/STOP_RULES.md`

Store project-specific stop rules and overrides. Project-specific rules may be stricter than the skill defaults, but not looser unless the user explicitly approves.

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

## Write Rules

- Append to `LOOP_RUNS.jsonl` and `EVALUATION.md`.
- Preserve unresolved blockers in `PENDING.md`.
- Keep only the current continuation path in `NEXT_ACTIONS.md`.
- Never store secrets, full private documents, large logs, or full chat transcripts.
