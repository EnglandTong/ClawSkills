# ClawHub Skills

This repository contains public AI workflow Skills and Plugins by England Tong.

## Skills

| Skill | Version | Description |
| --- | --- | --- |
| `agent-loop-engineering` | 2.1.0 | Execution plane for low-context Bounded Autopilot, proactive failure repair, focused and functional evidence, real-path write boundaries, stage review, and independent final acceptance. |
| `cms-project-governance` | 2.1.0 | Control plane for non-technical goal guidance, compact legacy CMS bootstrap, sizing, alignment, delivery-class evidence, and independent QA governance. |
| `web-search-rules` | 4.0.0 | Evidence-backed web research, claim verification, source rules, staging, archive safeguards, and audit. |
| `ai-workflow-os` | 2.0.0 | Router across lifecycle, governance, coding, memory, research, and synthesis without competing state. |
| `project-lifecycle-navigator` | 2.0.0 | Lifecycle advisory for intake, realignment, whole-system audit, delivery review, and Owner rebaseline. |
| `daily-workflow` | 4.0.0 | Evidence-backed project orientation, checkpoint, wrap-up, and self-contained handoff memory. |

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

## Bundle Plugin

`plugins/ai-engineering-expert` version 1.1.0 bundles both Skills as a ClawHub `bundle-plugin` and Qoder Expert Kit. It includes OpenClaw, Claude, and Qoder manifests plus bilingual routing instructions.

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
