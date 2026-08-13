# -*- coding: utf-8 -*-
"""
生成《GMGN App 产品侧打法》 -> docs/gmgn-counterplay.html

这份文档的身份：
  Arthur v8 deck 第 15 页「本稿已知的缺口」第一条写着——
    「产品视角尚未纳入主线：Ava 08-13『我也弄了一份，在优化，一起比对』，
      她的正式产品视角未到，本稿第 12.5 页只是她 08-11 的排期清单。到齐后并入 v8。」
  本文就是那一份。所以：
    · 模块划分照 Ava 08-13 的口述：定位 → 发现层 → 放大层 → 拉新与承接 → 地基
    · 只写产品侧能交付的东西（增长线 / 渠道线归 v8，本文不重复排优先级）
    · 对 v8 与我方排期的冲突（USDC relay）给出边界，而不是回避

三层文档矩阵里的位置：
  Tier 0  fomo-brief            一页纸决策简报
  Tier 1  fomo-growth-loop      FOMO 增长闭环（诊断：它为什么转得动）
  Tier 1  gmgn-counterplay      本文（产品侧应对）                 ← 新增
  Tier 2  fomo-product-research 全面产品调研（参考层 + 防守清单 §10.2）

数字一律从 fomo_facts 注入。改数字改那里，然后跑 check-facts.py。
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import fomo_facts as F

V = F.V8
A = F.ARTHUR


# ── SVG 基元 ────────────────────────────────────────────
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def box(x, y, w, h, cls="dg-box", rx=3):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}"/>'

def txt(x, y, s, cls="dg-t", anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">{esc(s)}</text>'


# ── 图 1：【打】四个咬合点 ──────────────────────────────
def fig_bite():
    W, H = 960, 428
    LX, LW = 8, 224
    MX, MW = 336, 288
    RX, RW = 728, 224
    RH, GAP, Y0 = 64, 14, 40

    ROWS = [
        (["自研链上数据", "持仓来源 · 关联地址 · 资金关系"],
         "① 把 FOMO 榜搬过来重算",
         "留住要去 FOMO 看榜的用户",
         ["榜单 PnL 不区分来源", "没有自研数据，审计不了自己"], True),

        (["内盘 / 首发支持", "毕业前就能交易"],
         "② 进场点位分布",
         "谁在接谁的盘，画出来",
         ["只能毕业后进场", "Relay 仅询价标准 AMM"], True),

        (["服务端可用的签名路径", "真限价单 · 止盈止损已上线"],
         "③ 三件事，同一道墙",
         "从功能差升级为架构差",
         ["Privy 分片需设备在场", "自动跟单 · 真限价 · 止盈止损"], False),

        (["单链对单链 · 链上出入金", "执行可靠"],
         "④ 接住它的资金进出债",
         "一键接管持仓",
         ["卖不出（约 $2 门槛）", "入不进 · 拿不走"], True),
    ]

    p = [f'<svg class="dg" viewBox="0 0 {W} {H}" role="img" '
         f'aria-label="GMGN 长板与 FOMO 结构性短板的四个咬合点">']
    p.append('<defs><marker id="cp-ar" viewBox="0 0 10 10" refX="9" refY="5" '
             'markerWidth="6" markerHeight="6" orient="auto">'
             '<path d="M0 0 L10 5 L0 10 z" fill="currentColor"/></marker></defs>')

    p.append(txt(LX + LW / 2, 22, "我们的长板", "dg-h"))
    p.append(txt(MX + MW / 2, 22, "咬合点", "dg-h"))
    p.append(txt(RX + RW / 2, 22, "它的结构性短板", "dg-h"))

    for i, (lt, mt, ms, rt, anchored) in enumerate(ROWS):
        y = Y0 + i * (RH + GAP)
        cy = y + RH / 2

        p.append(box(LX, y, LW, RH, "dg-box-us"))
        p.append(txt(LX + LW / 2, y + 26, lt[0], "dg-t2"))
        p.append(txt(LX + LW / 2, y + 45, lt[1], "dg-s"))

        p.append(box(MX, y, MW, RH, "dg-box-bite"))
        p.append(txt(MX + MW / 2, y + 27, mt, "dg-t"))
        p.append(txt(MX + MW / 2, y + 47, ms, "dg-s"))
        if anchored:
            p.append(txt(MX + 12, y + 55, "⚓", "dg-n", anchor="start"))

        p.append(box(RX, y, RW, RH, "dg-box-them"))
        p.append(txt(RX + RW / 2, y + 26, rt[0], "dg-t2"))
        p.append(txt(RX + RW / 2, y + 45, rt[1], "dg-s"))

        p.append(f'<path d="M{LX + LW + 4} {cy} H{MX - 6}" class="dg-edge" '
                 f'marker-end="url(#cp-ar)"/>')
        p.append(f'<path d="M{MX + MW + 4} {cy} H{RX - 6}" class="dg-edge" '
                 f'marker-end="url(#cp-ar)"/>')

    fy = Y0 + 4 * (RH + GAP) + 8
    p.append(box(LX, fy, W - 16, 52, "dg-box-base"))
    p.append(txt(W / 2, fy + 22, "地基：Relay 交易解析（GMGN-8687 / 8688 / 8689 / 8665）", "dg-t"))
    p.append(txt(W / 2, fy + 41,
                 "⚓ 标记的三条战役都站在这块地基上——它不是止血，是进攻的前置条件", "dg-s"))
    p.append('</svg>')
    return "".join(p)


# ── 图 1：两条拉新链路的对偶 ────────────────────────────
#   左＝FOMO 从圈外拉人，右＝我们从链上拉人。
#   形状几乎一样，差别只在燃料——一个是造出来的 PnL，一个是链上真实持仓。
def fig_lanes():
    W, H = 960, 508
    CW = 436
    LX, RX = 8, 516
    NH, GAP, Y0 = 56, 20, 44
    MID = 480

    LEFT = [
        ("造榜", "拉盘做高 PnL"),
        ("造星", "24h 榜 ＋ 官方转发"),
        ("破圈", "TikTok / IG 短视频"),
        ("圈外小白进来", "此前从未接触 crypto"),
        ("交易", "小白的手续费"),
    ]
    RIGHT = [
        ("发现", "热门代币第一时间抓到并推出"),
        ("放大", "KOL 与大户的真实持仓"),
        ("赚钱效应", "链上可验证，不是造出来的"),
        ("链上新用户进来", "已在链上，但还没用我们"),
        ("交易", "专业执行 ＋ 参数可控"),
    ]

    p = [f'<svg class="dg" viewBox="0 0 {W} {H}" role="img" '
         f'aria-label="FOMO 从圈外拉人与 GMGN 从链上拉人的两条链路对比">']
    p.append('<defs><marker id="ln-ar" viewBox="0 0 10 10" refX="9" refY="5" '
             'markerWidth="6" markerHeight="6" orient="auto">'
             '<path d="M0 0 L10 5 L0 10 z" fill="currentColor"/></marker></defs>')

    p.append(f'<path d="M{MID} 12 V{Y0 + 5 * (NH + GAP) + 46}" class="dg-split"/>')
    p.append(txt(LX + CW / 2, 24, "FOMO：从圈外拉人", "dg-h"))
    p.append(txt(RX + CW / 2, 24, "我们：从链上拉人", "dg-h"))

    for col_x, items, cls in ((LX, LEFT, "dg-box-them"), (RX, RIGHT, "dg-box-us")):
        cx = col_x + CW / 2
        for i, (t, s) in enumerate(items):
            y = Y0 + i * (NH + GAP)
            p.append(box(col_x, y, CW, NH, cls))
            p.append(txt(cx, y + 24, t, "dg-t"))
            p.append(txt(cx, y + 42, s, "dg-s"))
            if i < len(items) - 1:
                p.append(f'<path d="M{cx} {y + NH + 2} V{y + NH + GAP - 5}" '
                         f'class="dg-edge" marker-end="url(#ln-ar)"/>')

    fy = Y0 + 5 * (NH + GAP) + 6
    p.append(box(LX, fy, CW, 46, "dg-box-base"))
    p.append(txt(LX + CW / 2, fy + 20, "燃料：造出来的 PnL", "dg-t2"))
    p.append(txt(LX + CW / 2, fy + 37, "卖出即归零，无承接盘", "dg-s"))
    p.append(box(RX, fy, CW, 46, "dg-box-us"))
    p.append(txt(RX + CW / 2, fy + 20, "燃料：链上真实持仓", "dg-t2"))
    p.append(txt(RX + CW / 2, fy + 37, "可验真，且是我们的存量资产", "dg-s"))
    p.append('</svg>')
    return "".join(p)


FIG_LANES_CAP = (
    "<b>图 1 · 两条拉新链路的对偶。</b>形状一样，<b>差别只在燃料</b>——"
    "它的要花钱造（造出来的盘卖出即归零），我们的是链上已有的真实持仓。"
    "所以客源不同，我们不必跟它抢 TikTok。"
)


# ── 图 0：思维导图（模块全貌）────────────────────────────
#   根在左，五个模块向右展开。叶子按模块分组，组内等距，组间留空。
def fig_map():
    LEAF_H, LEAF_GAP, GROUP_GAP, TOP = 30, 7, 26, 18
    RX, RW = 8, 168          # 根
    BX, BW = 226, 190        # 模块
    LX, LW = 452, 500        # 叶子

    GROUPS = [
        ("定位", "dg-m1", [
            "专业交易能力与专业交易员：主导区，不让",
            "按环节切不同人群：发现给新客，执行与分析守专业",
        ]),
        ("发现层", "dg-m2", [
            "热门代币第一时间发现 → 推出 → 到达",
            "热门精选 push　✓ 已上线，质量闸比 FOMO 稳健",
            "Callout 对标 FOMO thesis　◐ 推进中",
            "热门列表混链整合：弱化链 · 更稳健的币　◐ 推进中",
            "新用户第一屏＝热门榜单，不是交易面板",
        ]),
        ("放大层", "dg-m3", [
            "热门币里的 KOL 持仓",
            "大户持仓与动向",
            "赚钱效应：链上可验真，不是造出来的",
            "FOMO Leaderboard —— 重算，不镜像",
        ]),
        ("拉新与承接", "dg-m4", [
            "客源＝链上新用户，不是圈外小白",
            "法币入金　✓ 已支持，新链上的天然优势",
            "热门代币支持 USDC 购买（限新用户）",
            "跨链：待调研，不进老用户主路径",
            "迁移引导：一键导入私钥 / 接管持仓",
        ]),
        ("地基", "dg-m5", [
            "Relay 交易解析　GMGN-8687 / 8688 / 8689 / 8665",
            "relay 数据的标注与可信度规范",
            "推送延迟 6–20min —— 拦着「第一时间」",
            "客服口径 —— 与 FOMO 被并列批评",
        ]),
    ]

    heights = [len(g[2]) * LEAF_H + (len(g[2]) - 1) * LEAF_GAP for g in GROUPS]
    H = TOP * 2 + sum(heights) + GROUP_GAP * (len(GROUPS) - 1)
    W = LX + LW

    p = [f'<svg class="dg" viewBox="0 0 {W} {H}" role="img" '
         f'aria-label="GMGN App 产品侧打法思维导图">']

    root_cy = H / 2
    p.append(box(RX, root_cy - 30, RW, 60, "dg-box-root"))
    p.append(txt(RX + RW / 2, root_cy - 4, "GMGN App", "dg-troot"))
    p.append(txt(RX + RW / 2, root_cy + 16, "产品侧打法", "dg-troot"))

    y = TOP
    for (name, cls, leaves), gh in zip(GROUPS, heights):
        bcy = y + gh / 2
        p.append(box(BX, bcy - 21, BW, 42, cls))
        p.append(txt(BX + BW / 2, bcy + 5, name, "dg-t"))
        # 根 → 模块
        p.append(f'<path d="M{RX + RW} {root_cy} C{RX + RW + 30} {root_cy}, '
                 f'{BX - 30} {bcy}, {BX} {bcy}" class="dg-edge-thin"/>')
        for i, leaf in enumerate(leaves):
            ly = y + i * (LEAF_H + LEAF_GAP)
            lcy = ly + LEAF_H / 2
            p.append(box(LX, ly, LW, LEAF_H, "dg-box-leaf"))
            p.append(txt(LX + 12, lcy + 4, leaf, "dg-t3", anchor="start"))
            p.append(f'<path d="M{BX + BW} {bcy} C{BX + BW + 24} {bcy}, '
                     f'{LX - 24} {lcy}, {LX} {lcy}" class="dg-edge-thin"/>')
        y += gh + GROUP_GAP

    p.append('</svg>')
    return "".join(p)


# ── 图 0b：五个模块怎么转起来 ────────────────────────────
#   导图是静态树，看不出模块之间的喂养关系。这张补箭头：
#   前四个模块首尾相接成环，第五个（地基）在下面托着整圈。
def fig_loop():
    W, H = 960, 250
    NW, NH, NY = 200, 72, 62
    XS = [8, 256, 504, 752]

    NODES = [
        ("① 发现", "热门币第一时间抓到并推出", "§03"),
        ("② 放大", "KOL 与大户的真实持仓", "§04"),
        ("③ 拉新承接", "法币入金 · USDC · 迁移引导", "§05"),
        ("④ 交易", "专业执行 · 参数可控", "—"),
    ]

    p = [f'<svg class="dg" viewBox="0 0 {W} {H}" role="img" '
         f'aria-label="五个模块的流转闭环：发现→放大→拉新承接→交易，数据回流，地基托底">']
    p.append('<defs><marker id="lp-ar" viewBox="0 0 10 10" refX="9" refY="5" '
             'markerWidth="6" markerHeight="6" orient="auto">'
             '<path d="M0 0 L10 5 L0 10 z" fill="currentColor"/></marker></defs>')

    for i, (t, sub, ref) in enumerate(NODES):
        x = XS[i]
        cx = x + NW / 2
        p.append(box(x, NY, NW, NH, "dg-box-us"))
        p.append(txt(cx, NY + 28, t, "dg-t"))
        p.append(txt(cx, NY + 48, sub, "dg-s"))
        if ref != "—":
            p.append(txt(x + NW - 10, NY + 16, ref, "dg-n", anchor="end"))
        if i < len(NODES) - 1:
            p.append(f'<path d="M{x + NW + 5} {NY + NH / 2} H{XS[i + 1] - 7}" '
                     f'class="dg-edge" marker-end="url(#lp-ar)"/>')

    # 回流弧（走上方，避开地基）
    x4c = XS[3] + NW / 2
    x1c = XS[0] + NW / 2
    p.append(f'<path d="M{x4c} {NY - 2} V42 Q{x4c} 32 {x4c - 10} 32 '
             f'H{x1c + 10} Q{x1c} 32 {x1c} 42 V{NY - 4}" '
             f'class="dg-edge-loop" marker-end="url(#lp-ar)"/>')
    p.append(txt(W / 2, 20, "数据回流：谁在买 · 谁在赚 · 什么在热", "dg-lab-loop"))

    # 地基
    fy = NY + NH + 34
    p.append(box(8, fy, W - 16, 56, "dg-m5"))
    p.append(txt(W / 2, fy + 24, "⑤ 地基：Relay 交易解析 · 标注与可信度规范 · 推送延迟〔待核〕· 客服口径", "dg-t"))
    p.append(txt(W / 2, fy + 43, "四条都托在上面这一圈底下——不清掉，环转不起来", "dg-s"))
    for x in XS:
        cx = x + NW / 2
        p.append(f'<path d="M{cx} {fy - 3} V{NY + NH + 7}" '
                 f'class="dg-edge-thin" marker-end="url(#lp-ar)" '
                 f'style="color:var(--hot);stroke:var(--hot)"/>')

    p.append('</svg>')
    return "".join(p)


FIG_LOOP_CAP = (
    "<b>图 0 · 五个模块怎么转起来。</b>前四个首尾相接：交易产生的链上数据回流到发现层，"
    "让下一轮「什么在热、谁在赚」更准。<b>地基那条不产生用户价值，但托着整圈</b>——"
    "Relay 解析没修，②③ 就拿不到 FOMO 那侧的数据。"
)


FIG_MAP_CAP = (
    "<b>图 0b · 每个模块里装什么。</b>前四个是产品要交付的，第五个是拦着前四个的地基。"
    "✓＝已上线，◐＝推进中，其余为本季度新增。"
)


FIG_CAP = (
    "<b>图 2 · 四个咬合点。</b>只收结构性短板——改它要动供应商架构或账户体系。"
    "带 ⚓ 的三条共用同一块地基，那块地基的排期决定它们的启动时间。"
)


CSS = '''
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
     color:var(--ink-2);margin:0;max-width:64ch;text-wrap:pretty}
h2{font-family:var(--serif);font-weight:600;font-size:clamp(1.4rem,3vw,1.85rem);line-height:1.2;
   margin:0 0 10px;text-wrap:balance}
h3{font-family:var(--sans);font-weight:650;font-size:1.02rem;margin:26px 0 8px}
h4{font-family:var(--sans);font-weight:650;font-size:.95rem;margin:20px 0 6px;color:var(--ink-2)}
.snum{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--accent);
      text-transform:uppercase;margin:0 0 10px;display:flex;align-items:center;gap:12px}
.snum::after{content:"";flex:1;height:1px;background:var(--line)}
section{margin:64px 0 0}
p{margin:0 0 16px;max-width:70ch;text-wrap:pretty}
strong{font-weight:650;color:var(--ink)}
em{font-style:normal;color:var(--accent);font-weight:600}
code{font-family:var(--mono);font-size:.86em;background:var(--surface-2);
     border:1px solid var(--line-soft);border-radius:2px;padding:1px 5px}
a{color:var(--ours);text-underline-offset:2px}
ul,ol{margin:0 0 18px;padding-left:22px;max-width:72ch}
li{margin:0 0 9px}
li::marker{color:var(--accent)}
blockquote{margin:0 0 16px;padding:2px 0 2px 16px;border-left:2px solid var(--accent-line);
           color:var(--ink-2);font-style:italic;max-width:68ch}

figure{margin:22px 0 12px;background:var(--surface);border:1px solid var(--line);
       border-radius:3px;padding:22px 20px 16px;overflow-x:auto}
figcaption{margin-top:16px;padding-top:14px;border-top:1px solid var(--line-soft);
           font-size:13.5px;line-height:1.6;color:var(--muted);max-width:80ch}
figcaption b{color:var(--ink-2);font-weight:600}
svg.dg{display:block;width:100%;height:auto;min-width:700px;font-family:var(--sans);color:var(--muted)}
.dg-box-us{fill:var(--ours-soft);stroke:var(--ours);stroke-width:1.2}
.dg-box-bite{fill:var(--surface);stroke:var(--accent-line);stroke-width:1.4}
.dg-box-them{fill:var(--hot-soft);stroke:var(--hot);stroke-width:1.2}
.dg-box-base{fill:var(--accent-soft);stroke:var(--accent-line);stroke-width:1.4}
.dg-t{fill:var(--ink);font-size:13.5px;font-weight:650}
.dg-troot{fill:#fff;font-size:14px;font-weight:700}
.dg-t2{fill:var(--ink);font-size:12.8px;font-weight:600}
.dg-s{fill:var(--muted);font-size:11px}
.dg-h{fill:var(--accent);font-size:11.5px;font-weight:700;letter-spacing:.1em}
.dg-n{fill:var(--ours);font-size:12px}
.dg-edge{stroke:var(--muted);stroke-width:1.5;fill:none;color:var(--muted)}
.dg-edge-thin{stroke:var(--line);stroke-width:1.3;fill:none;color:var(--line)}\n.dg-edge-loop{stroke:var(--ours);stroke-width:1.6;stroke-dasharray:6 4;fill:none;color:var(--ours)}\n.dg-lab-loop{fill:var(--ours);font-size:11.5px;font-weight:600;paint-order:stroke;stroke:var(--surface);stroke-width:4px;stroke-linejoin:round}
.dg-split{stroke:var(--line);stroke-width:1.2;stroke-dasharray:5 5;fill:none}
.dg-box-root{fill:var(--ours);stroke:var(--ours);stroke-width:1.5}
.dg-box-leaf{fill:var(--surface-2);stroke:var(--line-soft);stroke-width:1}
.dg-m1{fill:var(--ours-soft);stroke:var(--ours);stroke-width:1.3}
.dg-m2{fill:var(--accent-soft);stroke:var(--accent-line);stroke-width:1.3}
.dg-m3{fill:var(--accent-soft);stroke:var(--accent-line);stroke-width:1.3}
.dg-m4{fill:var(--accent-soft);stroke:var(--accent-line);stroke-width:1.3}
.dg-m5{fill:var(--hot-soft);stroke:var(--hot);stroke-width:1.3}
.dg-t3{fill:var(--ink-2);font-size:12.5px}

.note{background:var(--surface-2);border:1px solid var(--line-soft);border-left:3px solid var(--muted);
      border-radius:3px;padding:16px 20px;margin:0 0 22px;font-size:15px}
.note.key{border-left-color:var(--accent);background:var(--accent-soft)}
.note.warn{border-left-color:var(--hot);background:var(--hot-soft)}
.note.gain{border-left-color:var(--ours);background:var(--ours-soft)}
.note p:last-child{margin-bottom:0}
.note h3{margin:0 0 8px;font-size:1rem;font-weight:650}
.note ul,.note ol{margin-bottom:0}

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
.p-mid{background:var(--accent-soft);color:var(--accent);border-color:var(--accent-line)}
.tag{font-family:var(--mono);font-size:10px;padding:1px 5px;border-radius:2px;
     border:1px solid var(--line);color:var(--muted);white-space:nowrap}
footer{margin:72px 0 0;padding:22px 0 0;border-top:1px solid var(--line);
       font-family:var(--mono);font-size:11.5px;color:var(--muted);line-height:1.7}
@media (max-width:640px){.wrap{padding:0 16px 56px}figure{padding:14px 12px 12px}}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}

@media print{
  :root, :root[data-theme="dark"], :root:not([data-theme="light"]){
    --ground:#FFFFFF; --surface:#FFFFFF; --surface-2:#F7F8FA;
    --line:#C8D0D8; --line-soft:#E2E7EC;
    --ink:#101720; --ink-2:#38434F; --muted:#5E6A76;
    --accent:#A8500B; --accent-soft:#F7EDE2; --accent-line:#D8A46B;
    --hot:#A8291F; --hot-soft:#FAEAE7;
    --ours:#0B6E6C; --ours-soft:#E4F1F0;
  }
  @page{ size:A4 portrait; margin:14mm 12mm 16mm; }
  body{ background:#fff; font-size:9.6pt; line-height:1.5; }
  .wrap{ max-width:none; padding:0; }
  header{ padding-top:0; }
  h1{ font-size:22pt; } h2{ font-size:14pt; } .dek{ font-size:11pt; }
  p,li{ font-size:9.6pt; }
  svg.dg{ min-width:0 !important; width:100%; }
  figure{ padding:10px 8px 8px; }
  .scroll{ overflow-x:visible; }
  table{ font-size:8.4pt; } th,td{ padding:5px 7px; }
  section{ break-before:page; } section:first-of-type{ break-before:auto; }
  figure, table, .note{ break-inside:avoid; }
  h2, h3, .snum{ break-after:avoid; } figcaption{ break-before:avoid; }
}
'''

import cp_body

FIGS = {
    "map":       fig_map(),   "map_cap":   FIG_MAP_CAP,
    "loop":      fig_loop(),  "loop_cap":  FIG_LOOP_CAP,
    "lanes":     fig_lanes(), "lanes_cap": FIG_LANES_CAP,
    "bite":      fig_bite(),  "bite_cap":  FIG_CAP,
}

HTML = ('<!doctype html>\n<html lang="zh-CN">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="color-scheme" content="light dark">\n'
        '<title>GMGN App 产品侧打法</title>\n'
        '<style>' + CSS + '</style>\n</head>\n<body>\n<div class="wrap">\n'
        + cp_body.body(F, V, A, FIGS)
        + '\n</div>\n</body>\n</html>\n')

out = pathlib.Path(__file__).resolve().parents[1] / "gmgn-counterplay.html"
out.write_text(HTML, encoding="utf-8")
print(f"写入 {out}　{len(HTML):,} 字节")
