# Clawhub Skills

This repository contains public AI workflow skills by England Tong, including skills originally published on Clawhub.

## Skills

| Skill | Version | Description |
| --- | --- | --- |
| `agent-loop-engineering` | 1.0.0 | Top-level loop controller for long-running AI coding work with persistent `Docs/` state, stop gates, completion gates, runner adapters, and context budgeting. |
| `web-search-rules` | 3.0.0 | Rules and operating guidance for evidence-backed web search workflows. |
| `ai-workflow-os` | 1.0.0 | A workflow operating system for AI-assisted projects, research, and handoffs. |
| `project-lifecycle-navigator` | 1.0.0 | Project lifecycle prompts and guidance for intake, realignment, and code-review upgrades. |
| `daily-workflow` | 3.0.0 | Daily workflow and project-local handoff guidance for AI coding work. |

## Recommended Entry

Use `agent-loop-engineering` as the entry skill for AI coding work. Use `ai-workflow-os` for non-coding research, source governance, and workflow coordination. `agent-loop-engineering` routes to the other skills only when needed:

```text
agent-loop-engineering
  -> project-lifecycle-navigator
  -> ai-workflow-os
  -> daily-workflow
  -> web-search-rules
```

Do not load every skill on every loop. `agent-loop-engineering` uses progressive reading and project-local `Docs/` files to keep context small and resumable.

## Repository Layout

```text
skills/
  agent-loop-engineering/
  ai-workflow-os/
  daily-workflow/
  project-lifecycle-navigator/
  web-search-rules/
```

Each skill keeps its original Clawhub package structure, including `SKILL.md`, metadata, agent configuration, and supporting references or templates when present.

## License

Released under the MIT License. See [LICENSE](LICENSE).
