# ClawSkills

Practical [AI agent Skills](https://agentskills.io) for project work: governance, coding loops, research, and session memory.

**What.** Six installable Skills. An agent reads `SKILL.md` and follows the process. They work in Claude Code, Cursor, and 35+ other products that speak the open Skill format — no per-platform rewrite.

**Who.** England Tong. I coded in university and never became a full-time engineer. Most of my working years were on factory floors and in quality control (品管): gates, evidence, acceptance, stop-loss. That is the habit these Skills borrow.

**Why.** Agents are good at moving. They are less good at stopping when the evidence is thin, the scope has drifted, or someone is about to rubber-stamp their own work. Shop-floor QC already solved that class of problem. These Skills apply the same discipline to agent-run projects.

## Skills

| Skill | Version | Description |
| --- | --- | --- |
| `agent-loop-engineering` | 2.2.0 | Run an already-authorized coding goal in loops: keep state, fix what breaks, show real evidence, and stop before the same agent signs final acceptance. |
| `cms-project-governance` | 2.2.1 | Keep a drifting or half-finished project under control: one current delivery state, a right-sized scope, and independent QA acceptance. |
| `web-search-rules` | 4.1.0 | Search the web and save findings with a source URL, date, and quote on every claim. |
| `ai-workflow-os` | 2.1.0 | Pick the right Skill for a mixed request — lifecycle, governance, coding, memory, research — without creating a second source of truth. |
| `project-lifecycle-navigator` | 2.1.1 | Audit a project you are unsure about and get a go / narrow / pivot / archive / stop recommendation. Read-only: it does not write code or change governance state. |
| `daily-workflow` | 4.1.0 | Say 开工啦 or 收工啦 and get a resumable project note, so tomorrow you or another AI can pick up without re-reading everything. |

Versions in this table match each Skill's `SKILL.md`, `_meta.json`, and (where present) `skill.json`. History lives in [`CHANGELOG.md`](CHANGELOG.md).

## Recommended Entry

Use `cms-project-governance` when a goal is vague or changing, old project records conflict, work needs sizing or alignment, or independent acceptance is required. Use `agent-loop-engineering` once the outcome, scope, acceptance, and authority are coherent.

```text
cms-project-governance 2.2.1
  -> compact ACTIVE_PACKET (contract_version 2.0)
  -> agent-loop-engineering 2.2.0
  -> Ready for Independent Acceptance
  -> another agent, task, or human QA
```

Both Skills remain independently installable. Do not merge either ClawHub listing into the other.

For a combined workflow request, use `ai-workflow-os` as a router only. It delegates lifecycle advisory to `project-lifecycle-navigator`, session memory to `daily-workflow`, web research to `web-search-rules`, formal governance to `cms-project-governance`, and authorized coding to `agent-loop-engineering`. Each specialist stays independently installable and owns its own state.

## Install Anywhere

`SKILL.md` is an open standard ([agentskills.io](https://agentskills.io)) read by 35+ agent products, including Claude Code, ChatGPT, Codex CLI, VS Code, GitHub Copilot, Gemini CLI, Cursor, Trae, and Windsurf.

```bash
# from this repository (canonical source)
npx skills add EnglandTong/ClawSkills

# from ClawHub (one listing at a time)
clawhub install englandtong/daily-workflow
```

The ClawHub slug for `cms-project-governance` is `coding-management-system` (historical name; do not rename). Other Skills use the directory name as the slug.

Install one Skill, not all six. Most tools only need the one matching the job:

| If you want | Install |
| --- | --- |
| Resumable session memory and handoff | `daily-workflow` |
| Web research saved with sources and dates | `web-search-rules` |
| Decide whether to continue, cut, or archive a project | `project-lifecycle-navigator` |
| Non-technical goal discovery, sizing, and QA acceptance | `cms-project-governance` |
| Autonomous coding loops under a clear authority boundary | `agent-loop-engineering` |
| One router across all of the above | `ai-workflow-os` |

**One rule.** This GitHub repository is the canonical source; ClawHub and every cross-platform index are publish targets. Change order is always local, then `CHANGELOG.md`, then commit and push, then refresh the indexes. Never write a platform-specific content variant.

## What the coding Skills actually enforce

These are current rules, not a frozen 2.1 release note. See `CHANGELOG.md` for the dated history.

- `Controller -> Developer -> QC` prompts map into the loop. QC means Stage Reviewer inside a single-agent loop — not final sign-off.
- Standard and Full execution cannot self-sign final acceptance.
- Legacy Bootstrap indexes `Docs/docs`, reads selected current authority only, and writes nothing on conflict.
- Compact context defaults to the Packet, current Work Order, affected source/tests, verification configuration, and last three Loop records.
- Old JSONL gaps are aggregated and detailed findings are capped at 20 unless `--strict-history` is requested.
- Runtime, Contract, Governance, Artifact, and Mixed delivery claims use distinct evidence rules. A passing unit test is not proof that the flow works.
- Real paths are checked before project writes, so `..`, symlink, or junction escapes are rejected.

## Local Commands

Same `node` invocations on bash and PowerShell:

```bash
node skills/agent-loop-engineering/scripts/bootstrap-active-packet.mjs --workspace <project> --language zh-CN --json
node skills/agent-loop-engineering/scripts/validate-loop-state.mjs --workspace <project> --json --summary --max-findings 20
node skills/agent-loop-engineering/scripts/test-state-tools.mjs
```

```powershell
node skills/agent-loop-engineering/scripts/bootstrap-active-packet.mjs --workspace <project> --language zh-CN --json
node skills/agent-loop-engineering/scripts/validate-loop-state.mjs --workspace <project> --json --summary --max-findings 20
node skills/agent-loop-engineering/scripts/test-state-tools.mjs
```

Bootstrap is read-only unless `--write` is supplied and current authority is conflict-free.

Run before every release:

```bash
bash scripts/preflight.sh          # version sync, bundled copies, clean scan, frontmatter, quickstarts
bash scripts/publish-clawhub.sh    # dry run by default; add --yes to publish
```

`preflight.sh` exits non-zero on any failure. `publish-clawhub.sh` always passes `--tags` and `--topics` explicitly, because the ClawHub CLI defaults to `latest` and silently replaces the whole tag history when they are omitted.

## Bundle Plugin

`plugins/ai-engineering-expert` version **1.1.3** bundles `cms-project-governance` 2.2.1 and `agent-loop-engineering` 2.2.0 as a ClawHub `bundle-plugin` and Qoder Expert Kit. It includes OpenClaw, Claude, and Qoder manifests plus bilingual routing instructions.

The bundled copies under `plugins/ai-engineering-expert/skills/` must stay byte-identical to `skills/`. After any Skill change, re-copy and verify with `diff -rq`. A matching version number with divergent content breaks the release rule.

The Plugin is an extra one-install distribution format. Keep both standalone Skill listings live and searchable.

Release zips are not checked into this repository. Publish the ClawHub `bundle-plugin` from `plugins/ai-engineering-expert` or its exact committed GitHub source. A Qoder ZIP, if you build one, is not a ClawPack upload.

## Repository Layout

```text
plugins/
  ai-engineering-expert/
skills/
  agent-loop-engineering/
  cms-project-governance/
  ai-workflow-os/
  daily-workflow/
  project-lifecycle-navigator/
  web-search-rules/
```

## License

Released under the MIT License. See [LICENSE](LICENSE).
