# AI Engineering Expert 1.1.0 ClawHub And Qoder Publication

Source directory:

```text
plugins/ai-engineering-expert
```

The Plugin is an additional distribution format. Do not merge, hide, or delete either standalone Skill listing.

Plugin 是额外的一键安装形式。不要合并、隐藏或删除两个独立 Skill listing。

## ClawHub Source

ClawHub publishes this `bundle-plugin` from the source directory or its committed GitHub location:

```text
plugins/ai-engineering-expert
```

The Qoder ZIP is an installable Qoder Expert Kit and a portable source archive. It is not the direct input to `clawhub package publish`. Do not use `clawhub package pack`; that command creates a ClawPack `.tgz` for external code plugins, while bundle Plugins use extracted-file publication.

## Validate And Dry Run

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

Expected identity:

```text
Name: @englandtong/ai-engineering-expert
Display name: AI Engineering Expert
Family: bundle-plugin
Version: 1.1.0
Categories: context, tools
Topics: ai-coding, autonomous-agents, project-governance, context-management, quality-assurance
```

The Plugin category vocabulary is not the standalone Skill vocabulary. `context` and `tools` are current Plugin categories; `development`, `automation`, and `agents` belong to Skill catalog metadata.

## Qoder Installation

Upload `ai-engineering-expert-v1.1.0-qoder.zip` as an Expert Kit. Confirm these qualified Skills and the expert role are visible:

```text
ai-engineering-expert:cms-project-governance
ai-engineering-expert:agent-loop-engineering
ai-engineering-expert
```

## Live Publication

Do not publish without explicit authorization and an authenticated ClawHub session. Do not store credentials in the repository. Commit and push the exact release first so ClawHub source provenance does not point at an older commit. Remove `--dry-run`, add `--wait`, and publish only after authorization.

没有明确授权和有效 ClawHub 登录状态时不要正式发布。不要把凭证存入仓库；只有正式发布获批后才移除 `--dry-run`。
