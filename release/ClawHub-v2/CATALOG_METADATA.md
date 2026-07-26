# ClawHub Catalog Metadata / ClawHub 目录元数据

Use the English values below in ClawHub. Chinese translations are included for review only.

请把下面的英文值填写到 ClawHub。中文翻译只用于确认含义。

ClawHub currently allows up to three categories and five author topics per skill. Topics are normalized into lowercase, hyphenated slugs.

ClawHub 当前允许每个 Skill 最多选择 3 个 Categories 和 5 个 Topics。Topics 会被标准化为小写连字符格式。

## Agent Loop Engineering

### Short summary

```text
Runs bounded AI coding loops with persistent state, evidence gates, safe stops, and resumable handoffs.
```

中文参考：

```text
通过持久状态、证据门槛、安全停止和可恢复交接，运行有边界的 AI 编码循环。
```

### Categories

Select these in this order:

1. `Development`
2. `Automation`
3. `Agents`

### Topics

Paste or add these five topics:

```text
ai-coding, agentic-development, software-testing, execution-loops, context-recovery
```

### Merge listing

Leave this unset. Do not merge this listing into another skill.

保持为空，不要把这个 listing 合并到其他 Skill。

## CMS Project Governance

### Short summary

```text
Turns vague ideas into right-sized, governed AI delivery with clear goals, alignment checks, and QA acceptance.
```

中文参考：

```text
把模糊想法转化为规模适当、目标清晰、持续对齐并经过 QA 验收的 AI 交付。
```

### Categories

Select these in this order:

1. `Agents`
2. `Productivity`
3. `Development`

### Topics

Paste or add these five topics:

```text
project-governance, requirements-analysis, software-delivery, qa-acceptance, goal-alignment
```

### Merge listing

Leave this unset. Specifically, do **not** select:

```text
Agent Loop Engineering (agent-loop-engineering)
```

Merging would hide `cms-project-governance` from search and browse and redirect its old listing to `agent-loop-engineering`. These skills have separate responsibilities and should remain independently discoverable.

保持为空。不要选择 `Agent Loop Engineering (agent-loop-engineering)`。合并会隐藏 `cms-project-governance`，并把旧 listing 重定向到执行 Skill；这与两个 Skill 独立安装、独立发现和独立使用的设计冲突。

## Update Order / 更新顺序

For each skill:

1. Save `Short summary`.
2. Save `Catalog metadata`.
3. Leave `Merge listing` unchanged.
4. Reopen the public listing and confirm the card, categories, topics, search visibility, and canonical URL.

每个 Skill 都按以上顺序保存，并在公开页面复核卡片、分类、Topics、搜索可见性和正式 URL。

## Future Publishing Note / 后续发布注意

ClawHub can derive or update the listing summary from the `description` in `SKILL.md` during publishing. After publishing a new version, recheck the Short summary and restore the concise value above if needed.

ClawHub 发布新版本时可能根据 `SKILL.md` 的 `description` 更新 listing summary。以后发布新版本后，应再次检查 Short summary，必要时恢复为上面的精简版本。

Official references:

- https://github.com/openclaw/clawhub/blob/main/docs/skill-format.md
- https://github.com/openclaw/clawhub/blob/main/packages/schema/src/catalogMetadata.ts
- https://github.com/openclaw/clawhub/blob/main/src/components/SkillOwnershipPanel.tsx
