# ClawHub Workflow Suite Release

Prepared: 2026-08-14

This release updates four independently installable canonical Skills. `ai-workflow-os` is a router; it does not replace the three specialist Skills.

| Skill | Online baseline | Prepared version | Source path |
| --- | --- | --- | --- |
| `web-search-rules` | 3.0.0 | 4.0.0 | `skills/web-search-rules` |
| `project-lifecycle-navigator` | 1.0.0 | 2.0.0 | `skills/project-lifecycle-navigator` |
| `daily-workflow` | 3.0.0 | 4.0.0 | `skills/daily-workflow` |
| `ai-workflow-os` | 1.0.0 | 2.0.0 | `skills/ai-workflow-os` |

## Release Gate

1. Review `git diff` and keep unrelated user changes out of the release.
2. Run the validation commands in `VALIDATION.md`.
3. Commit and push the exact source.
4. Record the exact source commit; do not attribute these versions to the old `8aa6b34` baseline.
5. Run the four dry runs again with source provenance flags.
6. Confirm `clawhub whoami` returns the intended owner.
7. Obtain explicit authorization for the live external publication.
8. Publish one Skill at a time and inspect the exact version and scan result before continuing.

## Dry Run Template With Source Provenance

Replace `<release-commit>` and `<release-ref>` only after the exact source is committed and pushed.

```powershell
$common = @(
  '--source-repo', 'EnglandTong/ClawSkills',
  '--source-commit', '<release-commit>',
  '--source-ref', '<release-ref>'
)

npx.cmd --yes clawhub@latest skill publish ".\skills\web-search-rules" `
  --slug web-search-rules `
  --name "Web Search Rules / 网页研究与资料入库治理" `
  --version 4.0.0 `
  --changelog "Add claim-level evidence, source freshness, capability gates, and safer staged research intake." `
  --tags latest,web-search,research,source-governance,knowledge-base,bilingual `
  --source-path skills/web-search-rules @common --dry-run --json

npx.cmd --yes clawhub@latest skill publish ".\skills\project-lifecycle-navigator" `
  --slug project-lifecycle-navigator `
  --name "Project Lifecycle Navigator / 项目生命周期导航助手" `
  --version 2.0.0 `
  --changelog "Separate whole-system audit, latest-delivery review, and Owner-led rebaseline with evidence and authority gates." `
  --tags latest,project-management,product-management,mvp,code-review,bilingual `
  --source-path skills/project-lifecycle-navigator @common --dry-run --json

npx.cmd --yes clawhub@latest skill publish ".\skills\daily-workflow" `
  --slug daily-workflow `
  --name "Daily Workflow / 项目记忆工作流" `
  --version 4.0.0 `
  --changelog "Add read-only orientation, one-writer state ownership, exact evidence outcomes, and safer resumable handoffs." `
  --tags latest,project-memory,handoff,context-management,workflow,bilingual `
  --source-path skills/daily-workflow @common --dry-run --json

npx.cmd --yes clawhub@latest skill publish ".\skills\ai-workflow-os" `
  --slug ai-workflow-os `
  --name "AI Workflow OS / AI 工作流路由系统" `
  --version 2.0.0 `
  --changelog "Replace the duplicated all-in-one controller with a specialist router and one-writer authority model." `
  --tags latest,ai-workflow,orchestration,project-management,research-governance,bilingual `
  --source-path skills/ai-workflow-os @common --dry-run --json
```

If the shell does not expand `@common` as expected, write the four source flags explicitly. Do not remove `--dry-run` until the source provenance and identity are confirmed.

## Live Publication

```powershell
npx.cmd --yes clawhub@latest login
npx.cmd --yes clawhub@latest whoami
```

Run the same commands without `--dry-run` only after explicit authorization. A successful dry run is not publication. After each live publish:

```powershell
npx.cmd --yes clawhub@latest inspect @englandtong/<slug> --version <version> --files --json
```

Confirm version, display name, included files, source commit/path, tags, and scan verdict.

## Historical Duplicate

`@englandtong/web-search-rules-en` remains a separate live 3.0.0 listing. Do not publish the v4 source to both slugs. After the canonical v4 release is verified, decide separately whether to merge or redirect the historical English slug using the current ClawHub ownership workflow.
