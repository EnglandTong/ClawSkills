# CMS Project Governance 2.1.0 ClawHub Listing

Use these values to update the existing listing. The local Skill name and folder are `cms-project-governance`, but the current canonical ClawHub slug is `coding-management-system`.

请用以下资料更新现有 listing。本地 Skill 名称和目录为 `cms-project-governance`，但当前 ClawHub canonical slug 是 `coding-management-system`。

## Identity

| Field | Value |
| --- | --- |
| Content type | `Skill` |
| Owner / Publisher | `englandtong` |
| Local Skill name | `cms-project-governance` |
| Canonical ClawHub slug | `coding-management-system` |
| Scoped canonical identity | `@englandtong/coding-management-system` |
| Existing alias | `@englandtong/cms-project-governance` resolves to the canonical listing |
| Display name | `CMS Project Governance` |
| Version | `2.1.0` |
| Release tag | `latest` |
| License | `MIT-0` (required for all ClawHub Skills) |
| Local source | `skills/cms-project-governance` |
| Current public version | `2.0.0` |
| Public page | `https://clawhub.ai/englandtong/skills/coding-management-system` |
| Icon | Leave unchanged/empty unless intentionally adding one |

Do not publish this update as a new `cms-project-governance` row. Doing so may split download history and create two live governance listings.

### Optional Canonical Rename

The safest update is to retain `coding-management-system` for 2.1.0. If the Owner explicitly requires the public canonical URL to match the local Skill name, ClawHub supports a live rename that keeps the old slug as a redirect:

```powershell
npx.cmd --yes clawhub@latest skill rename `
  @englandtong/coding-management-system `
  cms-project-governance
```

The rename command has no dry-run option. Run it only while authenticated and authorized, verify both old and new URLs, and then publish 2.1.0 with `--slug cms-project-governance`. Never publish both slug variants as separate Skills.

## Short Summary

```text
Turns changing goals and legacy project records into compact, conflict-checked delivery with aligned scope and QA control.
```

中文参考：

```text
把变化中的目标和旧项目记录整理为精简、经过冲突检查、范围对齐且受 QA 控制的交付状态。
```

## Full Description

Use this only if the upload form provides a separate long-description field. ClawHub otherwise reads the full Skill content from `SKILL.md`.

```text
CMS Project Governance is the control plane for vague or changing goals and legacy AI-development records. It discovers intent, sizes work, selects Lite/Standard/Full governance, bootstraps one conflict-checked Active Packet, separates Runtime/Contract/Governance/Artifact evidence, and triggers alignment or rebaseline when direction changes. It reduces document and token overhead while preserving Owner, Controller, Developer, Stage Reviewer, and independent QA authority.
```

中文参考：

```text
CMS Project Governance 是模糊或变化目标及旧 AI 开发记录的控制层。它分析意图、评估工作大小、选择 Lite/Standard/Full 治理级别、建立一个经过冲突检查的 Active Packet，区分 Runtime/Contract/Governance/Artifact 证据，并在方向变化时触发对齐或重基线。它在保留 Owner、Controller、Developer、Stage Reviewer 和独立 QA 权限边界的同时，降低文档与 Token 负担。
```

## Changelog

```text
Adds read-only Legacy Bootstrap, conflict-safe Active Packet drafting, delivery-class evidence boundaries, risk and alignment triggers, independent QA controls, and low-token governance for large legacy Docs trees.
```

中文参考：

```text
加入只读 Legacy Bootstrap、冲突时零写入的 Active Packet 草拟、交付类别证据边界、风险与目标对齐触发器、独立 QA 控制，以及面向大型旧 Docs 的低 Token 治理。
```

## Catalog Metadata

Categories, maximum three:

```text
agents, productivity, development
```

Topics, maximum five:

```text
project-governance, requirements-analysis, goal-alignment, qa-acceptance, token-efficiency
```

Merge listing:

```text
Leave empty. Specifically do not select Agent Loop Engineering (agent-loop-engineering).
```

Governance and execution are separate capabilities. Merging would hide this listing from search and browse.

## Requirements And Permissions

```text
No API key, account login, MCP server, external service, hook, or bundled executable is required.
Node.js 18+ is required only when calling the optional bootstrap and validation scripts.
Legacy Bootstrap is read-only by default and writes only with --write when current authority is coherent.
Conflicting routes, decisions, or authorization produce zero writes and one consolidated Owner request.
```

## Upload Artifact

Portable ZIP:

```text
release/ClawHub-v2.1/cms-project-governance-v2.1.0.zip
```

SHA256:

```text
8A99817600A717B771BA0AEF5B0DF94C65E8841F6DB1F27F8F197581927A8321
```

Current ClawHub CLI publishes from the Skill folder. Use the ZIP only when a dashboard explicitly accepts an archive.

## Validate And Preview

Run from the repository root:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" `
  ".\skills\cms-project-governance"

npx.cmd --yes clawhub@latest skill publish ".\skills\cms-project-governance" `
  --slug coding-management-system `
  --name "CMS Project Governance" `
  --owner englandtong `
  --version 2.1.0 `
  --changelog "Adds read-only Legacy Bootstrap, conflict-safe Active Packet drafting, delivery-class evidence boundaries, risk and alignment triggers, independent QA controls, and low-token governance for large legacy Docs trees." `
  --tags latest `
  --categories agents,productivity,development `
  --topics project-governance,requirements-analysis,goal-alignment,qa-acceptance,token-efficiency `
  --dry-run `
  --json
```

Dry-run evidence on 2026-08-13: `would-publish`, canonical slug `coding-management-system`, latest `2.0.0`, target `2.1.0`, 24 files.

Before an authorized live release, commit and push the exact source. Remove `--dry-run` only after authentication. Add source provenance using repository `EnglandTong/ClawSkills`, the exact release commit, ref/tag, and `skills/cms-project-governance`; never point 2.1.0 at an older commit.
