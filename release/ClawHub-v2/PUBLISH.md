# ClawHub v2 Upload / ClawHub v2 上传

The two source folders are ready for direct ClawHub CLI publishing:

两个源目录可以直接通过 ClawHub CLI 发布：

- `skills/agent-loop-engineering`
- `skills/cms-project-governance`

Before editing the public listings, use the copy-ready values in:

编辑公开 listing 前，请使用以下文件中的可复制元数据：

- `release/ClawHub-v2/CATALOG_METADATA.md`

## 1. Preview / 预览

```powershell
npx.cmd --yes clawhub@latest skill publish ".\skills\agent-loop-engineering" `
  --slug agent-loop-engineering `
  --name "Agent Loop Engineering" `
  --owner englandtong `
  --version 2.0.0 `
  --changelog "V2 bilingual execution contract, bounded stages, evidence gates, and cross-platform state validation." `
  --tags latest `
  --dry-run

npx.cmd --yes clawhub@latest skill publish ".\skills\cms-project-governance" `
  --slug cms-project-governance `
  --name "CMS Project Governance" `
  --owner englandtong `
  --version 2.0.0 `
  --changelog "V2 bilingual goal discovery, adaptive governance, Active Packet handoff, alignment, and QA control." `
  --tags latest `
  --dry-run
```

## 2. Publish / 正式发布

Log in first with the official ClawHub CLI. Do not place tokens in these files.

先使用 ClawHub 官方 CLI 登录。不要把 Token 写入这些文件。

```powershell
npx.cmd --yes clawhub@latest login

npx.cmd --yes clawhub@latest skill publish ".\skills\agent-loop-engineering" `
  --slug agent-loop-engineering `
  --name "Agent Loop Engineering" `
  --owner englandtong `
  --version 2.0.0 `
  --changelog "V2 bilingual execution contract, bounded stages, evidence gates, and cross-platform state validation." `
  --tags latest

npx.cmd --yes clawhub@latest skill publish ".\skills\cms-project-governance" `
  --slug cms-project-governance `
  --name "CMS Project Governance" `
  --owner englandtong `
  --version 2.0.0 `
  --changelog "V2 bilingual goal discovery, adaptive governance, Active Packet handoff, alignment, and QA control." `
  --tags latest
```

ClawHub publishes folders, not these ZIP files. The ZIP files in this release folder are transport and review copies. Extract them before using the CLI if the source folders are unavailable.

ClawHub CLI 发布的是文件夹，不是本目录中的 ZIP。ZIP 只用于传输和审阅；如果没有源目录，请先解压再用 CLI 发布。
