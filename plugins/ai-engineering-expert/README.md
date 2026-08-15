# AI Engineering Expert

Version: 1.1.1

AI Engineering Expert is a bilingual ClawHub bundle Plugin and Qoder Expert Kit for governed, proactive AI-assisted software delivery. It packages two independently usable Skills:

- `cms-project-governance` 2.1.1: goal discovery, Legacy Bootstrap, sizing, alignment, isolated-worker authorization, rebaseline, and independent QA control.
- `agent-loop-engineering` 2.1.1: low-context Bounded Autopilot, isolated subagent delegation, focused verification, proactive repair, and layered stage review.

The expert role routes work between them without collapsing governance and execution authority.

## What Changed In 1.1

- Recognizes existing `Controller -> Developer -> QC` CMS prompts directly.
- Maps QC to Stage Reviewer and preserves independent Standard/Full acceptance.
- Bootstraps legacy `Docs/docs` state without recursively reading all history.
- Stops with zero writes on route, QA, authority, claim-class, or path conflicts.
- Aggregates legacy validator warnings and caps details at 20 by default.
- Adds context and verification-cost controls for measurable Token reduction.
- Bundles read-only bootstrap, compact validation, and regression test utilities.

## Shared Contract

Both Skills use `Docs/ACTIVE_PACKET.md` with backward-compatible `contract_version: "2.0"` plus the 2.1 fields for bounded autonomy, layered acceptance, delivery class, compact context, real-path write scope, and authority fingerprint.

New Standard/Full execution ends at `Ready for Independent Acceptance`. Another agent, task, or human owns final QA.

## Qoder

The bundle contains `.qoder-plugin/plugin.json`, `qoder.md`, `agents/ai-engineering-expert.md`, and `skills/*`. Qualified Skill names are:

```text
ai-engineering-expert:cms-project-governance
ai-engineering-expert:agent-loop-engineering
```

Qoder Expert Kits can install the release ZIP directly. Qoder CLI can install the extracted Plugin directory.

## ClawHub

This directory is the ClawHub publication unit for a no-service `bundle-plugin`. OpenClaw loads the two Skill directories through `openclaw.plugin.json`; `.claude-plugin/plugin.json` and `.qoder-plugin/plugin.json` provide compatible package discovery metadata.

ClawHub publishes a bundle Plugin from this folder or from its committed GitHub source. Do not pass the Qoder ZIP to `clawhub package publish`, and do not run `clawhub package pack`: ClawPack `.tgz` output is the code-plugin path, while bundle Plugins use extracted-file publication.

Validate and preview from the repository root:

```powershell
npx.cmd --yes clawhub@latest package validate ".\plugins\ai-engineering-expert" `
  --out ".\work\clawhub-plugin-validation-1.1.1"

npx.cmd --yes clawhub@latest package publish ".\plugins\ai-engineering-expert" `
  --family bundle-plugin `
  --name "@englandtong/ai-engineering-expert" `
  --display-name "AI Engineering Expert" `
  --owner englandtong `
  --version 1.1.1 `
  --changelog "Adds bounded-autonomous execution, compact legacy CMS bootstrap, proactive repair, layered acceptance, and low-context validation." `
  --tags latest `
  --categories context,tools `
  --topics ai-coding,autonomous-agents,project-governance,context-management,quality-assurance `
  --bundle-format claude `
  --dry-run `
  --json
```

The Plugin category vocabulary is different from the standalone Skill vocabulary. Use `context,tools` here; do not reuse `development,automation,agents` for the Plugin listing. Commit and push the release before live publication so ClawHub source provenance identifies the exact released content.

Do not merge or hide the two standalone Skill listings. The Plugin is an additional one-install distribution channel.

## Requirements And Permissions

- Node.js 18 or later for the optional local bootstrap and validator scripts.
- No MCP server, API key, external service, hook, or runtime service.
- Project reads, edits, tests, and commands remain subject to host sandbox and project permissions.
- Bootstrap is read-only unless `--write` is supplied and its state is conflict-free.

## 中文说明

AI Engineering Expert 1.1 是中英文 ClawHub Plugin 与 Qoder Expert Kit，包含两个保持独立权限的 Skill：

- `cms-project-governance` 负责需求分析、旧项目引导、分级、方向对齐、重基线和独立 QA；
- `agent-loop-engineering` 负责低上下文自主开发、聚焦验证、主动返修和阶段审查。

它可直接理解“按 CMS 规则推进，Controller 派工、Developer 开发、QC 验收并自主循环，目录外禁止修改”的调用方式。QC 在单 Agent 循环中代表阶段审查；Standard/Full 最终必须停在独立验收前。旧项目 Bootstrap 默认只读，有冲突时零写入。Plugin 不需要 MCP、API Key 或外部服务。
