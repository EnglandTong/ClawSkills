#!/usr/bin/env python3
"""Bootstrap CMS Lite Agent Loop docs with _Workbuddy suffix for each Development project."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATE = "2026-06-16"

PROJECTS = [
    {
        "root": r"D:\Development\OperationsManagement\inventory_system",
        "id": "inventory_system",
        "name": "库存管理系统 (Inventory System)",
        "goal": "维护基于 Flask + SQLite 的库存管理服务：Excel 数据源同步、库存查询/更新、局域网部署与自动同步调度。",
        "non_goals": [
            "不在此任务中重写为 FastAPI 或替换 Prisma",
            "不混入 Forecast 或 Cost&Price 模块字段",
            "不恢复 D:\\Recover 中已损坏的 flat 文件碎片",
        ],
        "scope": "Medium",
        "path": r"D:\Development\OperationsManagement\inventory_system",
        "recover_path": r"D:\Recover\ERP",
        "stack": "Flask 3.x, pandas, openpyxl, SQLite, gunicorn/psycopg(云部署)",
        "verify_auto": "python -m pip install -r requirements.txt",
        "verify_func": "python app.py 后 GET /api/inventory 返回 200",
        "must_pass": [
            "requirements.txt 依赖可安装",
            "python app.py 可启动并绑定 0.0.0.0:5000",
            "POST /api/sync 可从配置数据源同步到 inventory.db",
            "B2B_PATH/B2C_PATH/CALENDAR_PATH 环境变量行为与 README 一致",
            "init_data.py 在缺失 Excel 时不阻塞启动",
        ],
        "failure": [
            "inventory.db 无法读写",
            "同步后库存主表为空且无明确跳过原因",
            "局域网第二台机器无法访问 5000 端口",
        ],
        "status": "Continue",
        "last_action": "2026-06-16 灾难恢复盘点：源码在 D:\\Development 完整；D:\\Recover\\ERP 多为 node_modules 碎片，仅 env 模板可读。",
        "next": "在本机运行 python app.py 与 POST /api/sync，确认 inventory.db 与 .uploads 数据完整。",
        "blocked": False,
    },
    {
        "root": r"D:\Development\OperationsManagement\ForecastSystem",
        "id": "forecast_system",
        "name": "Focus Forecast System",
        "goal": "提供独立销售 Forecast/Budget 模块：12 个月滚动 Forecast、版本 ACTIVE/INACTIVE 管理、客户/产品主数据维护。",
        "non_goals": [
            "不引入 costPrice/sellingPrice/COGS 等成本价格字段",
            "不实现 BW 平台 RBAC 全套",
            "不从 Recover 根目录 36 万碎片还原目录树",
        ],
        "scope": "Medium",
        "path": r"D:\Development\OperationsManagement\ForecastSystem",
        "recover_path": r"D:\Recover\ERP - BW - Inventory",
        "stack": "Flask/Python, SQLite (forecast.db)",
        "verify_auto": "项目 README 指定测试或 python -m pytest",
        "verify_func": "启动服务并打开 Forecast 录入页，可创建/激活版本",
        "must_pass": [
            "forecast.db 可读写",
            "客户/产品主数据 CRUD 正常",
            "新建 ACTIVE 版本并复制来源版本明细",
            "按 anchor_month 规则仅一个 ACTIVE",
            "页面四种 Focus 录入模式行为符合 README",
        ],
        "failure": [
            "Forecast 行混入成本/采购价字段",
            "同 anchor_month 出现多个 ACTIVE",
            "版本对比无法导出",
        ],
        "status": "Continue",
        "last_action": "Recover 子目录 ERP - BW - Inventory 为空；ForecastSystem 在 Development 完整保留。",
        "next": "启动 ForecastSystem 并验证 forecast.db 与 docs/LAN_DEPLOYMENT.md 步骤。",
        "blocked": False,
    },
    {
        "root": r"D:\Development\OperationsManagement\Cost&Price_Structure",
        "id": "cost_price_structure",
        "name": "成本与价格结构管理系统",
        "goal": "管理国际贸易成本与价格结构：贸易流程、成本节点(KG/LB/Pack)、多币种报价与 Excel 导出。",
        "non_goals": [
            "不替换为 MarketSurvey 竞品追踪模型",
            "不在此轮实现 BW 平台自动同步",
        ],
        "scope": "Medium",
        "path": r"D:\Development\OperationsManagement\Cost&Price_Structure",
        "recover_path": r"D:\Recover\Market",
        "stack": "Vue 3 + Element Plus + Express + Prisma + SQLite",
        "verify_auto": "server npm run typecheck; client npm run build",
        "verify_func": "start.bat 启动后访问 TradeFlowConfig",
        "must_pass": [
            "server prisma dev.db 可读写",
            "tradeFlows/costNodes/customers API 正常",
            "TradeFlowConfig 与 CostEditor 页面可加载",
            "Excel 导出可用",
            "AI_HANDOVER.md 中数据模型与实现一致",
        ],
        "failure": [
            "Prisma migrate 失败",
            "三单位换算错误",
            "报价单 Excel 字段缺失",
        ],
        "status": "Continue",
        "last_action": "Recover/Market 含 Trade Data Analysis FastAPI 依赖碎片，与本项目 Vue+Express 栈不同；以 Development 为准。",
        "next": "运行 start.bat，验证 client/server 联调与 .uploads 目录。",
        "blocked": False,
    },
    {
        "root": r"D:\Development\MarketResearchTools\MarketSurvey",
        "id": "marketsurvey",
        "name": "MarketSurvey 竞品价格追踪",
        "goal": "市场竞品追踪与价格观察：产品档案、价格观察记录、角色权限、内网 SQLite 或 Supabase 双模式。",
        "non_goals": [
            "不把内网 SQLite 模式误发布为无认证生产环境",
            "不在此任务完成 Supabase 云项目创建（HANDOFF 已标注未完成）",
        ],
        "scope": "Large",
        "path": r"D:\Development\MarketResearchTools\MarketSurvey",
        "recover_path": r"D:\Recover\Market",
        "stack": "Vite + React + Express API + SQLite/Supabase",
        "verify_auto": "corepack pnpm typecheck && corepack pnpm test",
        "verify_func": "Start.bat 启动 dev:lan，5300 网页与 API 代理正常",
        "must_pass": [
            "data/marketsurvey.sqlite 持久化读写",
            "uploads/ 图片上传与展示",
            "admin/reporter/viewer 三角权限符合 README",
            "corepack pnpm backup 生成 backups/ 目录",
            "生产 build 在未配置 Supabase 时阻止启动",
        ],
        "failure": [
            "Reporter 可审批他人记录（若违反业务口径）",
            "相似产品提醒自动合并（应仅提醒）",
            "局域网端口代理失败",
        ],
        "status": "Continue",
        "last_action": "Recover/Market 含 Next.js route manifest 碎片；MarketSurvey 本体在 Development 完整。",
        "next": "运行 Start.bat，验证 SQLite 模式与三角色 smoke flow。",
        "blocked": False,
    },
    {
        "root": r"D:\Development\VisualProjectManagement\VisualProjectScheduling",
        "id": "company_gantt",
        "name": "公司内部甘特图 (company-gantt)",
        "goal": "React + Vite 企业内部项目甘特排期：多项目/阶段/任务/工作 CRUD、依赖排期、资源负载、导出与 E2E 冒烟。",
        "non_goals": [
            "不在此轮完成 MULTI_USER_PLAN 全量多用户后端（除非 WORK_ORDER 另定）",
            "不从 Recover 损坏的 App.tsx 恢复源码",
        ],
        "scope": "Medium",
        "path": r"D:\Development\VisualProjectManagement\VisualProjectScheduling",
        "recover_path": r"D:\Recover\Visual",
        "stack": "React 18 + Vite 6 + Vitest + Playwright + optional SQLite API",
        "verify_auto": "npm.cmd test && npm.cmd run build",
        "verify_func": "npm.cmd run test:e2e -- --reporter=line",
        "must_pass": [
            "localStorage key company-gantt-v3 迁移正常",
            "依赖排期与工作日规则正确",
            "六视图切换与筛选同步",
            "导出 ICS/CSV/XLSX 菜单可用",
            "HANDOFF.md 列出的 E2E 场景可运行",
        ],
        "failure": [
            "拖拽排期后依赖链未重算",
            "关键路径识别错误",
            "1365px 布局严重溢出且无 workaround",
        ],
        "status": "Continue",
        "last_action": "Recover/Visual .env.example 含 COMPANY_GANTT_TOKEN；完整源码在 VisualProjectScheduling。",
        "next": "npm.cmd run dev:full 验证 API+前端；运行 test:e2e。",
        "blocked": False,
    },
    {
        "root": r"D:\Development\VisualProjectManagement\DiagramWeave-Public",
        "id": "diagramweave",
        "name": "DiagramWeave 流程图编辑器",
        "goal": "单机 Web/Electron 流程图编辑器：dagre 布局、导出 PDF/XLSX、离线 vendor 资源。",
        "non_goals": [
            "不改为云端协作多用户版本",
            "不合并 company-gantt 代码库",
        ],
        "scope": "Small",
        "path": r"D:\Development\VisualProjectManagement\DiagramWeave-Public",
        "recover_path": r"D:\Recover\Visual",
        "stack": "Vite + Electron + dagre + jspdf + xlsx",
        "verify_auto": "pnpm test && pnpm typecheck",
        "verify_func": "pnpm electron 或 pnpm serve 可打开编辑器",
        "must_pass": [
            "postinstall vendor:copy 与 font:download 成功",
            "vitest 单元测试通过",
            "playwright e2e 可运行（如已配置）",
            "PDF/XLSX 导出文件可打开",
        ],
        "failure": [
            "离线字体缺失导致 PDF 乱码",
            "dagre 布局崩溃",
        ],
        "status": "Continue",
        "last_action": "Visual 恢复区主要为 node_modules 碎片；DiagramWeave-Public 在 Development 完整。",
        "next": "pnpm setup && pnpm test，确认 electron 启动。",
        "blocked": False,
    },
    {
        "root": r"D:\Development\MiniApp_Hub",
        "id": "miniapp_hub",
        "name": "MiniApp Hub",
        "goal": "小程序/微系统 Hub：client、core-server、plugins、shared 模块化宿主，支持 docker 与 work 插件目录。",
        "non_goals": [
            "不在无明确 WORK_ORDER 时重写整个 Hub 架构",
        ],
        "scope": "Large",
        "path": r"D:\Development\MiniApp_Hub",
        "recover_path": r"D:\Recover",
        "stack": "Monorepo: client, core-server, plugins, docker, shared",
        "verify_auto": "按 Docs 或 package scripts 运行 test/build",
        "verify_func": "docker 或本地启动 core-server + client",
        "must_pass": [
            "README 与仓库结构一致",
            "core-server 可启动",
            "client 可连接 core-server",
            "plugins 目录可被加载或文档说明启用方式",
        ],
        "failure": [
            "Micro-System_Hub.zip 与当前代码不一致且无说明",
            "docker compose 无法启动",
        ],
        "status": "Continue",
        "last_action": "MiniApp_Hub 在 D 盘删除事件后仍完整。",
        "next": "阅读 Docs/ 与 docker/，运行最小 smoke 启动路径。",
        "blocked": False,
    },
    {
        "root": r"D:\Development\MyWork_Agent",
        "id": "mywork_agent",
        "name": "MyWork 个人本地 AI Agent",
        "goal": "按 mywork-design.md 重建本地优先 AI Agent：Loop Engineering、Privacy Gateway、WebBridge、@mywork/memory 与 @mywork/ui。",
        "non_goals": [
            "不做企业多租户 RBAC",
            "不在重建阶段把 ARK_API_KEY 写入仓库或聊天",
            "不从未损坏的 Recover 碎片猜测完整 monorepo 目录树",
        ],
        "scope": "Product",
        "path": r"D:\Development\MyWork_Agent",
        "recover_path": r"D:\Recover\MyWork",
        "stack": "规划：Rust/Tauri desktop + TS packages (@mywork/*) + OpenCode 风格 CMS",
        "verify_auto": "待 WORK_ORDER 定义后 cargo test / pnpm test",
        "verify_func": "MYWORK_UI=1 时 TaskContractPanel 可渲染",
        "must_pass": [
            "Docs/mywork-design.md 与 Docs/*_Workbuddy 一致",
            "packages/memory 本地 RAG 不上云",
            "packages/ui 绑定 GET /mywork/cms/session/:sessionId",
            "Privacy Gateway 脱敏后再调用云模型",
            "Agent Loop PLAN→EXECUTE→VERIFY→ADAPT 状态机可观测",
        ],
        "failure": [
            "文档上传未脱敏直送云端",
            "invoke 手动调用而非 bindings.ts",
            "Loop 无 VERIFY 阶段即标记 Done",
        ],
        "status": "Blocked",
        "last_action": "源码目录已删，仅 Docs/mywork-design.md + .git 残留；Recover/MyWork 有 @mywork/* README 片段。",
        "next": "人类确认重建范围：先 scaffold packages/memory + packages/ui，或从 git/远程恢复。",
        "blocked": True,
        "block_reason": "源码缺失；需确认是否从 git objects 或远程仓库恢复。",
    },
    {
        "root": r"D:\Development\ProjectManagement",
        "id": "project_management",
        "name": "ProjectManagement 占位恢复",
        "goal": "恢复 ProjectManagement 目录：对接 company-gantt 或多用户甘特后端。",
        "non_goals": [
            "不将 Recover 根目录 36 万 flat 文件手工搬回",
        ],
        "scope": "Medium",
        "path": r"D:\Development\ProjectManagement",
        "recover_path": r"D:\Recover\ProjectManagement",
        "stack": "待定：可 fork VisualProjectScheduling 或独立后端",
        "verify_auto": "TBD after scaffold",
        "verify_func": "TBD after scaffold",
        "must_pass": [
            "目录非空且有 README",
            "与 VisualProjectScheduling 关系文档化",
            "Docs/*_Workbuddy 与 TARGET 对齐",
        ],
        "failure": [
            "空目录长期无 scaffold",
            "与 company-gantt 重复建设无文档",
        ],
        "status": "Blocked",
        "last_action": "D:\\Development\\ProjectManagement 为空；Recover 下仅有 company-gantt/node_modules。",
        "next": "决定：fork VisualProjectScheduling 还是新建后端 API 项目。",
        "blocked": True,
        "block_reason": "目标架构未确认；目录为空。",
    },
    {
        "root": r"D:\Development\EduCore",
        "id": "educore",
        "name": "EduCore 光合啟途",
        "goal": "乡村教育 AI 自适应学习平台：BKT/IRT/SM-2 算法驱动的题目难度调整与温暖非评判 UX。",
        "non_goals": [
            "不在此 WORK_ORDER 混合 MyWork Agent 代码",
        ],
        "scope": "Product",
        "path": r"D:\Development\EduCore",
        "recover_path": "N/A",
        "stack": "AI adaptive learning platform（见 EduCore README）",
        "verify_auto": "项目定义 test/build 命令",
        "verify_func": "学习者 smoke flow，自适应推题正常",
        "must_pass": [
            "README 核心理念与实现一致",
            "自适应算法模块有测试覆盖",
            "无评判 UX 文案规范遵守",
        ],
        "failure": [
            "题目难度不随掌握度变化",
            "用户数据未本地化/未脱敏上云策略违反设计",
        ],
        "status": "Continue",
        "last_action": "EduCore 在 D:\\Development 存在；未在 Recover 子目录单独映射。",
        "next": "盘点 EduCore 仓库完整度并运行现有 test/build。",
        "blocked": False,
    },
]


def render_target(p: dict) -> str:
    ng = "\n".join(f"- {x}" for x in p["non_goals"])
    return f"""Status: Confirmed

