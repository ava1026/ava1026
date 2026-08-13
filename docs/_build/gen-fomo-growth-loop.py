# -*- coding: utf-8 -*-
"""生成 FOMO 增长闭环页面（三张手绘 SVG + 说明）"""

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

    leak(xs[1] + BW/2, True,  ["漏损：小额 ≤200U 实收 47.5%", "BNB 高波动不填充"])
    leak(xs[2] + BW/2, True,  ["漏损：KOL listing 偏袒争议", "排行榜公信力受损"])
    leak(xs[2] + BW/2, False, ["漏损：跟单者成为退出流动性"])
    leak(xs[0] + BW/2, False, ["漏损：出金要跳去 Spritz", "提现是投诉最集中区"])

    o.append("</svg>")
    return "\n".join(o)


# ══════════════════════════ 图二：三条加速支路 ══════════════════════════
def fig2():
    P = "f2"
    W, H = 960, 522
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
        ("资本回路", [
            ["交易量 / 用户数连创新高"],
            ["$550M 估值", "累计 $94M 到账"],
            ["现金补贴费率 / KOL / 入金"],
        ], "融资叙事本身成为获客预算的来源"),
    ]
    o = [f'<svg class="dg" role="img" viewBox="0 0 {W} {H}" '
         f'aria-label="三条加速支路：推荐分润回路、KOL 与 CLANS 回路、资本回路，各自自我强化后注入主飞轮">',
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
        ]),
        ("产品即获客", "删摩擦", [
            "Apple Pay 直接买币 → 68,000 首次买币用户 / $25M",
            "USDC 单一余额，跨 4–5 条链无感",
            "gas 全代付，无需持有任何原生代币",
            "极简 UI，App Store 4.6★",
        ]),
        ("联盟裂变", "买增长，按效果付费", [
            "邀请码 10% 终身手续费折扣",
            "卖出侧 25% 实时分润，无上限",
            "SEO 套利者虚标 90% / 95% 折扣（官方仅 10%）",
            "实测：约 29% 手续费来自绑定推荐人的用户",
        ]),
        ("社交裂变", "让用户互相拉", [
            "Friends：邀好友一起交易",
            "Feed：每笔交易自动成为内容",
            "Leaderboard：造星，制造可跟随对象",
            "CLANS（8/10 上线，50+）：组队、共建受众",
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
  <p class="dek">获客与交易不是两件事。在 FOMO 这里，<strong>一笔交易同时是三样东西</strong>：一次收入、一条内容、一个获客素材——这才是它转得比谁都快的原因。</p>
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
  <h2>三条自我强化的支路，把飞轮越推越快</h2>
  <p>主飞轮只是基础转速。真正让 FOMO 在 2026 年 7–8 月出现收入爆发的，是这三条各自也能自转、并持续向主飞轮注入动能的支路。</p>
  __FIG2__
  <div class="note gain">
    <p>三条支路有个共同点：<strong>都把「用户」变成了「渠道」</strong>。推荐分润让普通用户变推广者，CLANS 让 KOL 把观众变成可累积的资产，融资则把增长数字本身变成下一轮获客预算。FOMO 几乎不需要自己去"投放"——它把投放外包给了利益相关者。</p>
  </div>
</section>

<section>
  <p class="snum">03 — 获客侧拆解</p>
  <h2>五条并行通道</h2>
  <p>把「获客」这个词展开，FOMO 实际同时在跑五条通道。注意第二条——<strong>产品本身就是获客渠道</strong>，这是最容易被漏看、也最难被复制的一条。</p>
  __FIG3__
  <div class="note">
    <p><b>为什么"产品即获客"是最狠的一条：</b>其余四条都要持续付费（KOL 要钱、分润要钱、推送要研发），只有这一条是<strong>一次性建设、永久生效</strong>。Apple Pay 入金牵涉支付合规，USDC 统一余额与 gas 代付牵涉跨链清算架构——这两样都不是砸钱一个季度能追平的。</p>
  </div>
</section>

<section>
  <p class="snum">04 — 对我们的含义</p>
  <h2>不要照抄飞轮，要挑环节下手</h2>
  <p>完整复制这个闭环既不现实也没必要。更有效的做法是按"我们能不能做、做了打不打得中"两个维度，对每个环节单独定策。</p>
  <div class="scroll">
  <table>
    <thead><tr><th>闭环环节</th><th>FOMO 的做法</th><th>我们的位置</th><th>建议</th></tr></thead>
    <tbody>
      <tr><td>① 零门槛进人</td><td>Apple Pay + USDC 统一余额 + gas 代付</td><td class="p-hi">明显落后</td><td><strong>先做统一 USDC 余额 + gas 代付</strong>（体验的 80% 在这里，且不依赖外部方），跨链无感放第二步</td></tr>
      <tr><td>② 首笔交易达成</td><td>一键、跨链无感，但小额收 47.5%、BNB 会不填充</td><td class="p-us">我们更强</td><td>把<strong>小额费率对比</strong>做成传播物料；内盘 / 滑点 / 加速是它结构上做不到的</td></tr>
      <tr><td>③ 交易即内容</td><td>交易自动进 Feed，零成本 UGC</td><td class="p-hi">缺失</td><td>这是闭环铰链，<strong>越晚做越贵</strong>。但不必抄 Feed 形态——我们的优势是数据可信度</td></tr>
      <tr><td>④ 赚钱效应被看见</td><td>Leaderboard 造星，但有 KOL 偏袒争议</td><td class="p-us">可以打</td><td>做<strong>用真实链上数据背书的排行榜 / 组队</strong>，直接对冲它的公信力弱点</td></tr>
      <tr><td>⑤ 跟单 + 推送放大</td><td>已上线，激进推送建立心智</td><td class="p-us">质量更好但上线晚</td><td>推送尽快全量；我们 07-23 实测覆盖 14/14、6 币首触更早，且有质量闸拦假热度</td></tr>
      <tr><td>⑥ 笔数 × 费率</td><td>小额高频，$0.76/笔</td><td class="p-us">费率结构更优</td><td>盯住它的收费钱包净流入做日报，实时掌握对手转速</td></tr>
    </tbody>
  </table>
  </div>
  <div class="note leak">
    <h3>四个漏损点 = 四个切入口</h3>
    <ul>
      <li><strong>出金跳去 Spritz</strong> —— 提现是它投诉最集中的区域，且不在 App 内闭环。这是信任崩塌点，量化后可作为最硬的攻击素材。</li>
      <li><strong>小额被罚 47.5%</strong> —— 买 $2 收 $0.95。用户只要算过一次账就会走，而这恰恰是它主力人群（$0.76/笔说明客单极小）。</li>
      <li><strong>BNB 高波动不填充</strong> —— 官方承认在修但方案未定，窗口期有限。</li>
      <li><strong>跟单者成为退出流动性</strong> —— 排行榜跟单的负和本质，用户已在公开质疑"故意在即将下跌时推送买入警报"。</li>
    </ul>
  </div>
</section>

<footer>
  数据来源：GMGN 内部一手调研（链上实测 · HAR 抓包 · 07-23 影子测试 · 社群监控）与公开报道交叉整理，截至 2026-08-11。<br>
  完整论证、口径说明与资料出处见《FOMO 全面产品调研》主报告。竞品情报，内部使用。
</footer>

</div>
</body>
</html>
'''

out = HTML.replace("__FIG1__",
        '<figure>' + fig1() + '<figcaption><b>图 1 · 主飞轮。</b>顺时针六个环节构成闭环，橙色边为铰链（交易即内容，零边际成本 UGC）；红色虚线为四个漏损点，标注在用户实际掉队的环节上。</figcaption></figure>'
    ).replace("__FIG2__",
        '<figure>' + fig2() + '<figcaption><b>图 2 · 三条加速支路。</b>每条支路自身构成小循环（青色虚线为回流），并把动能注入主飞轮。共同机制：把用户、KOL、投资人都变成获客渠道。</figcaption></figure>'
    ).replace("__FIG3__",
        '<figure>' + fig3() + '<figcaption><b>图 3 · 获客侧思维导图。</b>五条并行通道及其具体手段。前四条持续烧钱，第二条「产品即获客」是一次性建设、永久生效——也是最难追平的一条。</figcaption></figure>'
    )

open("/home/user/ava1026/docs/fomo-growth-loop.html", "w", encoding="utf-8").write(out)
print("written:", len(out), "bytes")
