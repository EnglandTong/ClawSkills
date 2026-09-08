# Changelog

All changes in this release are additive and backward compatible. No `name` field, slug, directory layout, script path, script flag, enum value, or `contract_version` was changed or removed. Existing installs, Active Packets written at `contract_version: "2.0"`, and existing `LOOP_RUNS.jsonl` records at `record_version: "2.1"` continue to work unchanged.

Release date: 2026-09-07

## README Public Copy And Version Table (2026-09-08)

Documentation only. No Skill runtime, slug, or contract change.

- Root `README.md` opening rewritten as a short What / Who / Why. The Who/Why angle is England Tong's years in quality control (品管) and production-floor process, applied to agent project work.
- Skill table blurbs rewritten as plain result sentences. Dropped listing jargon from the public summary (`Bounded Autopilot`, `anti-involution`, `delivery-class evidence`, `control plane` / `execution plane` as table leads).
- Version table aligned to on-disk `SKILL.md` / `_meta.json` / `skill.json`: `cms-project-governance` **2.2.1**, `project-lifecycle-navigator` **2.1.1**, `agent-loop-engineering` 2.2.0, `ai-workflow-os` 2.1.0, `web-search-rules` 4.1.0, `daily-workflow` 4.1.0. Plugin called out as **1.1.3**.
- Removed the `## Version 2.1` heading and the stale `release/ClawHub-v2.1` / `AI-Engineering-Expert-v1.1.0` zip list (those artifacts are not in the tree). Kept the still-true coding-Skill rules under a version-free heading.
- Recommended-entry diagram now uses current Skill versions. Packet `contract_version: "2.0"` is unchanged.
- Local `node` commands documented for bash and PowerShell. ClawHub slug note for `coding-management-system` added next to install.
- Plugin `README.md` version header, bundled Skill versions, and `clawhub` `--version` examples updated from 1.1.1 / 2.1.1 to **1.1.3** / **2.2.1** / **2.2.0**, with a bash equivalent next to the PowerShell block.

## Fourth Pass: Positioning Split Between CMS And Navigator (2026-09-07)

A cross-skill duplicate scan (paragraph hashing, 6-gram Jaccard, term distribution, heading overlap) found that the six Skills are **not** largely duplicated. Only one file pair is materially redundant. What looked like duplication was **semantic crowding**: three Skills all speak the language of project governance, so their listing cards read like the same product.

**Constraint that shaped the fix.** `SKILL.md` is a cross-platform standard, so every Skill must be self-contained. A user may install exactly one Skill into any of 35+ products. Extracting shared files into a common directory is therefore not an option; it would break standalone installs instantly. Deduplication is limited to removing true duplicates, merging Skills, or repositioning copy. This pass takes the third route.

### What the scan actually found

| Layer | Finding | Verdict |
| --- | --- | --- |
| File level | `templates/{en,zh-CN}/ACTIVE_PACKET.md` exists in both `agent-loop-engineering` and `cms-project-governance`, Jaccard **1.00** after normalisation | 96% redundant, but the 5-line difference is deliberate |
| Boilerplate | `skill-card.md` `## Publisher` and `## Ethical Considerations` identical across all 6 Skills | Low value, no risk |
| Semantic | `cms` vs `navigator` share rebaseline 62/28, acceptance 53/34, scope 29/32, 101 KB vs 100 KB | **Only 1 shared H2 heading**, and navigator already defines an explicit boundary |

The 5 lines present only in the agent-loop copy are `agent_strategy`, `max_parallel_agents`, `context_return_policy`, `shared_authority_mode`, `single_writer`. The cms copy is a deliberate subset, because cms does not orchestrate multiple agents. Both copies are kept for self-containment, with a note recording the relationship.

### Changes

- `cms-project-governance` **2.2.0 -> 2.2.1** — opening sentence of `description` rewritten from a feature list to an outcome sentence. ClawHub derives the card summary from this sentence, so this is a listing copy change, not just a text edit. Ends with an explicit route to `project-lifecycle-navigator` for one-time read-only verdicts. `## Relationship To Agent Loop Engineering` gains the same routing rule in both English and Chinese.
- `project-lifecycle-navigator` **2.1.0 -> 2.1.1** — opening sentence rewritten to make the read-only audit role unmistakable. Ends with an explicit route to `cms-project-governance` for ongoing governance, Work Orders, Milestones and formal QA acceptance.
- Both copies of `ACTIVE_PACKET.md` in cms now carry an inline note naming the omitted fields and pointing to the full template.
- `scripts/publish-clawhub.sh` versions updated to match, so the next publish cannot ship a stale version number.
- Plugin `ai-engineering-expert` **1.1.2 -> 1.1.3** across all four manifests, because it embeds the cms copy.