# Project Target — {p['name']}

## User Goal

{p['goal']}

## Success Criteria

- 项目在 `{p['path']}` 可构建、可启动、核心业务流程可验证
- Agent Loop 状态文件齐全且可通过 agent-loop-check.ps1（Done 前使用 -Strict）
- 灾难恢复后 SQLite/uploads 完整或迁移路径已文档化

## Non-Goals

{ng}

## Current Scope

{p['scope']}

## Stack & Paths

- **Canonical path:** `{p['path']}`
- **Recover reference:** `{p['recover_path']}`
- **Stack:** {p['stack']}

## Human Decisions Required

- D 盘删除事件后是否轮换已泄露密钥（Recover 中曾出现 API key 片段）
- MyWork / ProjectManagement 重建范围与优先级

## Last Confirmed

{DATE}
"""


def render_acceptance(p: dict) -> str:
    mp = "\n".join(
        f"- [ ] {x}\n  Evidence required: automatic + functional\n  Current evidence: pending verification"
        for x in p["must_pass"]
    )
    fe = "\n".join(f"- {x}" for x in p["failure"])
    return f"""# Acceptance Contract — {p['name']}

## Must Pass

{mp}

## Evidence Required

Automatic:

- `{p['verify_auto']}`

Functional:

- {p['verify_func']}

