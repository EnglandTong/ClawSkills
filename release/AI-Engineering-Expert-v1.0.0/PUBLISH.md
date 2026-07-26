# AI Engineering Expert 1.0.0

This release contains one ClawHub `bundle-plugin` and Qoder Expert Kit that packages:

- `cms-project-governance`
- `agent-loop-engineering`
- `ai-engineering-expert` role routing

本版本是一个 ClawHub `bundle-plugin` 和 Qoder Expert Kit，包含两个独立 Skill 和一个统一专家角色。

## Source / 源目录

```text
plugins/ai-engineering-expert
```

Do not merge or delete the two existing standalone Skill listings. The Plugin is an additional one-install distribution channel.

不要合并或删除原来的两个独立 Skill listing。Plugin 是额外的一键安装发布方式。

## Validate / 校验

Run from the repository root:

```powershell
npx.cmd --yes clawhub@latest package validate ".\plugins\ai-engineering-expert"

npx.cmd --yes clawhub@latest package publish ".\plugins\ai-engineering-expert" `
  --family bundle-plugin `
  --name "@englandtong/ai-engineering-expert" `
  --version 1.0.0 `
  --owner englandtong `
  --dry-run
```

Expected package identity:

```text
Name: @englandtong/ai-engineering-expert
Display name: AI Engineering Expert
Family: bundle-plugin
Version: 1.0.0
```

## Publish To ClawHub / 发布到 ClawHub

Log in first. Do not store the token in this repository.

先登录，不要把 Token 保存到仓库。

```powershell
npx.cmd --yes clawhub@latest login

npx.cmd --yes clawhub@latest package publish ".\plugins\ai-engineering-expert" `
  --family bundle-plugin `
  --name "@englandtong/ai-engineering-expert" `
  --version 1.0.0 `
  --owner englandtong
```

## Install In QoderWork / 安装到 QoderWork

Use the Qoder ZIP in this release directory:

```text
ai-engineering-expert-v1.0.0-qoder.zip
```

In QoderWork:

1. Open `Extensions` > `Expert Kits`.
2. Select `+ Add`.
3. Select `Upload plugin`.
4. Upload the ZIP.
5. Confirm that both bundled Skills and the `ai-engineering-expert` role are visible.

在 QoderWork 中进入“扩展 > Expert Kits”，选择“添加 > Upload plugin”，上传 ZIP，并确认两个 Skill 和专家角色都已识别。

## Qoder Skill Names / Qoder Skill 名称

```text
ai-engineering-expert:cms-project-governance
ai-engineering-expert:agent-loop-engineering
```

## Dependencies / 依赖

- No MCP server.
- No API key.
- No external service.
- No runtime module or bundled executable.

Plugin 不需要 MCP、API Key、外部服务或运行时代码。

## Post-install Check / 安装后检查

Test these two prompts separately:

```text
I have an idea for an internal system but do not know how to define the requirements. Help me clarify the smallest useful outcome.
```

Expected route: `cms-project-governance`.

```text
The target and acceptance criteria are authorized. Implement the next stage, run automatic and functional verification, and prepare evidence for review.
```

Expected route: `agent-loop-engineering`.