Before / after opening sentences:

| Skill | Was | Now |
| --- | --- | --- |
| `cms-project-governance` | Turn vague or changing goals and legacy CMS project records into one compact, conflict-checked delivery state with clear outcomes, right-sized scope, bounded autonomy, alignment checks, delivery-class-aware evidence, and independent QA control. | Keep a drifting or half-finished project under control with one compact, conflict-checked delivery state, right-sized scope, bounded autonomy, and independent QA acceptance. |
| `project-lifecycle-navigator` | Navigate software and AI projects through evidence-based discovery, MVP definition, mid-project realignment, repository-wide health review, latest-delivery alignment review, and Owner-led target rebaseline. | Audit a project you are unsure about and get a go, narrow, pivot, archive or stop recommendation, without writing code or changing governance state. |

Deliberately unchanged: the six-Skill split, all slugs, all directory layouts, and the two `-en` listings whose ownership cannot be confirmed from the public API.

## Third Pass: Repository Hygiene And Cross-Platform Readiness (2026-09-07)

Triggered by a full local-vs-remote audit of `EnglandTong/ClawSkills`. Remote `main` was confirmed identical to local `HEAD` at `094efe2` by per-blob SHA comparison, so every change below is repository hygiene and release safety, not a behaviour change to any Skill. All changes remain additive and backward compatible.

### Fixed: version drift was checked in three places, not five

Release process tracked `SKILL.md`, `_meta.json` and `skill.json`. Two more files also carry a version number and both had silently drifted:

| Skill | File | Was | Now |
| --- | --- | --- | --- |
| `daily-workflow` | `sitemap.xml` | **3.0.0** | 4.1.0 |
| `web-search-rules` | `sitemap.xml` | 4.0.0 | 4.1.0 |
| `daily-workflow` | `SECURITY.md` | 4.0.0 | 4.1.0 |
| `web-search-rules` | `SECURITY.md` | 4.0.0 | 4.1.0 |
| `ai-workflow-os` | `SECURITY.md` | 2.0.0 | 2.1.0 |

`daily-workflow` was behind by a full major version. All six Skills now agree across all five locations.

### New file: `scripts/preflight.sh`

The drift above is now machine-checked before every release. Six gates: five-location version sync, `plugins/ai-engineering-expert/skills/` byte-identical to `skills/`, clean scan (email, absolute local path, phone number, stale zip), YAML frontmatter validity, `QUICKSTART.md` required fields, and the four plugin manifests agreeing on a version. Exits non-zero on any failure. It caught three real defects on its first run, including an unsynced bundled copy created minutes earlier.

### Six packages now have identical structure

`agent-loop-engineering` and `cms-project-governance` were missing `SECURITY.md`, `skill-card.md` and `.clawhubignore` that the other four already had; `project-lifecycle-navigator` was missing `SECURITY.md`. All added, bilingual, with rules specific to each Skill rather than a shared boilerplate. Note the four non-primary Skills stay inline-bilingual by design and intentionally have no `SKILL.zh-CN.md`.

### Metadata for cross-platform indexes

All six `_meta.json` files carried `version` and internal ClawHub IDs only. Added `license`, `author`, `homepage`, and `tags` / `topics` arrays matching `scripts/publish-clawhub.sh`, since third-party indexes read license and author. Existing `ownerId`, `slug`, `version` and `publishedAt` are untouched.

### Removed from the public repository

`docs/agent-loop-24h-temp-notes.md` (June temporary notes) and `plugins/work/` (six plugin-inspector validation artifacts). Two stale `skills/*.zip` from June were deleted locally; they were never tracked by git, so no history rewrite is needed.

### `HANDOFF_NEXT_AI_2026-08-17.md` path disclosure