## Failure Examples

{fe}

## Known Exclusions

- Recover 区损坏的 null-byte 源码文件不作为验收依据
- node_modules 碎片文件不计入项目完整性

## Manual Confirmation Needed

- [ ] 人类确认生产/内网部署模式（SQLite vs Supabase vs local-cloud）
  Reason: 环境相关，Agent 不得擅自访问生产密钥
"""


def render_loop_state(p: dict) -> str:
    blocked = p.get("blocked", False)
    status = p["status"]
    sr = "Yes" if blocked else "No"
    reason = p.get("block_reason", "None") if blocked else "None"
    result = (
        "Blocked pending human decision"
        if blocked
        else "Source tree present under Development; verification pending"
    )
    return f"""# Loop State — {p['name']}

## Status

{status}

## Last Action

{p['last_action']}

## Evidence

Command: Recover inventory scan + Development path audit ({DATE})

Result: {result}

Exit code: N/A (documentation bootstrap)

Functional check: Pending — run project-specific verification in ACCEPTANCE_Workbuddy.md

Logs / screenshots / files:

- `D:\\Recover\\FINAL_RECOVERY_SCAN_2026-06-16.md` (if present)
- `{p['path']}`

## Failed Checks

None (bootstrap only)

## Root Cause

None

## Next Action

