# Validation Record

Prepared: 2026-08-14  
Repository baseline before edits: `main` at `8aa6b34`  
ClawHub CLI: `0.23.3`

## Source Validation

All four source folders passed the current local `quick_validate.py` with `PYTHONUTF8=1`:

- `web-search-rules`: PASS
- `project-lifecycle-navigator`: PASS
- `daily-workflow`: PASS
- `ai-workflow-os`: PASS

All four `agents/openai.yaml` files passed local checks for:

- `interface.display_name`
- 25-64 character `interface.short_description`
- `interface.default_prompt` containing the exact `$skill-name`

Additional checks:

- Internal Markdown links: PASS
- Referenced prompt/module/resource paths from each `SKILL.md`: PASS
- `git diff --check`: PASS
- UTF-8 frontmatter parsing: PASS

The first `quick_validate.py` attempt failed before content validation because the Windows default decoder used GBK. Re-running with `PYTHONUTF8=1` produced the results above.

## Online Baseline

Read-only `clawhub inspect --versions --json` confirmed:

| Canonical slug | Current latest | Scan verdict |
| --- | --- | --- |
| `@englandtong/web-search-rules` | 3.0.0 | clean |
| `@englandtong/project-lifecycle-navigator` | 1.0.0 | clean |
| `@englandtong/daily-workflow` | 3.0.0 | clean |
| `@englandtong/ai-workflow-os` | 1.0.0 | clean |

Historical duplicate observed: `@englandtong/web-search-rules-en` 3.0.0, scan verdict clean.

## ClawHub Dry Run

All four commands returned `ok: true` and `status: would-publish`:

| Skill | Prepared version | Files | Fingerprint |
| --- | ---: | ---: | --- |
| `web-search-rules` | 4.0.0 | 14 | `9600a485620a6d7234a554f2e1fce8af5601e2e6e2408e5816f5269aac889e78` |
| `project-lifecycle-navigator` | 2.0.0 | 13 | `b56bc1ed5fabe03b1b7aaa6d28b69c1a23075304dbc901e9a2446fe96cc62513` |
| `daily-workflow` | 4.0.0 | 3 | `16af70d9d18dc9794face4ede667fe0ef1ec62e0660730dd28acbd0eb7f521d6` |
| `ai-workflow-os` | 2.0.0 | 31 | `da5c78ee676f7cc9aa02af6ad457696d04fdaf1821024ddc1e1da5522bf2782e` |

The file counts confirm `.clawhubignore` excluded `_meta.json`, `skill-card.md`, sitemap files, and project-only publishing/readme metadata as intended.

## Evidence Boundary

- Live publication: Not Executed.
- Post-publication scan: Not Executed.
- Source commit and push: Not Executed.
- Forward-testing on fresh agents: Not Executed because this turn did not have explicit multi-agent authorization.

Do not call the release published or accepted until the live external operation and post-publication inspection are complete.