Five absolute paths of the form `D:\Development\ClawSkills\ClawSkills` were committed to a public repository, contradicting the clean-scan rule adopted the previous day. Replaced with `<repo-root>`. The earlier scan covered `skills/` and `plugins/` only and missed root-level Markdown; the scan in `preflight.sh` now covers the tracked tree.

### `cms-project-governance` works standalone

Three references to `{baseDir}/../agent-loop-engineering/...` are a convenience for co-installed setups and fail when only the governance Skill is installed. One rule in the Relationship section now covers all of them: state the absence in one line and substitute the in-skill action, never fail the run. This is a clarification of existing intent, not a change to authority boundaries.

### Cross-platform distribution

Added `skills.sh.json` and an Install Anywhere section to `README.md`. `SKILL.md` is an open standard read by 35+ agent products, so no per-platform content variant is needed or permitted. Documented the rule that GitHub is the canonical source and ClawHub is one publish target, with change order local, then changelog, then commit and push, then index refresh.

### Tooling

`git config --global http.sslBackend openssl` is required on this machine. Git for Windows defaults to `schannel`, which fails TLS handshake behind the local proxy with `server closed abruptly (missing close_notify)`. This affects git network operations only; no token is needed for a public repository.

---

## Second Pass: Discoverability And Conversion (2026-09-07)

Triggered by a ClawHub telemetry audit. Measured position before this pass, across **8** listings including two legacy `-en` duplicates:

| Metric | Value |
| --- | --- |
| Total downloads | 5,194 |
| Total installs | 83 |
| Conversion | **1.60%** (site-wide average 2.56%) |
| Stars | 0 on every listing |
| Best / worst conversion | `web-search-rules-en` 2.28% / `coding-management-system` 0.17% |

Diagnosis was "seen but not installed", so this pass targets clarity and friction rather than content depth.

### New file: `scripts/publish-clawhub.sh`

Root cause of missing tags found and fixed. `clawhub publish` defaults `--tags` to `latest`; any publish that omits the flag silently replaces that listing's whole tag history with a single `latest` entry. That is exactly how `coding-management-system` and `agent-loop-engineering` ended up with 1 tag and 0 topics. All six listings now have their slug, version, topics, tags and changelog pinned in one script, defaulting to `--dry-run` and accepting `--yes` / `--only`. Verified with `bash -n` plus a mocked `CLAWHUB_CLI=echo` run.

### Install Intelligence

`summary` on the listing card is generated server-side from `description`, so the abstract first sentence was directly costing installs. Rewritten to lead with a concrete result:

| Skill | Before | After |
| --- | --- | --- |
| `web-search-rules` | "Govern evidence-backed web research and controlled knowledge-base intake" | "Search the web and save findings into your knowledge base with a source URL, date and quote attached to every claim. Works with Obsidian, NotebookLM, IMA, Feishu Docs and Tencent Docs." |
| `daily-workflow` | "Preserve concise, evidence-backed project memory across..." | "Say 开工啦 or 收工啦 and get a resumable project note written for you, so tomorrow you or another AI can pick up without re-reading everything." |

### New: `QUICKSTART.md` in all six Skills

Each contains install command, one trigger phrase, what to expect within 30 seconds, a minimum-usable path that skips the advanced surface, and an explicit privacy block (runs locally, stores no credentials, confirms before destructive actions). The two promoted Skills get the fuller treatment; the other four stay short and are labelled advanced or dependency so they do not compete for attention.

`cms-project-governance/QUICKSTART.md` also documents that the ClawHub slug is `coding-management-system`, since the directory name differs and there is no redirect.

### Listing metadata to be restored on next publish

| Skill | Tags before | Tags pinned | Topics before | Topics pinned |
| --- | --- | --- | --- | --- |
| `coding-management-system` | 1 | 19 | 5 | 5 (rewritten) |
| `agent-loop-engineering` | 1 | 21 | **0** | 4 (new) |
| `ai-workflow-os` | 14 | 17 | 1 | 4 |
| `project-lifecycle-navigator` | 9 | 14 | 2 | 4 |
| `web-search-rules` | 21 | 25 | 4 | 5 |
| `daily-workflow` | 22 | 21 | 3 | 5 |

`Handoff` was added to `daily-workflow` topics and `Obsidian` to `web-search-rules` topics, both being search terms the previous metadata missed.

### Not done — needs Owner decision

