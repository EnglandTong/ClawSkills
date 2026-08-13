# Agent Loop Engineering 2.1.0 ClawHub Listing

Use these values to update the existing England Tong listing. Do not create an unscoped duplicate: another publisher also uses the same slug.

请用以下资料更新 England Tong 现有 listing。ClawHub 上另有其他发布者使用相同 slug，不要建立无发布者范围的重复条目。

## Identity

| Field | Value |
| --- | --- |
| Content type | `Skill` |
| Owner / Publisher | `englandtong` |
| Canonical slug | `agent-loop-engineering` |
| Scoped identity | `@englandtong/agent-loop-engineering` |
| Display name | `Agent Loop Engineering` |
| Version | `2.1.0` |
| Release tag | `latest` |
| License | `MIT-0` (required for all ClawHub Skills) |
| Local source | `skills/agent-loop-engineering` |
| Current public version | `2.0.0` |
| Public page | `https://clawhub.ai/englandtong/skills/agent-loop-engineering` |
| Icon | Keep the existing `lucide:Sparkles` unless intentionally changing it |

## Short Summary

```text
Runs low-context, bounded-autonomous coding loops with proactive repair, evidence gates, and independent final review.
```

中文参考：

```text
通过低上下文、有界自主开发、主动返修、证据门禁和独立终验，持续推进已授权的软件目标。
```

## Full Description

Use this only if the upload form provides a separate long-description field. ClawHub otherwise reads the full Skill content from `SKILL.md`.

```text
Agent Loop Engineering is the execution plane for authorized AI-assisted software delivery. It runs bounded Controller -> Developer -> Stage Reviewer -> Repair cycles, makes reversible project-local decisions proactively, diagnoses and repairs failures, and verifies real behavior with focused tests and concise evidence. Compact context, persistent Active Packet and Loop state, real-path write boundaries, and independent Standard/Full acceptance keep long autonomous work aligned without replaying full project history.
```

中文参考：

```text
Agent Loop Engineering 是已授权 AI 软件交付的执行层。它按 Controller -> Developer -> Stage Reviewer -> Repair 进行有界循环，主动处理项目内可逆决策、诊断并修复失败，并以聚焦测试和精简证据验证真实行为。Compact 上下文、持续 Active Packet/Loop 状态、真实路径写入边界，以及 Standard/Full 独立终验，可在不反复读取全部历史的情况下保持长期开发对齐。
```

## Changelog

```text
Adds Bounded Autopilot, proactive failure diagnosis and repair, stage review with independent Standard/Full acceptance, Compact context, focused-first testing, aggregated legacy diagnostics, and real-path write boundaries.
```

中文参考：

```text
加入 Bounded Autopilot、主动失败诊断与返修、阶段审查及 Standard/Full 独立终验、Compact 上下文、聚焦测试优先、旧日志聚合诊断和真实路径写入边界。
```

## Catalog Metadata

Categories, maximum three:

```text
development, automation, agents
```

Topics, maximum five:

```text
ai-coding, autonomous-agents, software-testing, context-management, execution-loops
```

Merge listing:

```text
Leave empty. Do not merge this Skill into another listing.
```

## Requirements And Permissions

```text
No API key, account login, MCP server, external service, hook, or bundled executable is required.
Node.js 18+ is required only for the optional bootstrap, state validator, and regression scripts.
Writes are limited by the active project authorization; project-root escape through path traversal,
symlink, or junction is denied when outside_write_policy is Deny.
Standard and Full work require independent final acceptance.
```

## Upload Artifact

Portable ZIP:

```text
release/ClawHub-v2.1/agent-loop-engineering-v2.1.0.zip
```

SHA256:

```text
2A5A9B50C33FE5E1A7E63A0110E18543CD2A1488AE2FDDD6B91B546948ACC449
```

Current ClawHub CLI publishes from the Skill folder. Use the ZIP only when a dashboard explicitly accepts an archive.

## Validate And Preview

Run from the repository root:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" `
  ".\skills\agent-loop-engineering"

npx.cmd --yes clawhub@latest skill publish ".\skills\agent-loop-engineering" `
  --slug agent-loop-engineering `
  --name "Agent Loop Engineering" `
  --owner englandtong `
  --version 2.1.0 `
  --changelog "Adds Bounded Autopilot, proactive failure diagnosis and repair, stage review with independent Standard/Full acceptance, Compact context, focused-first testing, aggregated legacy diagnostics, and real-path write boundaries." `
  --tags latest `
  --categories development,automation,agents `
  --topics ai-coding,autonomous-agents,software-testing,context-management,execution-loops `
  --dry-run `
  --json
```

Dry-run evidence on 2026-08-13: `would-publish`, latest `2.0.0`, target `2.1.0`, 24 files.

Before an authorized live release, commit and push the exact source. Remove `--dry-run` only after authentication. Add source provenance using repository `EnglandTong/ClawSkills`, the exact release commit, ref/tag, and `skills/agent-loop-engineering`; never point 2.1.0 at an older commit.
