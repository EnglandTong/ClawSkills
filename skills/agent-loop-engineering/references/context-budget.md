# Context Budget

Long-running coding agents fail when they reread too much history, but they also
fail when they receive too little authority context. Context must be treated as
a bounded work packet, not a dump of all project knowledge.

For the broader CMS / memory model, read `cms-context-memory.md`.

## Context Packet Rule

Every role should receive a Context Packet:

```yaml
context_packet:
  role: Developer | Reviewer | QA | Controller | Archivist
  work_order: one current task
  target: only relevant goal and non-goals
  acceptance: only current acceptance rows
  constraints: stop rules and allowed scope
  recent_state: compressed latest status
  evidence: latest relevant validation only
  next_action: one intended action
  exclusions: what not to do
```

Do not load full chat history, full logs, stale plans, or entire reference
folders into the packet.

## Budget Tiers

Use tiers instead of "read everything".

| Tier | Use case | Suggested size | Suggested max project files |
| --- | --- | ---: | ---: |
| Lite | small bug, single file, clear acceptance | 3k-6k tokens | 3-5 |
| Standard | normal feature or review | 6k-12k tokens | 5-8 |
| Deep | repeated failure, architecture boundary, high-risk refactor | 12k-25k tokens | 8-12 |
| Rich | exceptional incident or design review | explicit approval | case by case |

Default to Lite or Standard. Escalate only when evidence shows missing context
caused failure or risk.

## Minimum Read Set

At loop start, read only:

1. `Docs/LOOP_CONFIG.md`
2. `Docs/TARGET.md`
3. `Docs/ACCEPTANCE.md`
4. Latest compressed context from `Docs/STATUS.md`
5. Immediate and Blockers sections from `Docs/PENDING.md`
6. `Docs/NEXT_ACTIONS.md`

If `LOOP_RUNS.jsonl` is needed, read only the latest 3-5 records.

These six items count toward `max_context_files_per_loop`. Reading only a section of a file still counts as one context file. Project manifests used to discover verification commands also count. Files listed but not opened do not count.

Skill instruction files and `references/*.md` files from the skill package do not count toward the project `max_context_files_per_loop`; that budget is for workspace/project files. Still read skill references progressively and only when their decision surface is active.

## Conditional Reads

- Read `completion-gate.md` only before declaring completion or risk.
- Read `environment-escalation.md` only when a command, dependency, permission, or environment issue appears.
- Read `runner-adapters.md` only when configuring or changing a runner.
- Read `web-search-rules` only for external sources, API docs, uploaded files, or knowledge intake.
- Read lifecycle skills only when scope, MVP, or project stage is unclear.

## Memory And Retrieval

Retrieved knowledge is a hint, not authority.

Use this authority order:

```text
Current work order
-> current acceptance criteria
-> stop rules
-> current compressed status
-> retrieved project memory
-> specialist knowledge
-> personal preference
-> external general reference
```

Before adding retrieved knowledge to context:

1. Extract a query from the current work order: goal, package, feature, role,
   risk, or error class.
2. Search only relevant memory scopes.
3. Rank by current relevance and freshness.
4. Compress to 3-7 facts.
5. Attach source paths.
6. Drop facts that do not change the next action.

Do not pass search dumps, full article summaries, or raw dogfooding logs to the
coding agent.

## Context Composition Ratio

For normal coding loops, aim for:

| Context type | Target share |
| --- | ---: |
| Task authority: work order and acceptance | 30-40% |
| Current code facts | 30-40% |
| State and evidence | 10-20% |
| Rules and guardrails | 10-15% |
| External reference / general theory | 0-5% |

If history, rules, or references dominate the packet, summarize them or move
them out of the current loop.

## Compression Rules

At the end of each loop, keep:

- Current target and whether it changed.
- Decisions made.
- Completed work.
- Verification evidence.
- Open blockers.
- Files touched.
- One immediate next action.

Keep `Docs/STATUS.md` compressed context under `max_compressed_context_lines` from `Docs/LOOP_CONFIG.md`; default is 40 lines. If the summary needs more than the limit, keep only facts needed for the next loop and move supporting detail to logs or archive files.

Remove:

- Repeated exploration notes.
- Full command logs.
- Full chat transcripts.
- Old failed attempts that no longer affect the next decision.
- Duplicate summaries.

## Compressed Context Template

Use this format in `Docs/STATUS.md`:

```markdown
## Compressed Context
- Target: one sentence
- Target changed: yes/no
- Decisions: max 5 bullets
- Completed: max 5 bullets
- Verification: command + status + evidence path
- Pending: max 5 bullets
- Blockers: max 5 bullets
- Files touched: paths only
- Logs/evidence paths: paths only
- Immediate next action: exactly one action
```

Keep each bullet short. Store detailed logs under the configured `log_directory` such as `.agent/logs`, then reference the path.

## Log Storage

Do not put full logs in `Docs/`. Use `log_directory` from `Docs/LOOP_CONFIG.md`; default to `.agent/logs`. If the directory is ignored by Git, record enough summary in `STATUS.md` for the next agent to continue.

Recommended repository policy:

- Keep `.agent/logs/` out of public commits unless the project explicitly needs sanitized logs.
- Store only command name, result, key error summary, and log path in `Docs/`.
- Redact secrets, tokens, private URLs, customer data, and machine-specific paths before writing any persistent state.

## Archive Triggers

When any active `Docs/` state file grows beyond 200 lines, evaluate whether it should be archived. Move older material to `Docs/archive/<FILENAME>_YYYY-MM.md` or `.jsonl` for JSONL logs, then keep only the latest useful content plus an archive index entry in the original file.

Do not archive unresolved blockers, current acceptance evidence, current target, or the immediate next action.

## File Budget Enforcement

When a loop would exceed `max_context_files_per_loop`:

1. Keep required state files and the core manifest first.
2. Queue optional reads in `Docs/PENDING.md` instead of opening them.
3. Summarize already-read material into `Docs/STATUS.md`.
4. Continue only if the next action can be done safely from the remaining context.
5. If the agent cannot judge the target, risk, or verification without more files, stop as `Blocked` with reason `context budget exceeded`.

Default loop sizes:

| Task type | Suggested `max_loops` |
| --- | --- |
| Small bug fix | 3-5 |
| Multi-file feature | 8-10 |
| Investigation-heavy repair | 10-15 |
| More than 20 loops | Requires explicit user approval |

## Context Stop Gate

Stop with `Blocked` when:

- The agent cannot identify the current target from compressed state.
- The next action depends on missing history that cannot be recovered from files.
- The required context exceeds the configured file or token budget and cannot be summarized safely.

Before stopping, update `PENDING.md`, `NEXT_ACTIONS.md`, `EVALUATION.md`, and `LOOP_RUNS.jsonl`.