Merging the two legacy `-en` listings (`web-search-rules-en` 747/17, `daily-workflow-en` 636/14) into their bilingual originals. Ownership cannot be confirmed from the public API and deletion is irreversible, so no action was taken.

---

## Version Matrix

| Artifact | Before | After | Files touched |
| --- | --- | --- | --- |
| `agent-loop-engineering` | 2.1.1 | **2.2.0** | `SKILL.md`, `SKILL.zh-CN.md`, `_meta.json`, new `references/{en,zh-CN}/anti-patterns.md` |
| `cms-project-governance` | 2.1.2 | **2.2.0** | `SKILL.md`, `SKILL.zh-CN.md`, `_meta.json`, new `references/{en,zh-CN}/anti-involution.md` |
| `project-lifecycle-navigator` | 2.0.0 | **2.1.0** | `SKILL.md`, `_meta.json`, `skill.json`, `skill-card.md`, `publish/CLAWHUB_LISTING.en.md` |
| `daily-workflow` | 4.0.0 | **4.1.0** | `SKILL.md`, `_meta.json`, `skill-card.md` |
| `web-search-rules` | 4.0.0 | **4.1.0** | `SKILL.md`, `_meta.json`, `skill-card.md` (plus the sample `config.json` version string inside `SKILL.md`) |
| `ai-workflow-os` | 2.0.0 | **2.1.0** | `SKILL.md`, `_meta.json`, `skill-card.md` |
| `@englandtong/ai-engineering-expert` | 1.1.1 | **1.1.2** | `package.json`, `openclaw.plugin.json`, `.claude-plugin/plugin.json`, `.qoder-plugin/plugin.json`, re-synced `skills/` |
| Repository `README.md` | — | updated | version table, bundle-plugin section |

### Version Drift Fixed

`_meta.json` had drifted from `SKILL.md` on four Skills, which made ClawHub release metadata disagree with the shipped instructions. All four are now aligned:

| Skill | `_meta.json` before | `_meta.json` after |
| --- | --- | --- |
| `ai-workflow-os` | 1.0.0 | 2.1.0 |
| `daily-workflow` | 3.0.0 | 4.1.0 |
| `project-lifecycle-navigator` | 1.0.0 | 2.1.0 |
| `web-search-rules` | 3.0.0 | 4.1.0 |

---

## `agent-loop-engineering` 2.1.1 -> 2.2.0

| Change | Where | Why |
| --- | --- | --- |
| `description` expanded with trigger phrases and edge topics | `SKILL.md` frontmatter | Search recall on ClawHub; users search by what they say, not by capability nouns |
| New section `Stall Rule` | `SKILL.md` > Bounded Autopilot | The dominant real failure is escaping a stall by restarting the project, which re-buys the same constraint |
| New section `Deterministic Paths` | `SKILL.md` > Bounded Autopilot | Wall-clock budgets inside deterministic algorithms produce flaky evidence and unreproducible results |
| New section `Gates A Human Must Physically Perform` | `SKILL.md` > Stages And Alignment | A manual check written as a blocking precondition froze a finished milestone for weeks; it must be deferred, not blocking |
| New section `Evidence Downgrade Ban` table | `SKILL.md` > Evidence And Verification Cost | Consolidates the recurring claim-class errors (build = usable, unit test = flow works, never-assessed security = Passed) into one enforceable list |
| `Hard Stops` +2 bullets | `SKILL.md` > Hard Stops | Real personal/confidential data shipping inside distributed artifacts, and bulk restructure without a backup |
| New reference `anti-patterns.md` (en + zh-CN) | `references/` | Keeps the long diagnostic detail out of the always-loaded `SKILL.md`, consistent with the Skill's own compaction rule |

## `cms-project-governance` 2.1.2 -> 2.2.0

| Change | Where | Why |
| --- | --- | --- |
| `description` expanded with trigger phrases | `SKILL.md` frontmatter | Search recall; adds the involution, kill-or-keep, and accepted-but-never-released cases |
| Core Principles +11, +12 | `SKILL.md` > Core Principles | Names governance involution and in-place voiding as first-class principles so later rules have a basis |
| New section `Anti-Involution Controls` | `SKILL.md` | Doc budget, doc-to-code signal, archive-by-moving, additive rebaseline, risk-acceptance exit, subtraction gate |
| `Required Gates` +4 bullets | `SKILL.md` > Required Gates | Makes the above enforceable rather than advisory |
| New reference `anti-involution.md` (en + zh-CN) | `references/` | Detection table and detailed procedures kept out of the hot path |

