# Agent Loop / CMS 2.1 Validation

Date: 2026-08-13

## Source Validation

- Four `quick_validate` passes: two source Skills and two Plugin copies.
- All Node scripts pass `node --check`.
- 12 state-tool regression tests pass.
- Source and Plugin Skill copies are SHA256-identical.
- Plugin JSON manifests parse.
- `git diff --check` passes.
- Known mojibake and stale package-version scans pass.

## Regression Coverage

- R21/R23 current-route conflict.
- QA heading Accepted with superseding Failed body decision.
- Multiple same-level Current Assignment routes.
- Explicit Current Effective override and hierarchical M/P routes.
- Historical `Old` directory exclusion.
- Contract evidence promoted incorrectly to Runtime.
- Hundreds of legacy JSONL records with missing fields.
- Linked authority path escape.
- Stage Reviewer failure, repair, pass, and independent-acceptance boundary.
- Stage Reviewer attempting final acceptance.
- Unsafe `write_scope` and outside-write policy.

## Six Read-Only Project Samples

Every Docs tree had the same aggregate content fingerprint before and after bootstrap plus validation. No Active Packet was created.

| Project | Bootstrap result | Packet preview | Validator detail groups |
| --- | --- | ---: | ---: |
| RFTS ERP System | Coherent read-only draft | 87 lines, Mixed | 3 |
| Trade Data Analysis | Zero-write conflict: R21 vs R23 | none | 3 |
| Pixel Craft | Zero-write conflict: no active authorization | none | 4 |
| 学习培伴 | Coherent read-only draft | 93 lines, Artifact | 3 |
| MiniApp Hub | Coherent read-only draft | 107 lines, Contract | 3 |
| EduCore | Coherent read-only draft | 97 lines, Governance | 4 |

The validator aggregated 5,495 legacy warning occurrences into 20 returned category details across all six projects. Pixel Craft retained one invalid JSONL error; EduCore retained six. Aggregation did not hide these errors.

## ClawHub

- `package validate`: PASS, 0 breakages, 0 warnings.
- `@englandtong/agent-loop-engineering` 2.1.0 dry-run with three categories and five topics: PASS, 24 files, latest 2.0.0.
- Local `cms-project-governance` 2.1.0 dry-run against canonical ClawHub slug `coding-management-system`, with three categories and five topics: PASS, 24 files, latest 2.0.0.
- No live publication was attempted.
