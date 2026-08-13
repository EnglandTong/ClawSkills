# Agent Loop / CMS 2.1 Release Notes

## Agent Loop Engineering 2.1.0

- Adds Bounded Autopilot through Controller, Developer, Stage Reviewer, and repair cycles.
- Makes ordinary reversible project-local decisions autonomous.
- Stops only after the same failure signature has no new evidence twice or a real authority/safety gate is reached.
- Keeps QA failure on the same Packet and Work Order.
- Adds lightweight alignment each stage and formal alignment at stages 3, 6, and 10 or material triggers.
- Requires independent final acceptance for Standard and Full governance.
- Adds Compact context, focused-first testing, aggregated logs, and optional usage statistics.

## CMS Project Governance 2.1.0

- Adds read-only Legacy Bootstrap with case-insensitive `Docs/docs` discovery.
- Inventories file metadata before reading selected current authority and explicit links.
- Writes a compact Active Packet only when authority is coherent; conflicts produce zero writes and one consolidated Owner request.
- Separates Runtime, Contract, Governance, Artifact, and Mixed delivery claims.
- Stops duplicate status, next-action, completion, and per-stage handoff expansion after migration.
- Triggers governance review after repeated risk carry or three consecutive `Accepted With Risk` decisions.

## Compatibility

- `contract_version: "2.0"` remains supported.
- New Loop records use `record_version: "2.1"`.
- Old Loop records remain readable and are reported in aggregate by default.
- Existing legacy files remain historical and are not bulk-rewritten.

## 中文摘要

2.1 加入有界自主循环、主动诊断返修、分层验收、每阶段轻量对齐、旧项目只读引导、交付类别证据边界及低 Token 协议。Standard/Full 最终只能进入独立验收准备状态；旧日志默认聚合，不再逐行产生大量警告。
