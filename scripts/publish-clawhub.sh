#!/usr/bin/env bash
# ClawHub 发布脚本 —— 参数固化的唯一真源
#
# 为什么必须有这个脚本：
#   clawhub publish 的 --tags 默认值是 "latest"。只要发布时忘了带 --tags，
#   该 listing 的历史 tags 会被覆盖成只剩 "latest"。
#   coding-management-system 现在只剩 1 个 tag，就是这么丢的。
#   --topics 同理，不传即为空。
#   => 以后发布一律走本脚本，不要手敲 clawhub publish。
#
# 用法：
#   bash scripts/publish-clawhub.sh --dry-run        # 预览，默认行为
#   bash scripts/publish-clawhub.sh --yes            # 真正发布
#   bash scripts/publish-clawhub.sh --yes --only web-search-rules
#
# 前置：npx clawhub@latest login   （本机当前未装 clawhub CLI）

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$ROOT/skills"
DRY=1
ONLY=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --yes)   DRY=0; shift ;;
    --only)  ONLY="${2:-}"; shift 2 ;;
    --dry-run) DRY=1; shift ;;
    *) echo "未知参数: $1"; exit 1 ;;
  esac
done

# 可用 CLAWHUB_CLI 环境变量覆盖（本机装了 clawhub 就设成 clawhub，
# 自测时可设成 echo）。
CLI="${CLAWHUB_CLI:-npx --yes clawhub@latest}"

# slug | 源目录 | 版本 | topics | tags
# 注意 cms-project-governance 的 ClawHub slug 是 coding-management-system，
# 这是历史遗留，不能改（改名会断所有已安装用户的更新链）。
publish_one() {
  local slug="$1" dir="$2" ver="$3" topics="$4" tags="$5" changelog="$6"
  [[ -n "$ONLY" && "$slug" != "$ONLY" && "$dir" != "$ONLY" ]] && return 0

  echo "--------------------------------------------------------------"
  echo "  $slug  v$ver"
  echo "  from   skills/$dir"
  echo "  topics $topics"
  echo "  tags   $(echo "$tags" | tr ',' ' ' | wc -w) 个"
  echo "--------------------------------------------------------------"

  local -a args=(
    publish "$SKILLS_DIR/$dir"
    --slug "$slug"
    --version "$ver"
    --topics "$topics"
    --tags "$tags"
    --changelog "$changelog"
  )
  [[ $DRY -eq 1 ]] && args+=(--dry-run)

  $CLI "${args[@]}" || {
    echo "!! $slug 发布失败，停止（后续 listing 未动）"
    return 1
  }
  echo
}

# ---- 1. web-search-rules（主推）----
publish_one "web-search-rules" "web-search-rules" "4.1.0" \
  "Web Search,Knowledge Base,Obsidian,Feishu,研究" \
  "latest,web-search,search,research,knowledge-base,obsidian,notebooklm,ima,feishu,tencent-docs,source-governance,source-filtering,audit-log,whitelist,blacklist,url-rules,staging,fact-check,claim-verification,security,bilingual,chinese,english,zh-cn,en" \
  "Rewrite the opening line to state a concrete result. Add QUICKSTART.md with install command, a 30-second verification and a minimum-usable path. Add untrusted-metadata and single-source rules."

# ---- 2. daily-workflow（主推）----
publish_one "daily-workflow" "daily-workflow" "4.1.0" \
  "Handoff,Project Memory,Docs,工作流,记忆" \
  "latest,project-memory,handoff,ai-handoff,ai-handover,checkpoint,wrap-up,context-management,context-compression,daily-routine,daily-standup,daily-workflow,work-session,project-management,productivity,documentation,bilingual,chinese,english,zh-cn,en" \
  "Rewrite the opening line to lead with the trigger phrase. Add QUICKSTART.md covering the four phrases and the two-file lightweight profile. Add memory-bloat control and backup-before-restructure rules."

# ---- 3. coding-management-system（cms-project-governance，进阶/依赖）----
publish_one "coding-management-system" "cms-project-governance" "2.2.0" \
  "Project Governance,Project Management,Requirements,QA Acceptance,项目治理" \
  "latest,project-governance,requirements-analysis,goal-alignment,qa-acceptance,token-efficiency,scope-control,rebaseline,project-management,ai-coding-agent,milestone,work-order,legacy-bootstrap,drift-recovery,bilingual,chinese,english,zh-cn,en" \
  "Add anti-involution controls, active-document budget, rebaseline-by-append rule and unlock conditions for Accepted With Risk. Add QUICKSTART.md. Restore the full tag set that was lost to the default latest-only publish."

# ---- 4. agent-loop-engineering（进阶/依赖）----
publish_one "agent-loop-engineering" "agent-loop-engineering" "2.2.0" \
  "AI Coding,Autonomous Agents,Software Testing,Context Management" \
  "latest,ai-coding,autonomous-agents,bounded-autonomy,agent-loop,acceptance-testing,context-management,execution-loops,software-testing,coding-agent,automation,resumable,handoff,project-governance,cms,ai-coding-agent,bilingual,chinese,english,zh-cn,en" \
  "Add stall rule, deterministic-path guard, gates-a-human-must-perform downgrade and the evidence downgrade ban. Add QUICKSTART.md. Restore the topic list that was empty on this listing."

# ---- 5. ai-workflow-os（路由）----
publish_one "ai-workflow-os" "ai-workflow-os" "2.1.0" \
  "Orchestration,Workflow,Research,工作流" \
  "latest,ai-workflow,orchestration,router,project-management,research-governance,knowledge-base,source-filtering,web-search,handoff,project-memory,audit-log,bilingual,chinese,english,zh-cn,en" \
  "Add scope collapse guard. Add QUICKSTART.md."

# ---- 6. project-lifecycle-navigator ----
publish_one "project-lifecycle-navigator" "project-lifecycle-navigator" "2.1.0" \
  "Code Review,MVP,Project Management,项目" \
  "latest,project-management,product-management,mvp,code-review,ai-coding-agent,project-audit,rebaseline,scope-control,bilingual,chinese,english,zh-cn,en" \
  "Add startup gates, go/no-go score, pre-commit stop-loss and a repository structural-defect checklist. Add QUICKSTART.md."

if [[ $DRY -eq 1 ]]; then
  echo
  echo "以上是 --dry-run 预览，没有发布任何内容。"
  echo "确认无误后执行： bash scripts/publish-clawhub.sh --yes"
  echo "发布前请先登录： npx --yes clawhub@latest login"
fi
