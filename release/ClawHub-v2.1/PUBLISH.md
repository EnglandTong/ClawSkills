# ClawHub 2.1 Validation And Publication

Run from the repository root. The dry-run commands below do not publish a live version.

请在仓库根目录运行。以下 dry-run 命令不会正式发布。

## Validate Source Skills

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\skills\agent-loop-engineering"
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\skills\cms-project-governance"
node ".\skills\agent-loop-engineering\scripts\test-state-tools.mjs"
```

## Dry Run

```powershell
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

`coding-management-system` is the existing canonical ClawHub slug for the local `cms-project-governance` Skill. Publishing under a different new slug can create a duplicate listing.

If the Owner explicitly wants the public canonical URL to match the local Skill name, perform a separate authenticated rename before publication:

```powershell
npx.cmd --yes clawhub@latest skill rename `
  @englandtong/coding-management-system `
  cms-project-governance
```

This is a live registry change with no dry-run option. It keeps the old slug as a redirect. After a successful rename, change the CMS publish command to `--slug cms-project-governance`. Do not run both slug variants as separate publications.

## Live Publication

Do not run until validation passes and an authorized ClawHub session is available. Do not store login tokens in this repository.

正式发布前必须通过全部验证并取得已授权的 ClawHub 登录状态。不要在仓库中保存 Token。

Remove `--dry-run` from the two commands only when live publication is explicitly authorized. Commit and push the exact 2.1 source first, then add the exact `--source-repo`, `--source-commit`, `--source-ref`, and `--source-path` values if source provenance is required. After publication, apply `CATALOG_METADATA.md` and confirm that Merge Listing remains empty.

只有明确授权正式发布时，才移除两个命令中的 `--dry-run`。发布后按 `CATALOG_METADATA.md` 更新目录字段，并确认 Merge Listing 仍为空。
