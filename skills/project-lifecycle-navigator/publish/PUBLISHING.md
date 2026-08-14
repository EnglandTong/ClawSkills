# Publishing To ClawHub / 发布到 ClawHub

Publish from the repository root. ClawHub publishes the skill folder containing `SKILL.md`; `.clawhubignore` removes repository-only and generated files from the bundle.

## Release Identity

- Slug: `project-lifecycle-navigator`
- Display name: `Project Lifecycle Navigator`
- Version: `2.0.0`
- Source path: `skills/project-lifecycle-navigator`
- License: ClawHub `MIT-0`

Before a live release, inspect the existing listing and confirm that this slug is still the canonical owned identity. A local `_meta.json` is historical registry state, not proof of the current live version.

## Validation

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" `
  ".\skills\project-lifecycle-navigator"

npx.cmd --yes clawhub@latest skill publish ".\skills\project-lifecycle-navigator" `
  --slug project-lifecycle-navigator `
  --name "Project Lifecycle Navigator" `
  --version 2.0.0 `
  --changelog "Separate whole-system audit, latest-delivery review, and Owner-led rebaseline; add evidence states and specialist handoff boundaries." `
  --tags latest,project-management,product-management,ai-coding-agent,mvp,code-review,bilingual `
  --dry-run
```

## Live Release Gate

Do not publish live until the exact source is committed and pushed, the dry run is clean, and the user explicitly authorizes publication.

```powershell
npx.cmd --yes clawhub@latest login
npx.cmd --yes clawhub@latest whoami

npx.cmd --yes clawhub@latest skill publish ".\skills\project-lifecycle-navigator" `
  --slug project-lifecycle-navigator `
  --name "Project Lifecycle Navigator" `
  --version 2.0.0 `
  --changelog "Separate whole-system audit, latest-delivery review, and Owner-led rebaseline; add evidence states and specialist handoff boundaries." `
  --tags latest,project-management,product-management,ai-coding-agent,mvp,code-review,bilingual
```

A dry run is not publication. After a live publish, inspect the exact version and security scan result before calling the release complete.

## Changes In 2.0.0

- Adds separate Latest Delivery Alignment and Owner-Led Target Rebaseline modes.
- Keeps repository-wide audit read-only and distinct from delivery review and final QA.
- Adds evidence vocabulary, Owner authority gates, user-visible runtime expectations, and specialist handoffs.
