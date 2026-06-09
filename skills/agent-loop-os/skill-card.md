## Description: <br>
Agent Loop OS is a runner-neutral AI coding loop controller. It keeps project goals, acceptance criteria, current status, pending work, verification evidence, stop rules, and loop history in project-local `Docs/` files so multiple AI coding agents can continue the same development work safely. <br>

Agent Loop OS 是一个不绑定具体产品的 AI 编码循环总控 Skill。它把项目目标、验收标准、当前状态、待办、验证证据、停止规则和循环历史保存在项目本地 `Docs/` 文件中，让多个 AI Coding Agent 可以安全接力同一个开发任务。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[englandtong](https://clawhub.ai/user/englandtong) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and AI-assisted teams use this skill to control long-running or repeated coding work across Codex, Claude Code, OpenCode, Cline, Qoder, CodeBuddy, Trae, Gemini CLI, Aider, GitHub Actions, or other AI coding agents. It defines a shared `Docs/` state protocol, context budget rules, environment escalation boundaries, runner adapter contracts, and completion gates for Done / Done with Risk / Blocked. <br>

开发者和 AI 辅助团队可以用它管理长期运行或多轮重复的编码工作，适配 Codex、Claude Code、OpenCode、Cline、Qoder、CodeBuddy、Trae、Gemini CLI、Aider、GitHub Actions 或其他 AI Coding Agent。它定义共享的 `Docs/` 状态协议、上下文预算、环境问题升级边界、runner 适配契约，以及 Done / Done with Risk / Blocked 完成门禁。 <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes project-local `Docs/` state files that may include project context, verification summaries, blockers, and file paths. <br>
Mitigation: Review `Docs/` before sharing or committing, keep `.agent/logs/` out of public commits unless sanitized, and never store secrets, private customer data, full logs, or full chat transcripts in project state. <br>
风险：本 Skill 会写入项目本地 `Docs/` 状态文件，其中可能包含项目上下文、验证摘要、阻塞项和文件路径。 <br>
缓解：分享或提交前先审查 `Docs/`；除非已脱敏，否则不要把 `.agent/logs/` 提交到公开仓库；不要在项目状态中保存密钥、真实用户数据、完整日志或完整聊天记录。 <br>
Risk: Long-running agents may continue in the wrong direction if goals or acceptance criteria are unclear. <br>
Mitigation: Use `Docs/TARGET.md` and `Docs/ACCEPTANCE.md` as the source of truth, require bootstrap confirmation when the target is unclear, and stop when next actions conflict with the target. <br>
风险：如果目标或验收标准不清晰，长期运行的 Agent 可能沿错误方向继续。 <br>
缓解：以 `Docs/TARGET.md` 和 `Docs/ACCEPTANCE.md` 作为唯一目标与验收来源；目标不清时先 bootstrap 并确认；下一步与目标冲突时必须停止。 <br>
Risk: Multiple AI agents may overwrite each other's state. <br>
Mitigation: Use canonical `Docs/` file names, preserve loop evidence, write one bounded loop at a time, and require sequential scheduling or file locking for multiple runners. <br>
风险：多个 AI Agent 可能互相覆盖状态。 <br>
缓解：使用统一 canonical `Docs/` 文件名，保留 loop evidence，每次只写入一个有边界的 loop；多 runner 需要串行调度或文件锁。 <br>
Risk: Environment work may require credentials, production data, system installs, or irreversible Git operations. <br>
Mitigation: Treat these as hard stops, write `Blocked`, and ask a human. `allow_*` flags cannot override hard stops. <br>
风险：环境问题可能涉及凭证、生产数据、系统安装或不可逆 Git 操作。 <br>
缓解：这些情况一律视为 hard stop，写入 `Blocked` 并询问人类；`allow_*` 配置不能覆盖硬停止规则。 <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/englandtong/agent-loop-os) <br>
- [Security Guide](SECURITY.md) <br>
- [Loop State Protocol](references/loop-state-protocol.md) <br>
- [Completion Gate](references/completion-gate.md) <br>
- [Runner Adapters](references/runner-adapters.md) <br>
- [Context Budget](references/context-budget.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSONL, Configuration, Guidance] <br>
**Output Format:** [Project-local Docs/ Markdown state files, LOOP_RUNS.jsonl loop records, concise chat reports, runner adapter prompts, and verification summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Maintains project-local state; supports multi-agent handoff; does not require global memory; stops on credentials, production data, system installs, destructive operations, and unclear direction.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md, _meta.json, SECURITY.md, and release validation) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their development environment, review generated or modified project state before relying on it, and apply their organization's safety, security, privacy, and compliance requirements before deployment. <br>

用户应根据自己的开发环境判断是否适合使用本 Skill；依赖生成或修改的项目状态前，应先审查内容，并在部署前遵守所在组织的安全、隐私和合规要求。 <br>
