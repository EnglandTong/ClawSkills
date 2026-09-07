# ClawHub Skills

This repository contains public AI workflow Skills and Plugins by England Tong.

## Skills

| Skill | Version | Description |
| --- | --- | --- |
| `agent-loop-engineering` | 2.2.0 | Execution plane for low-context Bounded Autopilot, proactive failure repair, focused and functional evidence, real-path write boundaries, stage review, and independent final acceptance. |
| `cms-project-governance` | 2.2.0 | Control plane for non-technical goal guidance, compact legacy CMS bootstrap, sizing, alignment, delivery-class evidence, anti-involution controls, and independent QA governance. |
| `web-search-rules` | 4.1.0 | Evidence-backed web research, claim verification, untrusted-metadata handling, single-source cross-checking, source rules, staging, archive safeguards, and audit. |
| `ai-workflow-os` | 2.1.0 | Router across lifecycle, governance, coding, memory, research, and synthesis without competing state, with a subtraction-first scope guard. |
| `project-lifecycle-navigator` | 2.1.0 | Lifecycle advisory for intake, MVP scoping, startup gates, realignment, whole-system audit, delivery review, stop-loss, and Owner rebaseline. |
| `daily-workflow` | 4.1.0 | Evidence-backed project orientation, checkpoint, wrap-up, memory-bloat control, and self-contained handoff memory. |

Versions above are the authoritative source. Each Skill's `SKILL.md`, `_meta.json`, and (where present) `skill.json` carry the same number; see `CHANGELOG.md` for the change record.

## Recommended Entry

Use `cms-project-governance` when a goal is vague or changing, old project records conflict, work needs sizing or alignment, or independent acceptance is required. Use `agent-loop-engineering` once outcome, scope, acceptance, and authority are coherent.

```text
cms-project-governance 2.1
  -> compact ACTIVE_PACKET (contract_version 2.0)
  -> agent-loop-engineering 2.1
  -> Ready for Independent Acceptance
  -> another agent, task, or human QA
```

Both Skills remain independently installable. Do not merge either ClawHub listing into the other.

For combined workflow requests, use `ai-workflow-os` as a router only. It delegates lifecycle advisory to `project-lifecycle-navigator`, session memory to `daily-workflow`, web research intake to `web-search-rules`, formal governance to `cms-project-governance`, and authorized coding execution to `agent-loop-engineering`. Each specialist remains independently installable and authoritative for its state surface.

## Install Anywhere

`SKILL.md` is an open standard (agentskills.io) read by 35+ agent products, including Claude Code, ChatGPT, Codex CLI, VS Code, GitHub Copilot, Gemini CLI, Cursor, Trae, and Windsurf. These Skills need no per-platform variant.

```bash
# from this repository (canonical source)
npx skills add EnglandTong/ClawSkills

# from ClawHub
clawhub install englandtong/daily-workflow
```

Install one Skill, not all six. Most tools only need the one matching the job:

| If you want | Install |
| --- | --- |
| Resumable session memory and handoff | `daily-workflow` |
| Web research saved with sources and dates | `web-search-rules` |
| Decide whether to continue, cut, or archive a project | `project-lifecycle-navigator` |
| Non-technical goal discovery, sizing, and QA acceptance | `cms-project-governance` |
| Autonomous coding loops under bounded authority | `agent-loop-engineering` |
| One router across all of the above | `ai-workflow-os` |

**One rule.** This GitHub repository is the canonical source; ClawHub and every cross-platform index are publish targets. The change order is always local, then `CHANGELOG.md`, then commit and push, then refresh the indexes. Never write a platform-specific content variant.

## Version 2.1

- `Controller -> Developer -> QC` prompts route directly into Bounded Autopilot; QC means Stage Reviewer inside a single-agent loop.
- Standard and Full execution cannot self-sign final acceptance.
- Legacy Bootstrap indexes `Docs/docs`, reads selected current authority only, and writes nothing on conflict.
- Compact context defaults to the Packet, current Work Order, affected source/tests, verification configuration, and last three Loop records.
- Old JSONL gaps are aggregated and detailed findings are capped at 20 unless `--strict-history` is requested.
- Runtime, Contract, Governance, Artifact, and Mixed delivery claims use distinct evidence rules.
- Real paths are checked before project writes to reject `..`, symlink, or junction escapes.

## Local Commands

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

`plugins/ai-engineering-expert` version 1.1.2 bundles both Skills as a ClawHub `bundle-plugin` and Qoder Expert Kit. It includes OpenClaw, Claude, and Qoder manifests plus bilingual routing instructions.

The bundled copies under `plugins/ai-engineering-expert/skills/` must stay byte-identical to `skills/`. After any Skill change, re-copy and verify with `diff -rq`; a version number that matches while the content diverges breaks the release rule.

The Plugin is an additional one-install distribution format. Keep both standalone Skill listings live and searchable.

Release artifacts:

- `release/ClawHub-v2.1/agent-loop-engineering-v2.1.0.zip`
- `release/ClawHub-v2.1/cms-project-governance-v2.1.0.zip`
- `release/ClawHub-v2.1/AGENT_LOOP_ENGINEERING_LISTING.md`
- `release/ClawHub-v2.1/CMS_PROJECT_GOVERNANCE_LISTING.md`
- `release/AI-Engineering-Expert-v1.1.0/ai-engineering-expert-v1.1.0-qoder.zip`
- `release/AI-Engineering-Expert-v1.1.0/CLAWHUB_LISTING.md`

Publish the ClawHub `bundle-plugin` from `plugins/ai-engineering-expert` or its exact committed GitHub source. The Qoder ZIP is not a ClawPack upload.

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
