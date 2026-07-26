# AI Engineering Expert

Version: 1.0.0

AI Engineering Expert is a bilingual, no-code bundle Plugin for governed AI-assisted software delivery. It packages two independent Skills and one Qoder expert role:

- `cms-project-governance`: turns ideas and changing requirements into clear, right-sized, reviewable delivery.
- `agent-loop-engineering`: executes an authorized software goal through bounded, evidence-backed coding loops.
- `ai-engineering-expert`: routes work between governance and execution without collapsing their authority boundaries.

## Why Two Skills

The two Skills remain separate by design:

- governance decides what should be built, how much control is needed, whether work remains aligned, and whether QA accepts it;
- execution decides how to implement the authorized target and supplies evidence.

They share the `ACTIVE_PACKET` contract but can still be invoked independently.

## Languages

Both Skills include complete English and Simplified Chinese instructions, references, and templates. The expert responds in the user's language. Machine-readable state keys and enum values remain English for interoperability.

## Qoder

The bundle contains:

- `.qoder-plugin/plugin.json`
- `qoder.md`
- `agents/ai-engineering-expert.md`
- `skills/*`

Qoder registers bundled Skills with plugin-qualified names:

```text
ai-engineering-expert:cms-project-governance
ai-engineering-expert:agent-loop-engineering
```

Qoder Expert Kits can install the ZIP directly. Qoder CLI can install the extracted directory as a local Plugin.

## ClawHub

This directory is a ClawHub `bundle-plugin`. It also includes a `.claude-plugin/plugin.json` compatibility marker for package discovery.

OpenClaw loads the two bundled Skill directories through `openclaw.plugin.json`. The manifest declares no runtime module, tools, hooks, services, or configuration fields.

Preview publication:

```powershell
npx.cmd --yes clawhub@latest package publish ".\plugins\ai-engineering-expert" `
  --family bundle-plugin `
  --name "@englandtong/ai-engineering-expert" `
  --version 1.0.0 `
  --owner englandtong `
  --dry-run
```

Publish only after the dry run and package validation pass.

## Dependencies And Permissions

- No MCP server.
- No API key.
- No external service.
- No bundled executable code.
- The execution Skill may ask the host agent to read, edit, test, or run project code, subject to the host's permission and sandbox controls.

## 中文说明

AI Engineering Expert 是一个中英文、无外部依赖的软件交付专家套件：

- `cms-project-governance` 负责需求、规划、规模、方向、重基线和 QA；
- `agent-loop-engineering` 负责经过授权的开发、调试、验证和循环推进；
- 专家角色负责判断先治理还是直接执行，但不会把两种权限混在一起。

Qoder Expert Kits 可以直接上传 ZIP。Qoder CLI 可以安装解压后的 Plugin 目录。Plugin 不需要 MCP、API Key 或外部服务。
