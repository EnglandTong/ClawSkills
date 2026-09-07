#!/usr/bin/env bash
# preflight.sh — 发布前自动校验（ClawHub / GitHub / 跨平台索引）
#
# 用法：
#   bash scripts/preflight.sh          # 全量检查
#   bash scripts/preflight.sh --quiet  # 只打印失败项
#
# 退出码：0 = 全部通过；1 = 存在失败项
#
# 检查项（前三项是历史事故的直接来源）：
#   1. 版本号五处同步   SKILL.md / _meta.json / skill.json / sitemap.xml / SECURITY.md
#   2. plugin 内嵌副本  skills/<name> 与 plugins/ai-engineering-expert/skills/<name> 零差异
#   3. 干净扫描         邮箱 / 本机绝对路径 / 手机号（排除已知误报源）
#   4. frontmatter      name == 目录名；description 无「冒号+空格」、不以冒号结尾
#   5. QUICKSTART       必备字段（安装命令 + 触发语 + 可验证输出）
#   6. plugin manifest  4 份清单版本号一致
#
# 注意：不要用 PyYAML 校验 frontmatter（该环境已不可用），本脚本只做字符串判断。

set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT" || exit 1

QUIET=0
[[ "${1:-}" == "--quiet" ]] && QUIET=1

FAIL=0
pass() { [[ $QUIET -eq 0 ]] && printf '  \033[32mPASS\033[0m  %s\n' "$1"; return 0; }
fail() { printf '  \033[31mFAIL\033[0m  %s\n' "$1"; FAIL=$((FAIL + 1)); return 0; }
warn() { printf '  \033[33mWARN\033[0m  %s\n' "$1"; return 0; }
head2() { printf '\n\033[1m%s\033[0m\n' "$1"; }

SKILLS=(agent-loop-engineering cms-project-governance daily-workflow web-search-rules ai-workflow-os project-lifecycle-navigator)
PLUGIN="plugins/ai-engineering-expert"

# 从文件里抽取版本号的统一函数
ver_skill()    { grep -m1 -i "^Version:" "skills/$1/SKILL.md" 2>/dev/null | sed 's/.*: *//; s/[[:space:]]*$//' | tr -d '\r'; }
ver_meta()     { grep -m1 -o '"version"[[:space:]]*:[[:space:]]*"[^"]*"' "skills/$1/_meta.json" 2>/dev/null | sed 's/.*"\([^"]*\)"$/\1/'; }
ver_skilljson(){ grep -m1 -o '"version"[[:space:]]*:[[:space:]]*"[^"]*"' "skills/$1/skill.json" 2>/dev/null | sed 's/.*"\([^"]*\)"$/\1/'; }
ver_sitemap()  { grep -o '<skill:version>[^<]*' "skills/$1/sitemap.xml" 2>/dev/null | head -1 | sed 's/.*>//'; }
ver_sec()      { grep -m1 -i "^Version:" "skills/$1/SECURITY.md" 2>/dev/null | sed 's/.*: *//; s/[[:space:]]*$//' | tr -d '\r'; }

# ────────────────────────────────────────────────────────────
head2 "1. 版本号五处同步"
for s in "${SKILLS[@]}"; do
  vs="$(ver_skill "$s")"
  [[ -z "$vs" ]] && { fail "$s: SKILL.md 找不到 Version 行"; continue; }
  drift=0
  for pair in "_meta.json:$(ver_meta "$s")" "skill.json:$(ver_skilljson "$s")" \
              "sitemap.xml:$(ver_sitemap "$s")" "SECURITY.md:$(ver_sec "$s")"; do
    file="${pair%%:*}"; fv="${pair#*:}"
    [[ -z "$fv" ]] && continue                      # 文件不存在则跳过
    if [[ "$fv" != "$vs" ]]; then
      fail "$s: $file 版本 $fv != SKILL.md 的 $vs"
      drift=1
    fi
  done
  [[ $drift -eq 0 ]] && pass "$s  v$vs 五处一致"
done

# ────────────────────────────────────────────────────────────
head2 "2. plugin 内嵌副本一致性（内嵌副本必须与 skills/ 逐文件相同）"
for s in agent-loop-engineering cms-project-governance; do
  if [[ ! -d "$PLUGIN/skills/$s" ]]; then
    fail "$s: plugin 内嵌副本不存在"
    continue
  fi
  out="$(diff -rq "skills/$s" "$PLUGIN/skills/$s" 2>&1)"
  if [[ -z "$out" ]]; then
    pass "$s 内嵌副本零差异"
  else
    fail "$s 内嵌副本存在差异："
    echo "$out" | sed 's/^/         /'
  fi
done