{p['next']}

## Stop Rule Triggered

{sr}

Reason: {reason}
"""


def render_log(p: dict) -> str:
    entry = {
        "timestamp": NOW,
        "event": "loop_end",
        "agent": "WorkBuddy",
        "scenario_guess": "Disaster recovery bootstrap",
        "skill_used": "agent-loop-engineering",
        "templates_used": [
            "TARGET_Workbuddy.md",
            "ACCEPTANCE_Workbuddy.md",
            "LOOP_STATE_Workbuddy.md",
            "LOOP_LOG_Workbuddy.jsonl",
        ],
        "project_id": p["id"],
        "files_read": [p["path"], p["recover_path"]],
        "files_written": [
            "Docs/TARGET_Workbuddy.md",
            "Docs/ACCEPTANCE_Workbuddy.md",
            "Docs/LOOP_STATE_Workbuddy.md",
            "Docs/LOOP_LOG_Workbuddy.jsonl",
        ],
        "commands": [],
        "verification_commands": [],
        "evidence": [f"bootstrap:{DATE}"],
        "checker_result": "Not run",
        "verified_at": NOW,
        "code_size": {
            "size_class": "Unknown",
            "code_files": 0,
            "code_lines": 0,
            "changed_files": "Docs only",
        },
        "notes": (
            f"CMS Lite bootstrap for {p['name']}. Status={p['status']}. "
            "Do not mark Done until ACCEPTANCE checks pass."
        ),
    }
    return json.dumps(entry, ensure_ascii=False)


def main() -> None:
    created: list[str] = []
    for p in PROJECTS:
        docs = Path(p["root"]) / "Docs"
        docs.mkdir(parents=True, exist_ok=True)
        files = {
            "TARGET_Workbuddy.md": render_target(p),
            "ACCEPTANCE_Workbuddy.md": render_acceptance(p),
            "LOOP_STATE_Workbuddy.md": render_loop_state(p),
            "LOOP_LOG_Workbuddy.jsonl": render_log(p) + "\n",
        }
        for name, content in files.items():
            path = docs / name
            path.write_text(content, encoding="utf-8")
            created.append(str(path))
    print(f"Created {len(created)} files")
    for c in created:
        print(c)


if __name__ == "__main__":
    main()
