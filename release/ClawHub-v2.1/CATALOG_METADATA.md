# ClawHub 2.1 Catalog Metadata / ClawHub 2.1 目录元数据

Use the English values below in ClawHub. Chinese text is a review aid. Keep both standalone listings live and independently searchable.

请把以下英文值填写到 ClawHub。中文只用于核对含义。两个独立 Skill listing 都应保持上线并可单独搜索。

Complete copy-ready records:

- `AGENT_LOOP_ENGINEERING_LISTING.md`
- `CMS_PROJECT_GOVERNANCE_LISTING.md`

Online identity checked on 2026-08-13: Agent Loop uses canonical slug `agent-loop-engineering`. The local CMS Skill is named `cms-project-governance`, but its existing ClawHub canonical slug is `coding-management-system`; `@englandtong/cms-project-governance` resolves to that listing. Update the existing canonical listing instead of creating a duplicate.

## Agent Loop Engineering

### Short Summary

```text
Runs low-context, bounded-autonomous coding loops with proactive repair, evidence gates, and independent final review.
```

中文参考：

```text
通过低上下文、有界自主开发、主动返修、证据门禁和独立终验，持续推进已授权的软件目标。
```

### Categories

1. `development` (`Development` in the UI)
2. `automation` (`Automation` in the UI)
3. `agents` (`Agents` in the UI)

### Topics

```text
ai-coding, autonomous-agents, software-testing, context-management, execution-loops
```

### Merge Listing

Leave unset. Do not merge this listing into another Skill.

保持为空。不要把此 listing 合并到其他 Skill。

## CMS Project Governance

### Short Summary

```text
Turns changing goals and legacy project records into compact, conflict-checked delivery with aligned scope and QA control.
```

中文参考：

```text
把变化中的目标和旧项目记录整理为精简、经过冲突检查、范围对齐且受 QA 控制的交付状态。
```

### Categories

1. `agents` (`Agents` in the UI)
2. `productivity` (`Productivity` in the UI)
3. `development` (`Development` in the UI)

### Topics

```text
project-governance, requirements-analysis, goal-alignment, qa-acceptance, token-efficiency
```

### Merge Listing

Leave unset. Specifically do not select:

```text
Agent Loop Engineering (agent-loop-engineering)
```

Merging would hide `cms-project-governance` from search and browse. Governance and execution remain separate capabilities.

保持为空，尤其不要选择 `Agent Loop Engineering (agent-loop-engineering)`。合并会隐藏治理 Skill，不符合双 Skill 独立安装和独立发现的设计。

## Listing Update Checklist

1. Save the Short Summary.
2. Save Categories and Topics.
3. Leave Merge Listing unchanged and empty.
4. Confirm both public listings remain visible in cards, search, and browse.
5. Confirm each canonical URL still resolves to its own Skill.