# ────────────────────────────────────────────────────────────
head2 "3. 干净扫描（公开索引前必过）"
# 3a 邮箱
hits="$(grep -rEn "[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}" skills plugins --include='*.md' --include='*.json' --include='*.mjs' 2>/dev/null \
        | grep -v 'clawhub.ai' | head -5)"
[[ -z "$hits" ]] && pass "无邮箱" || { fail "发现邮箱："; echo "$hits" | sed 's/^/         /'; }

# 3b 本机绝对路径
hits="$(grep -rFn -e 'D:\Development' -e 'C:\Users' -e '/Users/' -e '/home/' skills plugins 2>/dev/null | head -5)"
[[ -z "$hits" ]] && pass "无本机绝对路径" || { fail "发现本机路径："; echo "$hits" | sed 's/^/         /'; }

# 3c 手机号（排除 _meta.json：其 publishedAt 毫秒时间戳会误报）
hits="$(grep -rEn "(^|[^0-9])1[3-9][0-9]{9}([^0-9]|$)" skills plugins --include='*.md' --include='*.mjs' --include='*.json' 2>/dev/null \
        | grep -v '_meta.json' | head -5)"
[[ -z "$hits" ]] && pass "无手机号" || { warn "疑似手机号（人工确认是否为时间戳误报）："; echo "$hits" | sed 's/^/         /'; }

# 3d 陈旧发布包（src 目录里不该有 zip）
hits="$(find skills -maxdepth 2 -name '*.zip' 2>/dev/null | head -5)"
[[ -z "$hits" ]] && pass "skills/ 下无陈旧 zip" || { fail "发现陈旧 zip（索引器会误读为正式内容）："; echo "$hits" | sed 's/^/         /'; }

# ────────────────────────────────────────────────────────────
head2 "4. frontmatter 合法性（YAML 明文标量）"
for s in "${SKILLS[@]}"; do
  f="skills/$s/SKILL.md"
  desc="$(sed -n '3p' "$f")"
  name="$(sed -n '2p' "$f" | sed 's/^name: *//' | tr -d '\r')"
  ok=1
  [[ "$name" != "$s" ]] && { fail "$s: frontmatter name='$name' 与目录名不一致"; ok=0; }
  # description 内含「冒号+空格」会让 YAML 明文标量解析失败（跳过行首的 "description:"）
  if echo "$desc" | sed 's/^description: *//' | grep -q ': '; then
    fail "$s: description 含「冒号+空格」，YAML 会解析失败"; ok=0
  fi
  echo "$desc" | grep -qE ':\s*$' && { fail "$s: description 以冒号结尾"; ok=0; }
  echo "$desc" | sed 's/^description: *//' | grep -qE '^[^A-Za-z0-9 ]' && { fail "$s: description 以特殊字符开头"; ok=0; }
  [[ $ok -eq 1 ]] && pass "$s frontmatter 合法"
done

# ────────────────────────────────────────────────────────────
head2 "5. QUICKSTART 必备字段"
for s in "${SKILLS[@]}"; do
  f="skills/$s/QUICKSTART.md"
  if [[ ! -f "$f" ]]; then fail "$s: 缺 QUICKSTART.md"; continue; fi
  ok=1
  grep -q "install" "$f"        || { fail "$s: QUICKSTART 缺安装命令"; ok=0; }
  grep -qE "Try it|验证" "$f"    || { fail "$s: QUICKSTART 缺可验证输出章节"; ok=0; }
  [[ $ok -eq 1 ]] && pass "$s QUICKSTART 完整"
done

# ────────────────────────────────────────────────────────────
head2 "6. plugin 四份 manifest 版本一致"
pv=""
for f in "$PLUGIN/package.json" "$PLUGIN/openclaw.plugin.json" "$PLUGIN/.claude-plugin/plugin.json" "$PLUGIN/.qoder-plugin/plugin.json"; do
  if [[ ! -f "$f" ]]; then fail "缺 manifest: $f"; continue; fi
  cur="$(grep -m1 -o '"version"[[:space:]]*:[[:space:]]*"[^"]*"' "$f" | sed 's/.*"\([^"]*\)"$/\1/')"
  [[ -z "$pv" ]] && pv="$cur"
  if [[ "$cur" == "$pv" ]]; then
    pass "$(basename "$(dirname "$f")")/$(basename "$f")  v$cur"
  else
    fail "$f 版本 $cur != $pv"
  fi
done

# ────────────────────────────────────────────────────────────
printf '\n'
if [[ $FAIL -eq 0 ]]; then
  printf '\033[32m全部检查通过\033[0m，可以发布。\n'
  exit 0
else
  printf '\033[31m%d 项未通过\033[0m，修复后再发布。\n' "$FAIL"
  exit 1
fi
