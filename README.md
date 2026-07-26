# Clawhub Skills

This repository contains public AI workflow skills by England Tong, including skills originally published on Clawhub.

## Skills

| Skill | Version | Description |
| --- | --- | --- |
| `agent-loop-engineering` | 2.0.0 | Execution-plane skill for authorized AI coding work with a versioned Active Packet, ten-stage timeboxes, bounded loops, automatic and functional evidence, failure budgets, context control, safe stop gates, and resumable handoffs. |
| `cms-project-governance` | 2.0.0 | Human-facing control-plane skill that turns vague ideas into clear outcomes, sizes work, selects Lite/Standard/Full governance, dispatches delivery, checks direction, and separates Developer completion from QA acceptance. |
| `web-search-rules` | 3.0.0 | Rules and operating guidance for evidence-backed web search workflows. |
| `ai-workflow-os` | 1.0.0 | A workflow operating system for AI-assisted projects, research, and handoffs. |
| `project-lifecycle-navigator` | 1.0.0 | Project lifecycle prompts and guidance for intake, realignment, and code-review upgrades. |
| `daily-workflow` | 3.0.0 | Daily workflow and project-local handoff guidance for AI coding work. |

## Recommended Entry

Use `cms-project-governance` when the goal is vague, needs planning, or requires QA and direction control. Use `agent-loop-engineering` once the target and acceptance criteria are authorized. The two skills share the `ACTIVE_PACKET` contract version 2.0 but remain independently usable:

```text
cms-project-governance
  -> ACTIVE_PACKET 2.0
  -> agent-loop-engineering

agent-loop-engineering
  -> project-lifecycle-navigator
  -> ai-workflow-os
  -> daily-workflow
  -> web-search-rules
```

Do not load every skill on every loop. Version 2.0 defaults to a minimal Active Packet plus append-only loop evidence, expands documentation only when risk requires it, and treats stages as timeboxed checkpoints rather than Milestones or files.

Both v2 skills include:

- `SKILL.md` as the English ClawHub entry;
- `SKILL.zh-CN.md` as the complete Chinese operating guide;
- matching `references/en/` and `references/zh-CN/` sets;
- English and Chinese copy-ready templates;
- English machine keys and state enums for cross-language interoperability.

## Bundle Plugin

`plugins/ai-engineering-expert` packages both v2 Skills as one no-code ClawHub `bundle-plugin` and Qoder Expert Kit. It adds a bilingual expert role that routes vague or governance-heavy work to `cms-project-governance` and authorized implementation work to `agent-loop-engineering`.

The Plugin is an additional distribution format. Keep both standalone Skill listings live so users can install either capability independently.

Release files:

- `release/AI-Engineering-Expert-v1.0.0/ai-engineering-expert-v1.0.0-qoder.zip`
- `release/AI-Engineering-Expert-v1.0.0/PUBLISH.md`
- `release/AI-Engineering-Expert-v1.0.0/SHA256SUMS.txt`

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

Each skill keeps its original Clawhub package structure, including `SKILL.md`, metadata, agent configuration, and supporting references or templates when present.

## License

Released under the MIT License. See [LICENSE](LICENSE).