## `project-lifecycle-navigator` 2.0.0 -> 2.1.0

| Change | Where | Why |
| --- | --- | --- |
| `description` expanded | `SKILL.md` frontmatter | Adds the highest-frequency real requests: should I keep going, kill it, is it over-engineered, what does done mean |
| New section `Startup Gates` | `SKILL.md` | Four questions, a 100-point go/no-go score, first-version caps, and a pre-commit stop-loss. Prevents the failure that starts before any code exists |
| Mode B: narrow instead of restart | `SKILL.md` > Mode B | Restarting discards working code; the constraint is usually scope |
| Mode C: structural-defect checklist | `SKILL.md` > Mode C | Adds duplicate copies, missing/invalid version anchor, build residue, shipped secrets, debug bypass, entrypoint truth, god modules, dependency sprawl |
| Decision Rules +8, +9, +10 | `SKILL.md` | Single source, subtraction before addition, back up before restructure |
| Evidence vocabulary +`duplicate-copy`, +`unversioned` | `SKILL.md` | Lets an audit state these findings without borrowing another skill's terms |
| `skill.json` tags + version; `skill-card.md`; `CLAWHUB_LISTING.en.md` | publish surfaces | Listing metadata and trigger examples kept in step with the Skill |

## `daily-workflow` 4.0.0 -> 4.1.0

| Change | Where | Why |
| --- | --- | --- |
| `description` expanded | `SKILL.md` frontmatter | Adds the real session-switch triggers (change agent, context nearly full, resume tomorrow) |
| New section `Memory Bloat Control` | `SKILL.md` | Session memory had the same involution risk as governance; adds live-set budget and archive-not-annotate discipline |
| New section `Before A Bulk Restructure` | `SKILL.md` | A checkpoint is the natural place to enforce backup-before-change |
| `Safety` extended | `SKILL.md` | Handoffs travel into new sessions and issue trackers, so real contact data is now explicitly excluded |

## `web-search-rules` 4.0.0 -> 4.1.0

| Change | Where | Why |
| --- | --- | --- |
| `description` expanded | `SKILL.md` frontmatter | Adds fact-check, latest-policy/price/version, and AI-summary-accuracy triggers |
| Safety Baseline +9, +10 | `SKILL.md` | Metadata is a producer's assertion, not a fact; snippets and AI overviews are `discovered`, never `supported` |
| New `Single-Source Rule` | `SKILL.md` > Evaluate Sources | One source supports awareness, not a conclusion; numeric/legal/pricing/version claims require a primary read |
| Sample `config.json` version | `SKILL.md` > Configuration Contract | Keep the documented config in step with the Skill version |

## `ai-workflow-os` 2.0.0 -> 2.1.0

| Change | Where | Why |
| --- | --- | --- |
| `description` expanded | `SKILL.md` frontmatter | Adds the "which skill should handle this" and end-to-end routing triggers |
| New section `Scope Collapse Guard` | `SKILL.md` | A combined request must not silently become authorization for new scope; the router reduces scope, it does not expand it |

## `@englandtong/ai-engineering-expert` 1.1.1 -> 1.1.2

| Change | Why |
| --- | --- |
| Re-copied `skills/cms-project-governance` and `skills/agent-loop-engineering` into the plugin | The bundled CMS copy was stuck at 2.1.1 and was missing `scripts/` and both `cross-plugin-file-contracts.md` files, breaking the release rule that bundled copies stay identical to source. Both trees now pass `diff -rq` with zero differences |
| Version bumped in all four manifests | Keeps plugin version honest about content change |
| `description` updated in all four manifests | Reflects the added anti-involution coverage |

## Not Changed On Purpose

- All `name` fields and slugs. They are the install and cross-reference contract; renaming would break existing installs and every `use <skill>` reference inside the other Skills.
- Directory layout, script filenames, script flags, `contract_version: "2.0"`, `record_version: "2.1"`, and all enum values.
- The `qc` -> `Stage Reviewer` mapping and the `Ready for Review` legacy input handling.
- CDH cross-plugin contract schema text in `cms-project-governance`; it was verified consistent with the governance and supervisor plugin implementations and was left untouched.
