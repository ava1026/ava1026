# -*- coding: utf-8 -*-
"""生成 FOMO 增长闭环页面（四张手绘 SVG + 说明）"""

def defs(pfx):
    return f'''<defs>
<marker id="{pfx}a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--muted)"/></marker>
<marker id="{pfx}b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--accent)"/></marker>
<marker id="{pfx}c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--hot)"/></marker>
<marker id="{pfx}d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--ours)"/></marker>
</defs>'''

def box(x, y, w, h, cls="dg-box"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" class="{cls}"/>'

def txt(x, y, s, cls="dg-t", anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">{s}</text>'


# ══════════════════════════ 图一：主飞轮 ══════════════════════════
def fig1():
    P = "f1"
    W, H = 960, 592
    BW, BH = 240, 78
    xs = [30, 360, 690]
    ty, by = 110, 380
    tcy, bcy = ty + BH/2, by + BH/2
    o = [f'<svg class="dg" role="img" viewBox="0 0 {W} {H}" '
         f'aria-label="FOMO 增长主飞轮：零门槛进人 → 首笔交易 → 交易自动进 Feed → 赚钱效应被看见 → 跟单与推送放大 → 笔数与收入 → 现金回投获客，闭环回到起点；沿途标出四个漏损点">',
         defs(P)]

    stages = [
        # (序号, x, y, 主标题, 副标题)
        ("①", xs[0], ty, "零门槛进人",      "Apple Pay · USDC 统一余额 · gas 全代付"),
        ("②", xs[1], ty, "首笔交易达成",    "一键买全网 · 跨链无感 · 3s"),
        ("③", xs[2], ty, "交易自动进 Feed", "Leaderboard / Thesis / Profile"),
        ("④", xs[2], by, "赚钱效应被看见",  "谁在赚、赚多少，公开可查"),
        ("⑤", xs[1], by, "跟单 + 推送放大", "callout 20/40/80 档 · GME 一天 11 次"),
        ("⑥", xs[0], by, "笔数 × 费率 = 收入", "128k 笔/日 × ≈$0.76/笔"),
    ]
    for n, x, y, t, s in stages:
        o.append(box(x, y, BW, BH))
        o.append(txt(x + 14, y + 20, n, "dg-n", "start"))
        o.append(txt(x + BW/2, y + 38, t))
        o.append(txt(x + BW/2, y + 60, s, "dg-s"))

    # 顺时针的六条边
    def harrow(x1, x2, y, label, hot=False, sub=None):
        m = f"{P}b" if hot else f"{P}a"
        c = "dg-edge dg-edge-hot" if hot else "dg-edge"
        lc = "dg-lab-hot" if hot else "dg-lab"
        o.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" class="{c}" marker-end="url(#{m})"/>')
        mx = (x1 + x2) / 2
        o.append(txt(mx, y - (26 if sub else 14), label, lc))
        if sub:
            o.append(txt(mx, y - 10, sub, "dg-s"))

    harrow(270, 354, tcy, "摩擦≈0", sub="转化率极高")
    harrow(600, 684, tcy, "交易即内容", hot=True, sub="零成本 UGC")

    # 中心：闭环转速注解
    o.append(txt(480, 262, "闭环周期 ≈ 分钟级", "dg-h"))
    o.append(txt(480, 286, "推送把「转一圈」的时间从天压缩到分钟", "dg-s"))
    harrow(684, 600, bcy, "情绪触发")          # ④→⑤ 向左
    harrow(354, 270, bcy, "更多人下单")        # ⑤→⑥ 向左

    # ③→④ 右侧向下
    o.append(f'<line x1="810" y1="{ty+BH}" x2="810" y2="{by-6}" class="dg-edge" marker-end="url(#{P}a)"/>')
    o.append(txt(826, 258, "内容把", "dg-lab", "start"))
    o.append(txt(826, 276, "赚钱效应", "dg-lab", "start"))
    o.append(txt(826, 294, "推到人前", "dg-lab", "start"))

    # ⑥→① 左侧向上
    o.append(f'<line x1="150" y1="{by}" x2="150" y2="{ty+BH+6}" class="dg-edge" marker-end="url(#{P}a)"/>')
    o.append(txt(134, 258, "现金回投", "dg-lab", "end"))
    o.append(txt(134, 276, "KOL / 折扣", "dg-lab", "end"))
    o.append(txt(134, 294, "/ 入金补贴", "dg-lab", "end"))

    # 漏损点
    def leak(cx, up, lines):
        y1 = ty if up else by + BH
        y2 = y1 - 38 if up else y1 + 38
        o.append(f'<line x1="{cx}" y1="{y1}" x2="{cx}" y2="{y2}" class="dg-edge dg-leak" marker-end="url(#{P}c)"/>')
        base = y2 - 12 - 16 * (len(lines) - 1) if up else y2 + 20
        for i, l in enumerate(lines):
            o.append(txt(cx, base + i * 16, l, "dg-leak-t"))

    leak(xs[1] + BW/2, True,  ["漏损：≤200U 固定 0.95U/笔", "对 <$95 小额不友好 · BNB 不填充"])
    leak(xs[2] + BW/2, True,  ["漏损：KOL listing 偏袒争议", "排行榜公信力受损"])
    leak(xs[2] + BW/2, False, ["漏损：跟单者成为退出流动性"])
    leak(xs[0] + BW/2, False, ["漏损：出金要跳去 Spritz", "提现是投诉最集中区"])

    o.append("</svg>")
    return "\n".join(o)


# ══════════════════════════ 图二：四条加速支路 ══════════════════════════
def fig2():
    P = "f2"
    W, H = 960, 680
    BW, BH = 250, 62
    xs = [30, 340, 650]
    PITCH = 158
    rows = [
        ("推荐分润回路", [
            ["用户绑定推荐码（省 10%）"],
            ["每笔卖出实时分 25%", "无上限、实时到账"],
            ["用户自己变成推广者"],
        ], "≈29% 的手续费来自绑定了推荐人的用户"),
        ("KOL / CLANS 回路", [
            ["KOL 获 listing 优先", "+ sponsored 曝光"],
            ["粉丝在排行榜", "看到 KOL 真实持仓"],
            ["跟单成交 → KOL 沉淀观众"],
        ], "CLANS 让 KOL 把观众变成可累积资产 → 更难离开"),
        ("原生红人孵化回路　← X 数据新增，最强的一条", [
            ["X 素人公开交易 + Thesis", "（@wwayfboss X 仅 752 粉）"],
            ["爬 Leaderboard", "→ 官方点名庆祝"],
            ["站内粉丝 8k–23k", "影响力只在 FOMO 内有效"],
        ], "红人带来跟单者，跟单者又成为下一批候选红人 —— 且影响力迁不走"),
        ("资本回路", [
            ["交易量 / 用户数连创新高"],
            ["$550M 估值", "累计 $94M 到账"],
            ["现金补贴费率 / KOL / 入金"],
        ], "融资叙事本身成为获客预算的来源"),
    ]
    o = [f'<svg class="dg" role="img" viewBox="0 0 {W} {H}" '
         f'aria-label="四条加速支路：推荐分润回路、KOL 与 CLANS 回路、原生红人孵化回路、资本回路，各自自我强化后注入主飞轮">',
         defs(P)]

    for ri, (name, nodes, ret) in enumerate(rows):
        y = 44 + ri * PITCH
        o.append(txt(30, y - 14, name, "dg-h", "start"))
        for ci, n in enumerate(nodes):
            x = xs[ci]
            o.append(box(x, y, BW, BH, "dg-box-soft"))
            if len(n) == 1:
                o.append(txt(x + BW/2, y + 37, n[0], "dg-t2"))
            else:
                for li, ln in enumerate(n):
                    o.append(txt(x + BW/2, y + 26 + li * 20, ln, "dg-t2"))
            if ci < 2:
                x1, x2 = x + BW, xs[ci + 1] - 6
                o.append(f'<line x1="{x1}" y1="{y+BH/2}" x2="{x2}" y2="{y+BH/2}" class="dg-edge" marker-end="url(#{P}a)"/>')
        # 回流弧
        sx, ex = xs[2] + BW/2, xs[0] + BW/2
        dip = y + BH + 40
        o.append(f'<path d="M {sx} {y+BH} C {sx} {dip}, {ex} {dip}, {ex} {y+BH+6}" '
                 f'class="dg-edge dg-edge-loop" marker-end="url(#{P}d)"/>')
        # 标签置于弧线最低点之下，避免压线
        o.append(txt((sx + ex) / 2, y + BH + 56, ret, "dg-lab-loop"))

    o.append("</svg>")
    return "\n".join(o)


# ══════════════════════════ 图三：获客侧思维导图 ══════════════════════════
def fig3():
    P = "f3"
    branches = [
        ("付费 / 合作投放", "买注意力", [
            "链官方号造势：@BNBCHAIN 3.9M · @base 1M",
            "日常 KOL 10k–400k，多为 Coinbase 系",
            "2k–10k 小号专职做增长（含创始人本人）",
            "★ X Affiliation Badge：认证挂在 KOL 自己主页，零成本长期曝光",
            "★ 2026.7–8 外部 KOL 转为主动加入：@orangie 377k · @EricCryptoman 267k",
        ]),
        ("社交裂变", "让用户互相拉 · 更是造人", [
            "Friends：邀好友一起交易",
            "Feed：每笔交易自动成为内容",
            "Leaderboard：造星，制造可跟随对象",
            "CLANS（8/10 上线，50+）：组队、共建受众",
            "★ 原生红人孵化：X 素人在站内涨到 8k–23k 粉（born on fomo）",
            "★ 官方点名庆祝作为激励货币：涨粉 / Leaderboard 里程碑",
            "★ 社交跟单：Follow → 通知 → 手动跟单买入",
        ]),
        ("联盟裂变", "买增长，按效果付费", [
            "邀请码 10% 终身手续费折扣",
            "卖出侧 25% 实时分润，无上限",
            "SEO 套利者虚标 90% / 95% 折扣（官方仅 10%）",
            "★ 红人自带 referral：@hdegrootvan 用 stimmy / 福利做转化",
            "实测：约 29% 手续费来自绑定推荐人的用户",
        ]),
        ("产品即获客", "删摩擦", [
            "Apple Pay 直接买币 → 68,000 首次买币用户 / $25M",
            "USDC 单一余额，跨 4–5 条链无感",
            "gas 全代付，无需持有任何原生代币",
            "★ Thesis：每笔交易附逻辑，把交易变成可验证的内容资产",
            "极简 UI，App Store 4.6★",
        ]),
        ("唤醒与复购", "缩短闭环周期", [
            "热门代币推送：20 / 40 / 80 traders 档位",
            "单日最高 23 条，GME 一天推 11 次",
        ]),
    ]
    LW, LH, LGAP = 470, 34, 7
    BX, BW2, BH2 = 232, 190, 52
    LX = 452
    o_rows, y = [], 24
    for name, tag, leaves in branches:
        h = len(leaves) * (LH + LGAP) - LGAP
        o_rows.append((name, tag, leaves, y, y + h / 2))
        y += h + 34
    H = y + 10
    W = LX + LW + 20

    o = [f'<svg class="dg" role="img" viewBox="0 0 {W} {H}" '
         f'aria-label="FOMO 获客方式思维导图：付费投放、产品即获客、联盟裂变、社交裂变、唤醒复购五类渠道及其具体手段">',
         defs(P)]
    root_cy = (o_rows[0][4] + o_rows[-1][4]) / 2
    o.append(box(16, root_cy - 34, 150, 68, "dg-box-root"))
    o.append(txt(91, root_cy - 6, "FOMO 获客", "dg-t"))
    o.append(txt(91, root_cy + 16, "五条并行通道", "dg-s"))

    for name, tag, leaves, ty0, bcy in o_rows:
        o.append(f'<path d="M 166 {root_cy} C 200 {root_cy}, 198 {bcy}, {BX} {bcy}" class="dg-edge dg-edge-thin"/>')
        o.append(box(BX, bcy - BH2/2, BW2, BH2, "dg-box-accent"))
        o.append(txt(BX + BW2/2, bcy - 4, name, "dg-t"))
        o.append(txt(BX + BW2/2, bcy + 16, tag, "dg-s"))
        for i, l in enumerate(leaves):
            ly = ty0 + i * (LH + LGAP)
            lcy = ly + LH/2
            o.append(f'<path d="M {BX+BW2} {bcy} C {LX-28} {bcy}, {LX-28} {lcy}, {LX} {lcy}" class="dg-edge dg-edge-thin"/>')
            o.append(box(LX, ly, LW, LH, "dg-box-soft"))
            o.append(txt(LX + 14, lcy + 5, l, "dg-t2", "start"))
    o.append("</svg>")
    return "\n".join(o)


# ══════════════════ 图四：影响力发生器（X 粉丝 vs FOMO 粉丝）══════════════════
def fig4():
    P = "f4"
    # (账号, X 粉丝, 倍数, FOMO 粉丝是否为自报)
    rows = [
        ("@wwayfboss",   752, 27.0, False),
        ("@octoseaa",   2636,  5.1, False),
        ("@hdegrootvan",7943,  2.9, True),
        ("@f4vel",      3055,  2.7, False),
        ("@thokani",    8073,  2.0, False),
    ]
    LX, BX, BWMAX = 150, 168, 500
    RH, BARH = 60, 17
    top = 68
    H = top + len(rows) * RH + 96
    W = 940
    mx = max(x * m for _, x, m, _ in rows)
    k = BWMAX / mx

    o = [f'<svg class="dg" role="img" viewBox="0 0 {W} {H}" '
         f'aria-label="五位被官方点名的原生交易员，X 粉丝与 FOMO 粉丝对比：X 粉丝跨度 10.7 倍，FOMO 粉丝跨度仅 2.8 倍，离散度塌缩">',
         defs(P)]
    o.append(txt(BX, 30, "X 粉丝", "dg-s", "start"))
    o.append(f'<rect x="{BX+52}" y="21" width="26" height="10" rx="2" class="dg-bar-x"/>')
    o.append(txt(BX + 96, 30, "FOMO 粉丝", "dg-s", "start"))
    o.append(f'<rect x="{BX+168}" y="21" width="26" height="10" rx="2" class="dg-bar-f"/>')
    o.append(txt(W - 20, 30, "放大倍数", "dg-s", "end"))
    o.append(f'<line x1="{BX}" y1="46" x2="{W-20}" y2="46" class="dg-edge-thin"/>')

    for i, (name, xf, m, self_rep) in enumerate(rows):
        y = top + i * RH
        ff = xf * m
        o.append(txt(LX, y + 22, name, "dg-t2", "end"))
        o.append(f'<rect x="{BX}" y="{y}" width="{max(2,round(xf*k))}" height="{BARH}" rx="2" class="dg-bar-x"/>')
        o.append(txt(BX + max(2, round(xf*k)) + 8, y + 13, f"{xf:,}", "dg-s", "start"))
        y2 = y + BARH + 5
        o.append(f'<rect x="{BX}" y="{y2}" width="{round(ff*k)}" height="{BARH}" rx="2" class="dg-bar-f"/>')
        lbl = f"{round(ff):,}" + ("（自报 23,000+）" if self_rep else "（推算）")
        o.append(txt(BX + round(ff*k) + 8, y2 + 13, lbl, "dg-s", "start"))
        o.append(txt(W - 20, y + 22, f"{m:g}×", "dg-mult", "end"))

    yb = top + len(rows) * RH + 16
    o.append(f'<line x1="{BX}" y1="{yb}" x2="{W-20}" y2="{yb}" class="dg-edge-thin"/>')
    o.append(txt(BX, yb + 26, "X 粉丝跨度 10.7×（752 → 8,073）", "dg-s", "start"))
    o.append(txt(BX, yb + 48, "FOMO 粉丝跨度仅 2.8×（8,248 → 23,035）", "dg-h", "start"))
    o.append(txt(BX + 330, yb + 38, "→ 离散度塌缩：站内粉丝由战绩决定，", "dg-lab", "start"))
    o.append(txt(BX + 330, yb + 56, "　 与你带进来的外部影响力基本无关", "dg-lab", "start"))
    o.append("</svg>")
    return "\n".join(o)


HTML = '''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>FOMO 增长闭环</title>
<style>
:root{
  --ground:#EDF0F3; --surface:#FFFFFF; --surface-2:#F5F7F9;
  --line:#D3DAE1; --line-soft:#E3E8ED;
  --ink:#121820; --ink-2:#3A4551; --muted:#66727F;
  --accent:#A8500B; --accent-soft:#F3E3D2; --accent-line:#D8A46B;
  --hot:#A8291F; --hot-soft:#F6DEDA;
  --ours:#0B6E6C; --ours-soft:#D9EDEC;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,"Songti SC","Source Han Serif SC",serif;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ground:#0E1319; --surface:#151C24; --surface-2:#1B242E;
  --line:#2C3945; --line-soft:#222C37;
  --ink:#E6EBF0; --ink-2:#BCC7D2; --muted:#8695A3;
  --accent:#E9A44C; --accent-soft:#33261A; --accent-line:#7A5828;
  --hot:#EE8378; --hot-soft:#3A1F1C;
  --ours:#54C9C4; --ours-soft:#123331;
}}
:root[data-theme="dark"]{
  --ground:#0E1319; --surface:#151C24; --surface-2:#1B242E;
  --line:#2C3945; --line-soft:#222C37;
  --ink:#E6EBF0; --ink-2:#BCC7D2; --muted:#8695A3;
  --accent:#E9A44C; --accent-soft:#33261A; --accent-line:#7A5828;
  --hot:#EE8378; --hot-soft:#3A1F1C;
  --ours:#54C9C4; --ours-soft:#123331;
}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);
     font-size:16px;line-height:1.72;-webkit-font-smoothing:antialiased}
.wrap{max-width:1040px;margin:0 auto;padding:0 24px 88px}
header{border-bottom:1px solid var(--line);padding:52px 0 26px;margin-bottom:16px}
.kicker{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;
        color:var(--accent);margin:0 0 16px}
h1{font-family:var(--serif);font-weight:600;font-size:clamp(2rem,4.6vw,2.9rem);line-height:1.14;
   letter-spacing:-.015em;margin:0 0 14px;text-wrap:balance}
.dek{font-family:var(--serif);font-size:clamp(1.04rem,2.1vw,1.24rem);line-height:1.6;
     color:var(--ink-2);margin:0;max-width:62ch;text-wrap:pretty}
h2{font-family:var(--serif);font-weight:600;font-size:clamp(1.4rem,3vw,1.85rem);line-height:1.2;
   margin:0 0 8px;text-wrap:balance}
.snum{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--accent);
      text-transform:uppercase;margin:0 0 10px;display:flex;align-items:center;gap:12px}
.snum::after{content:"";flex:1;height:1px;background:var(--line)}
section{margin:64px 0 0}
p{margin:0 0 16px;max-width:70ch;text-wrap:pretty}
strong{font-weight:650;color:var(--ink)}
code{font-family:var(--mono);font-size:.86em;background:var(--surface-2);
     border:1px solid var(--line-soft);border-radius:2px;padding:1px 5px}
ul{margin:0 0 18px;padding-left:22px;max-width:70ch}
li{margin:0 0 9px}
li::marker{color:var(--accent)}

figure{margin:22px 0 12px;background:var(--surface);border:1px solid var(--line);
       border-radius:3px;padding:22px 20px 16px;overflow-x:auto}
figcaption{margin-top:16px;padding-top:14px;border-top:1px solid var(--line-soft);
           font-size:13.5px;line-height:1.6;color:var(--muted);max-width:78ch}
figcaption b{color:var(--ink-2);font-weight:600}
svg.dg{display:block;width:100%;height:auto;min-width:680px;font-family:var(--sans);color:var(--ink-2)}
.dg-box{fill:var(--surface);stroke:var(--line);stroke-width:1}
.dg-box-soft{fill:var(--surface-2);stroke:var(--line-soft);stroke-width:1}
.dg-box-accent{fill:var(--accent-soft);stroke:var(--accent-line);stroke-width:1}
.dg-box-root{fill:var(--ours-soft);stroke:var(--ours);stroke-width:1.5}
.dg-t{fill:var(--ink);font-size:13.5px;font-weight:600}
.dg-t2{fill:var(--ink);font-size:12.5px}
.dg-s{fill:var(--muted);font-size:11px}
.dg-h{fill:var(--accent);font-size:12px;font-weight:700;letter-spacing:.04em}
.dg-n{fill:var(--accent);font-size:11px;font-family:var(--mono);font-weight:600}
.dg-edge{stroke:var(--muted);stroke-width:1.5;fill:none}
.dg-edge-thin{stroke:var(--line);stroke-width:1.2;fill:none}
.dg-edge-hot{stroke:var(--accent);stroke-width:2.4}
.dg-edge-loop{stroke:var(--ours);stroke-width:1.5;stroke-dasharray:6 4}
.dg-leak{stroke:var(--hot);stroke-dasharray:5 4;stroke-width:1.4}
.dg-lab,.dg-lab-hot,.dg-lab-loop,.dg-leak-t{
  paint-order:stroke;stroke:var(--surface);stroke-width:5px;stroke-linejoin:round}
.dg-lab{fill:var(--ink-2);font-size:11.5px}
.dg-lab-hot{fill:var(--accent);font-size:12.5px;font-weight:700}
.dg-lab-loop{fill:var(--ours);font-size:11.5px}
.dg-leak-t{fill:var(--hot);font-size:11.5px}
.dg-bar-x{fill:var(--muted);opacity:.45}
.dg-bar-f{fill:var(--accent)}
.dg-mult{fill:var(--accent);font-size:14px;font-weight:700;font-family:var(--mono)}

.note{background:var(--surface-2);border:1px solid var(--line-soft);border-left:3px solid var(--muted);
      border-radius:3px;padding:16px 20px;margin:0 0 22px;font-size:15px}
.note.hinge{border-left-color:var(--accent);background:var(--accent-soft)}
.note.leak{border-left-color:var(--hot);background:var(--hot-soft)}
.note.gain{border-left-color:var(--ours);background:var(--ours-soft)}
.note p:last-child{margin-bottom:0}
.note h3{margin:0 0 8px;font-size:1rem;font-weight:650}

.scroll{overflow-x:auto;margin:0 0 22px;border:1px solid var(--line);border-radius:3px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:14px;line-height:1.55}
th,td{padding:10px 14px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line-soft)}
thead th{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;
         color:var(--muted);font-weight:600;background:var(--surface-2);border-bottom:1px solid var(--line)}
tbody tr:last-child td{border-bottom:none}
.pill{display:inline-block;font-family:var(--mono);font-size:10.5px;font-weight:600;padding:2px 7px;
      border-radius:2px;white-space:nowrap;border:1px solid transparent}
.p-hi{background:var(--hot-soft);color:var(--hot);border-color:var(--hot)}
.p-us{background:var(--ours-soft);color:var(--ours);border-color:var(--ours)}
footer{margin:72px 0 0;padding:22px 0 0;border-top:1px solid var(--line);
       font-family:var(--mono);font-size:11.5px;color:var(--muted);line-height:1.7}
@media (max-width:640px){.wrap{padding:0 16px 56px}figure{padding:14px 12px 12px}}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
</style>
</head>
<body>
<div class="wrap">

<header>
  <p class="kicker">竞品情报 · FOMO 系列 · 内部使用</p>
  <h1>FOMO 的增长闭环</h1>
  <p class="dek">获客与交易不是两件事。在 FOMO 这里，<strong>一笔交易同时是三样东西</strong>：一次收入、一条内容、一个获客素材。而这套机制的终点，是它能把一个 X 上 752 粉的素人，变成站内两万人的红人。</p>
</header>

<section>
  <p class="snum">01 — 主飞轮</p>
  <h2>六个环节，一圈闭合</h2>
  <p>橙色那条边是整个闭环的<strong>铰链</strong>。别的产品要单独做内容运营，FOMO 不用——用户下单的那一刻，内容就产生了。</p>
  __FIG1__
  <div class="note hinge">
    <h3>铰链：交易即内容</h3>
    <p>②→③ 这一步是零边际成本的。传统交易终端要花钱买内容、请分析师、做社区；FOMO 的内容供给量<strong>等于它的交易笔数</strong>——128k 笔/日就是 128k 条内容。交易越多，内容越多；内容越多，跟单越多；跟单又变成交易。<strong>这条边一旦接上，获客成本就随规模下降，而不是上升。</strong></p>
  </div>
  <div class="note leak">
    <h3>四个漏损点（红色虚线）</h3>
    <p>闭环不是密封的。每个漏损点都是用户在某个环节掉队的地方，也正是<strong>我们可以插进去的位置</strong>——细节见第 04 节。</p>
  </div>
</section>

<section>
  <p class="snum">02 — 加速支路</p>
  <h2>四条自我强化的支路，把飞轮越推越快</h2>
  <p>主飞轮只是基础转速。真正让 FOMO 在 2026 年 7–8 月出现收入爆发的，是这四条各自也能自转、并持续向主飞轮注入动能的支路。其中<strong>原生红人孵化回路</strong>是本轮 X 数据新增的一条，也是四条里最强的一条——详见第 04 节。</p>
  __FIG2__
  <div class="note gain">
    <p>四条支路有个共同点：<strong>都把「用户」变成了「渠道」</strong>。推荐分润让普通用户变推广者，CLANS 让 KOL 把观众变成可累积的资产，融资则把增长数字本身变成下一轮获客预算。FOMO 几乎不需要自己去"投放"——它把投放外包给了利益相关者。</p>
  </div>
</section>

<section>
  <p class="snum">03 — 获客侧拆解</p>
  <h2>五条并行通道</h2>
  <p>把「获客」这个词展开，FOMO 实际同时在跑五条通道。排序按权重，并把两条「裂变」放在一起：<strong>社交裂变</strong>靠关系带人（原生红人孵化就长在这一条上），<strong>联盟裂变</strong>靠利益带人（分润与折扣码）——它们是同一件事的两种驱动力，理应相邻阅读。而<strong>产品即获客</strong>是最容易被漏看、也最难被复制的一条。</p>
  __FIG3__
  <div class="note">
    <p><b>为什么"产品即获客"是最狠的一条：</b>其余四条都要持续付费（KOL 要钱、分润要钱、推送要研发），只有这一条是<strong>一次性建设、永久生效</strong>。Apple Pay 入金牵涉支付合规，USDC 统一余额与 gas 代付牵涉跨链清算架构——这两样都不是砸钱一个季度能追平的。</p>
  </div>
</section>

<section>
  <p class="snum">04 — 影响力发生器</p>
  <h2>它不是放大影响力，是从零制造影响力</h2>
  <p>这是 X 全网数据里最硬的一条发现。看被官方点名的五位原生交易员——<strong>X 粉丝越少的人，在 FOMO 上的放大倍数越高</strong>。</p>
  __FIG4__
  <div class="note hinge">
    <h3>离散度塌缩说明了什么</h3>
    <p>五个人的 X 粉丝相差 <strong>10.7 倍</strong>（752 → 8,073），但他们的 FOMO 粉丝只相差 <strong>2.8 倍</strong>（8,248 → 23,035）。外部影响力的巨大差距，进了 FOMO 就被抹平了。</p>
    <p>结论：<strong>在 FOMO 上，粉丝数由站内战绩决定，不由你带进来的外部影响力决定。</strong>它不是一个"把 X 影响力搬过来放大"的场子，而是一个<strong>平行的、自产自销的影响力市场</strong>。一个 X 上 752 粉的普通人，可以在这里拥有两万观众。</p>
  </div>
  <div class="note gain">
    <h3>为什么这是最强的锁定</h3>
    <p>这份影响力<strong>只在 FOMO 内部有效，迁不走</strong>。Pump.fun 挖角开出 $20k 签约 + $30k/月，却<strong>要求永久删除 FOMO 账号并签排他协议</strong>——因为它很清楚：账号本身就是资产，不删掉，人就等于没挖走。</p>
    <p>反过来看，这也给我们提了个醒：<strong>费率补贴挖不动这批人</strong>，能挖动他们的只有"能不能在你那儿重建同等规模的观众"。</p>
  </div>

  <h3>策略切换：从造星到被投奔</h3>
  <p>把名单按时间排开，能看到一次清晰的策略转向：</p>
  <div class="scroll">
  <table>
    <thead><tr><th>阶段</th><th>做法</th><th>代表账号</th><th>获客成本</th></tr></thead>
    <tbody>
      <tr><td><strong>2025 下半年 – 2026 上半年</strong><br>孵化期</td><td>点名原生素人，宣传"在 FOMO 建立声誉"，用官方庆祝当激励货币</td><td>@wwayfboss 752 · @octoseaa 2,636 · @f4vel 3,055 · @thokani 8,073 · @icemandot 8,091</td><td class="p-us">≈ 零现金</td></tr>
      <tr><td><strong>2026 年 3–6 月</strong><br>放大期</td><td>密集庆祝个人里程碑（涨粉、Leaderboard 登顶），把个案变成可复制的模板</td><td>@remusofmars 36k · @jotagezin 12.8k · @ResellCalendar 104k · @pingucharts 8.6k</td><td class="p-us">低</td></tr>
      <tr><td><strong>2026 年 7–8 月</strong><br>投奔期</td><td><strong>外部成名 KOL 与创始人主动宣布加入</strong>，平台不再需要买他们</td><td>@andyyy 76k · @mattkalish 44.8k（DraftKings 背景）· @0xyoshitaka 17k · @orangie 377k · @EricCryptoman 267k</td><td class="p-us">显著下降</td></tr>
    </tbody>
  </table>
  </div>
  <p>这条曲线本身就是飞轮成立的证据：<strong>当平台被证明能凭空造出观众，外部 KOL 就会自己找上门——获客成本随规模下降。</strong>这正是图 1 那条铰链在人力侧的表现。</p>

  <h3>跟单生态已经分化出三种类型</h3>
  <div class="scroll">
  <table>
    <thead><tr><th>类型</th><th>代表</th><th>驱动力</th><th>社区黏性</th><th>对我们的启示</th></tr></thead>
    <tbody>
      <tr><td>社交情绪型</td><td>@hdegrootvan<br>X 7,943 → FOMO 23,000+</td><td>高透明度截图 + 心态分享 + 社区回馈（stimmy / referral 福利）</td><td class="p-hi">最高</td><td>纯数据产品替代不了"一起战斗"的归属感</td></tr>
      <tr><td>资金实力型</td><td>@icemandot<br>X 8,091</td><td>钱包余额 + 单笔爆发，低调高胜率</td><td>中等</td><td>这类人本来就是我们 Smart Money 榜的强项</td></tr>
      <tr><td>成长学习型</td><td>@thokani<br>X 8,073，2.0×</td><td>真实盈利 + 从零成长故事</td><td>中高</td><td>叙事门槛低、最易复制，是最该抢的一层</td></tr>
    </tbody>
  </table>
  </div>

  <div class="note">
    <h3>澄清：FOMO 的「跟单」是手动的</h3>
    <p>源报告原文是「Follow 后接收通知，<strong>用户手动决定是否复制</strong>」——即你关注的人成交后，你收到推送，<strong>再由你自己点进去下单</strong>，买不买、买多少全是你的决定。系统<strong>不会</strong>按预设比例自动镜像，你不在线就什么都不会发生。</p>
    <p>所以它本质是<strong>推送驱动的交易</strong>，不是资管型跟单——与 callout 热门推送是同一套机制的延伸。</p>
    <p><strong>为什么只能先做手动</strong>〔推断〕：真自动跟单要求平台能代用户签名，而 FOMO 用 Privy 分片密钥，签名必须由前端 iframe 拉 share、本地重组私钥完成，<strong>用户不在场就签不了</strong>。要做真自动，要么托管私钥（自托管叙事破功），要么上会话密钥 / 预授权。这与它做不了真限价单是<strong>同一个技术根因</strong>——创始人公开承认过非托管跨 5 链做真限价单「extremely technical」。跟单、限价单、止盈止损，卡的是同一道墙。</p>
    <p><strong>两处不确定</strong>：源报告称「后期增加更接近自动 Copy 的功能」，用词是<em>更接近</em>，<strong>未说明已实现全自动</strong>；且其本身也承认「细粒度复制成交量属于 App 内部数据，外部无法完整获取」——<strong>跟单的真实执行率外部看不到</strong>。</p>
  </div>

  <div class="note leak">
    <h3>这条回路的阴暗面（可打击）</h3>
    <p>头部交易员粉丝越多，其交易越容易产生<strong>自实现效应</strong>——跟风资金帮助其顺利出场。社区已有公开批评：<strong>KOL 可能用小号提前布局，再用主号带跟单</strong>。这与图 1 中④的「跟单者成为退出流动性」是同一个漏损点，只是这里能看到它的<strong>作案机制</strong>。</p>
    <p>我们的反制不是也去造星，而是<strong>用链上数据把这件事查清楚并公示</strong>：关联地址识别、前置建仓检测、跟单者盈亏分布。这是 FOMO 结构上做不到的——它没有自研数据。</p>
  </div>

  <div class="note">
    <h3>数据质量说明（重要）</h3>
    <ul>
      <li>本节数据来自 X 公开抓取的二手整理，<strong>非我们的一手观测</strong>，粉丝数为抓取时点值。</li>
      <li><strong>FOMO 粉丝数是推算值</strong>（X 粉丝 × 官方公布倍数），仅 @hdegrootvan 的 23,000+ 为本人自报。</li>
      <li><strong>存在明显选择偏差</strong>：被官方点名的必然是倍数高的样本，n=5，<strong>不能代表平台平均水平</strong>。真实的中位放大倍数很可能远低于此。</li>
      <li>源数据自身标注了句柄匹配的不确定性（如 @btc_goose 系 @thebtcgoose 的最佳匹配），<strong>账号级准确性未经核验</strong>。</li>
      <li>建议后续用 Sensor Tower / 站内爬取做一次无偏采样，验证"离散度塌缩"是否在全量用户上成立。</li>
    </ul>
  </div>
</section>

<section>
  <p class="snum">05 — 诊断：我们在每个环节的位置</p>
  <h2>不要照抄飞轮，要挑环节下手</h2>
  <div class="note">
    <p><strong>📐 本页只做诊断，不开药方。</strong>下表回答「每个环节我们站在哪、能不能打」；<strong>具体行动与优先级统一在</strong><a href="https://claude.ai/code/artifact/0bf4ad28-129d-4594-83bf-7f5fa741271b">《FOMO 全面产品调研》§10</a>，避免两处优先级打架。需要一页纸转发的版本见<a href="https://claude.ai/code/artifact/76b7997d-e74f-4e77-bb3e-66d986048bef">《FOMO 决策简报》</a>。</p>
  </div>
  <p>完整复制这个闭环既不现实也没必要。按"我们能不能做、做了打不打得中"两个维度，逐环节看现状。</p>
  <div class="scroll">
  <table>
    <thead><tr><th>闭环环节</th><th>FOMO 的做法</th><th>我们的位置</th><th>诊断</th></tr></thead>
    <tbody>
      <tr><td>① 零门槛进人</td><td>Apple Pay + USDC 统一余额 + gas 代付</td><td class="p-hi">明显落后</td><td>差距集中在<strong>入金与 gas 两处摩擦</strong>；其中统一余额 + gas 代付不依赖任何外部方，跨链无感才依赖 Relay</td></tr>
      <tr><td>② 首笔交易达成</td><td>一键、跨链无感，但小额收 47.5%、BNB 会不填充</td><td class="p-us">我们更强</td><td>它 ≤200U 收<strong>固定 0.95U/笔</strong>，与我们 1% 的临界点是 <strong>$95</strong> —— 以上全线是它便宜；但内盘 / 滑点 / 加速是它<strong>结构上做不到</strong>的</td></tr>
      <tr><td>③ 交易即内容</td><td>交易自动进 Feed，零成本 UGC</td><td class="p-hi">缺失</td><td>闭环铰链所在，<strong>网络效应越晚介入越贵</strong>；但我们的差异资产是数据可信度，而非 Feed 形态本身</td></tr>
      <tr><td>④ 赚钱效应被看见</td><td>Leaderboard 造星，但有 KOL 偏袒争议</td><td class="p-us">可以打</td><td>它的排行榜有<strong>公信力缺口</strong>（KOL 偏袒争议，官方选择透明化而非否认）——这是可对冲的软肋</td></tr>
      <tr><td>⑤ 跟单 + 推送放大</td><td>已上线，激进推送建立心智</td><td class="p-us">质量更好但上线晚</td><td>07-23 实测我们覆盖 <strong>14/14</strong>、<strong>6 币首触更早</strong>，且质量闸能拦假热度；<strong>唯一劣势是上线时间</strong></td></tr>
      <tr><td>③b 原生红人孵化<br><span class="pill p-hi">X 数据新增</span></td><td>把 X 素人造成站内 8k–23k 粉的红人，影响力迁不走</td><td class="p-hi">缺失且最难补</td><td>影响力<strong>迁不走</strong>，费率补贴挖不动这批人；但它<strong>没有自研数据</strong>，无法审计自家跟单质量——这是结构性缺口</td></tr>
      <tr><td>⑥ 笔数 × 费率</td><td>小额高频，$0.76/笔</td><td class="p-us">费率结构更优</td><td>收入由笔数驱动；其 Solana 收费钱包净流入<strong>链上可观测</strong>，等于对手转速的实时读数</td></tr>
    </tbody>
  </table>
  </div>
  <div class="note leak">
    <h3>四个漏损点：用户实际在哪掉队</h3>
    <ul>
      <li><strong>出金跳去 Spritz</strong> —— 提现是它投诉最集中的区域，且不在 App 内闭环。这是信任崩塌点，量化后可作为最硬的攻击素材。</li>
      <li><strong>小额被罚 47.5%</strong> —— 买 $2 收 $0.95。用户只要算过一次账就会走，而这恰恰是它主力人群（$0.76/笔说明客单极小）。</li>
      <li><strong>BNB 高波动不填充</strong> —— 官方承认在修但方案未定，窗口期有限。</li>
      <li><strong>跟单者成为退出流动性</strong> —— 排行榜跟单的负和本质，用户已在公开质疑"故意在即将下跌时推送买入警报"。</li>
    </ul>
  </div>
</section>

<div class="note">
  <h3>📐 这份文档在哪一层</h3>
  <p><strong>Tier 0</strong> <a href="https://claude.ai/code/artifact/76b7997d-e74f-4e77-bb3e-66d986048bef">FOMO 决策简报</a> —— 结论 · 威胁分级 · P0/P1，一屏读完，可直接转发。<br>
  <strong>Tier 1</strong> <strong>本页</strong> —— 回答「病在哪」：飞轮机制、铰链、漏损点、获客导图。<br>
  <strong>Tier 2</strong> <a href="https://claude.ai/code/artifact/0bf4ad28-129d-4594-83bf-7f5fa741271b">FOMO 全面产品调研</a> —— 回答「怎么治」+ 全部证据：资本、数据、技术拆解、费率、口碑、行动清单、附录。</p>
</div>

<footer>
  数据来源：GMGN 内部一手调研（链上实测 · HAR 抓包 · 07-23 影子测试 · 社群监控）与公开报道交叉整理，截至 2026-08-11。<br>
  跨文档复用的数字收敛在 docs/_build/fomo_facts.py。竞品情报，内部使用。
</footer>

</div>
</body>
</html>
'''

out = HTML.replace("__FIG1__",
        '<figure>' + fig1() + '<figcaption><b>图 1 · 主飞轮。</b>顺时针六个环节构成闭环，橙色边为铰链（交易即内容，零边际成本 UGC）；红色虚线为四个漏损点，标注在用户实际掉队的环节上。</figcaption></figure>'
    ).replace("__FIG2__",
        '<figure>' + fig2() + '<figcaption><b>图 2 · 四条加速支路。</b>每条支路自身构成小循环（青色虚线为回流），并把动能注入主飞轮。共同机制：把用户、KOL、投资人都变成获客渠道——而原生红人孵化回路更进一步，<b>直接把素人造成红人</b>。</figcaption></figure>'
    ).replace("__FIG3__",
        '<figure>' + fig3() + '<figcaption><b>图 3 · 获客侧思维导图。</b>五条并行通道及其具体手段，<b>★ 为本轮 X 数据新增</b>。两条「裂变」相邻：社交裂变靠关系带人、联盟裂变靠利益带人；而「产品即获客」是唯一一次性建设、永久生效的通道——也是最难追平的一条。</figcaption></figure>'
    ).replace("__FIG4__",
        '<figure>' + fig4() + '<figcaption><b>图 4 · 影响力发生器。</b>五位被官方点名的原生交易员，X 粉丝（灰）与 FOMO 粉丝（橙）对比。FOMO 粉丝除 @hdegrootvan 为本人自报外均由「X 粉丝 × 官方倍数」推算。<b>注意选择偏差：官方只会点名倍数高的样本，n=5，不代表平台平均水平。</b></figcaption></figure>'
    )

open("/home/user/ava1026/docs/fomo-growth-loop.html", "w", encoding="utf-8").write(out)
print("written:", len(out), "bytes")
