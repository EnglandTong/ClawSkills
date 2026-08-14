# Detailed Review And Rebaseline

Date: 2026-08-14

## Executive Finding

The four Skills had useful content, but their system architecture was contradictory:

- three specialist Skills independently covered lifecycle, memory, and web intake;
- `ai-workflow-os` claimed to replace all three while shipping thinner copies of their workflows;
- formal governance and coding-loop responsibilities overlapped with `cms-project-governance` and `agent-loop-engineering`;
- metadata and version state differed across `SKILL.md`, references, generated registry snapshots, and agent configuration.

The update keeps all four canonical ClawHub listings, but changes their relationship:

```text
ai-workflow-os                         router only
  -> project-lifecycle-navigator       lifecycle advisory
  -> daily-workflow                    session memory
  -> web-search-rules                  web research intake
  -> cms-project-governance            formal control and acceptance
  -> agent-loop-engineering             authorized coding execution
```

One state surface now has one authoritative owner. Bundled `ai-workflow-os` modules are reduced-fidelity fallbacks, not competing implementations.

## 1. web-search-rules

### As Found

- `SKILL.md` called itself 3.0.0 while its config schema, `SECURITY.md`, sitemap, and several references described 4.0.0.
- Domain/source trust and claim truth were too easy to conflate.
- Search snippets could flow into staging without an explicit opened-source evidence state.
- Platform adapters were written as supported capabilities even though actual host tools may be absent.
- Examples used whitelist/auto-approved vocabulary that implied stronger evidence than was established.
- `agents/openai.yaml` did not use the current `interface` schema and its default prompt did not name `$web-search-rules`.

### Decision

Upgrade to 4.0.0 and retain as the authoritative web-research intake Skill.

### Material Changes

- Adds `discovered`, `opened`, `supported`, `corroborated`, `conflicted`, and `cannot-confirm` evidence states.
- Separates source rule, record quality, and claim support.
- Treats snippets as discovery only and requires actual source inspection for support.
- Adds freshness, primary-source preference, provenance, copyright-aware summarization, and explicit not-executed reporting.
- Makes platform support capability-based: unobserved capabilities are denied.
- Preserves dry-run, second-confirmation, prompt-injection, credential, and cloud-upload safeguards.
- Updates the rule engine, migration/test guide, examples, security checklist, and OpenAI metadata.

### Residual Risk

The platform operation references are procedural guidance only; live Feishu, DingTalk, Tencent Docs, IMA, Obsidian, and NotebookLM flows were not executed in this review.

## 2. project-lifecycle-navigator

### As Found

- Frontmatter contained a `version` field rejected by the current local `quick_validate.py`.
- No `agents/openai.yaml` existed.
- The three-mode design mixed repository-wide health review, current delivery review, and target change authority.
- Prompts forced 6-8 questions even when a repository could answer many of them directly.
- Code review emphasized source inspection but under-specified real user-visible runtime, evidence class, and independent acceptance boundaries.
- Rebaseline recommendations could be mistaken for authorization.

### Decision

Upgrade to 2.0.0 and retain as a read-only lifecycle advisory Skill.

### Material Changes

- Adds read-only repository orientation before questioning.
- Expands to five mutually distinct modes: New Project Intake, Mid-Project Realignment, Repository-Wide Health Review, Latest Delivery Alignment Review, and Owner-Led Target Rebaseline.
- Adds dedicated EN/ZH prompts for latest-delivery review and target rebaseline.
- Separates `implemented`, `partial`, `verified`, `unverified`, `unusable`, `documentation-conflict`, `not-executed`, and `cannot-confirm`.
- Requires product value, real user journey, data-to-analysis chain, runtime topology, and governance conflict review.
- Keeps `Developer Complete`, independent QA, and `Accepted` separate.
- Routes formal governance and implementation to the appropriate specialist Skills.

### Residual Risk

The large EN/ZH legacy prompts remain intentionally detailed for copy-ready use. They were structurally reviewed and updated, but not forward-tested in fresh agent sessions in this turn.

## 3. daily-workflow

### As Found

- UTF-8 BOM caused the first validator pass to report no frontmatter.
- Broad phrase triggers could create or rewrite a full `Docs/` scheme without first establishing whether another governance system already owned the state.
- It could create an unconfirmed target and later update it, which risked converting an AI summary into project authority.
- Its seven-file default duplicated state already owned by formal governance and coding-loop systems.
- Verification records did not consistently require exact commands, final exits, evidence boundaries, and deferred scenarios.
- `agents/openai.yaml` used the old flat schema.

### Decision

Upgrade to 4.0.0 and retain as the authoritative session-continuity Skill.

### Material Changes

- Adds read-only repository and governance orientation before writes.
- Requires clear persistence intent or an already configured trigger.
- Adds Existing Governance, Lightweight, and Legacy Migration profiles.
- Starts the lightweight profile with only `STATUS.md` and `NEXT_ACTIONS.md`.
- Prevents AI guesses from becoming `TARGET.md`; uses `TBD - Owner Confirmation Required`.
- Adds one-writer ownership, atomic state updates, dirty-worktree preservation, exact evidence outcomes, deferred scenario labels, and self-contained handoff requirements.
- Preserves formal QA, acceptance, and coding-loop evidence owned elsewhere.

### Residual Risk

No real project checkpoint or legacy-file migration was executed. The release validates the instructions and package, not every host project's custom governance schema.

## 4. ai-workflow-os

### As Found

- `SKILL.md` had no YAML frontmatter and failed standard validation.
- It claimed to replace the other three Skills while also depending on their concepts.
- Its modules duplicated thinner versions of specialist workflows, creating competing state and weaker safety/evidence rules.
- It defaulted to a large `Docs/` and knowledge-file layout without checking project authority.
- It did not define one writer per state surface or clear precedence with formal governance and coding execution.
- `agents/openai.yaml` used an unrelated legacy schema.

### Decision

Upgrade to 2.0.0 and rewrite as a router. Do not remove the listing; change its product position.

### Material Changes

- Adds a specialist map and authority order.
- Routes lifecycle, governance, coding, memory, research, and synthesis separately.
- Adds common end-to-end route patterns and a one-writer matrix.
- Treats bundled modules and templates as reduced-fidelity fallback only.
- Adds claim-ledger synthesis and precise evidence/completion vocabulary.
- Prevents fallback planning from being reported as specialist execution or independent acceptance.
- Updates fallback modules, migration guidance, security, usage examples, and OpenAI metadata.

### Residual Risk

Correct orchestration still depends on the host having the specialist Skills installed and on the agent honoring routing. This is a text Skill, not a hard runtime permission system.

## Package And Publication Findings

- All four Skills now have valid YAML frontmatter and current `agents/openai.yaml` metadata.
- `.clawhubignore` excludes stale `_meta.json`, generated `skill-card.md`, sitemap files, and project-only material where appropriate.
- Current ClawHub CLI dry-run accepts all four canonical folders.
- The historical `@englandtong/web-search-rules-en` listing remains a separate duplicate. Update only `web-search-rules` in this release; decide merge/redirect separately after the canonical v4 release is verified.
- Live publication, source commit/push, post-publication inspection, and post-publication security scan remain not executed.
