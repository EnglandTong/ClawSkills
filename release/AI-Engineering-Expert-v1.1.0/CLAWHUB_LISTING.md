# AI Engineering Expert 1.1.0 ClawHub Listing

These values are ready to paste into ClawHub. The package is an additional one-install Plugin; keep the two standalone Skill listings public and separate.

以下内容可直接填写到 ClawHub。Plugin 是额外的一键安装入口；两个独立 Skill listing 继续保持公开和独立。

## Required Identity

| Field | Value |
| --- | --- |
| Package family | `bundle-plugin` |
| Owner / Publisher | `englandtong` |
| Package name | `@englandtong/ai-engineering-expert` |
| Display name | `AI Engineering Expert` |
| Runtime / Plugin ID | `ai-engineering-expert` |
| Version | `1.1.0` |
| Release tag | `latest` |
| Channel | `community` |
| Visibility | `public` |
| License | `MIT` |
| Author | `England Tong` |
| Source path | `plugins/ai-engineering-expert` |
| Bundle format | `claude` |
| Host targets | Leave empty and use manifest detection |
| Icon | Leave empty until a stable HTTPS icon URL exists |

## Short Summary

```text
Bilingual AI engineering plugin for compact CMS bootstrap, bounded-autonomous coding loops, proactive repair, alignment, and independent QA.
```

中文参考：

```text
面向中英文项目的 AI 工程 Plugin，提供精简 CMS 引导、有界自主开发、主动返修、目标对齐和独立 QA。
```

## Full Description

```text
AI Engineering Expert combines Agent Loop Engineering 2.1.0 and CMS Project Governance 2.1.0 in one bilingual Plugin. It turns an authorized project goal into bounded Controller -> Developer -> Stage Reviewer -> Repair loops, bootstraps compact active state from legacy Docs, prevents scope and acceptance drift, and keeps Standard/Full final acceptance independent. Focused tests, aggregated history diagnostics, real-path write boundaries, and Compact context controls reduce repeated reads, full-log replay, and unnecessary full regressions.
```

中文参考：

```text
AI Engineering Expert 把 Agent Loop Engineering 2.1.0 与 CMS Project Governance 2.1.0 合并为一个中英文 Plugin。它把已授权目标转为有界的 Controller -> Developer -> Stage Reviewer -> Repair 循环，从旧 Docs 建立精简活动状态，控制范围和验收偏移，并保持 Standard/Full 独立终验。聚焦测试、历史诊断聚合、真实路径写入边界和 Compact 上下文控制可减少重复读取、完整日志回灌及无必要的全量回归。
```

## Changelog

```text
Adds bounded-autonomous execution, compact legacy CMS bootstrap, proactive repair, layered acceptance, and low-context validation.
```

中文参考：

```text
加入有界自主执行、旧项目精简 CMS 引导、主动返修、分层验收和低上下文校验。
```

## Catalog Metadata

Categories, using the Plugin catalog vocabulary:

```text
context, tools
```

Topics:

```text
ai-coding, autonomous-agents, project-governance, context-management, quality-assurance
```

Do not use the standalone Skill categories `development`, `automation`, or `agents` for this Plugin listing. ClawHub uses a different category vocabulary for Plugins.

## Links

| Field | Value |
| --- | --- |
| Homepage | `https://github.com/EnglandTong/ClawSkills` |
| Repository | `https://github.com/EnglandTong/ClawSkills.git` |
| Repository subpath | `plugins/ai-engineering-expert` |

Use the exact release commit or tag only after the current files have been committed and pushed. Do not associate a live release with an older commit.

## Capabilities And Requirements

```text
Includes Agent Loop Engineering 2.1.0 and CMS Project Governance 2.1.0.
Provides bilingual routing, bounded-autonomous coding loops, legacy CMS bootstrap,
goal alignment, proactive repair, compact context control, and independent QA gates.
No MCP server, API key, external service, hook, runtime service, or bundled executable is required.
Node.js 18+ is needed only when running the optional bootstrap and validation scripts.
```

## Merge Listing

Not applicable to the Plugin. Do not merge or hide either standalone Skill listing:

```text
agent-loop-engineering
cms-project-governance
```

## Publication Source

Current ClawHub CLI publication input:

```text
plugins/ai-engineering-expert
```

The Qoder ZIP is not direct `clawhub package publish` input. Extracting it recreates the Plugin source tree, but normal release publication should use the repository folder or the exact committed GitHub source. `clawhub package pack` is for external code-plugin ClawPack `.tgz` artifacts and is not used for this bundle Plugin.

## Validate And Preview

Run from the repository root:

```powershell
npx.cmd --yes clawhub@latest package validate ".\plugins\ai-engineering-expert" `
  --out ".\work\clawhub-plugin-validation-1.1.0"

npx.cmd --yes clawhub@latest package publish ".\plugins\ai-engineering-expert" `
  --family bundle-plugin `
  --name "@englandtong/ai-engineering-expert" `
  --display-name "AI Engineering Expert" `
  --owner englandtong `
  --version 1.1.0 `
  --changelog "Adds bounded-autonomous execution, compact legacy CMS bootstrap, proactive repair, layered acceptance, and low-context validation." `
  --tags latest `
  --categories context,tools `
  --topics ai-coding,autonomous-agents,project-governance,context-management,quality-assurance `
  --bundle-format claude `
  --dry-run `
  --json
```

For an authorized live release, first commit and push the exact source. Then authenticate with ClawHub, remove `--dry-run`, add `--wait`, and retain the same identity and catalog fields. Do not store the ClawHub token in this repository.
