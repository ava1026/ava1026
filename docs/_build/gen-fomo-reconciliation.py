# -*- coding: utf-8 -*-
"""生成 Arthur v5 × GMGN 三层文档 的逐条对账表"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fomo_facts as F  # noqa: E402

# (编号, 议题, Arthur v5 的说法, 我们的说法, 关系, 证据强度, 处理)
ROWS = [
    # ── 冲突 / 待对齐 ──
    ("C1", "0.95 USDC 的性质", "SOL gas 从 $0.1 涨到 $0.95，最低卖出门槛约 $2",
     "≤200U 档的<strong>平台费</strong>，以顶层独立 <code>transferChecked</code> 打进其收费 ATA，链上可查",
     "conflict",
     "他：社群观察／未标来源<br>我们：<strong>一手抓包 + 多笔链上验证</strong>",
     "<strong>必须对齐。</strong>若是平台费，「gas 涨了导致卖不掉」的叙事站不住，对外用会被打脸。也可能两件事叠加（gas 确实涨 + 另有平台费）—— 需要一次链上复核确认"),

    ("C2", "量级排名", "同窗口同链重算：30d GMGN $2.6B ｜ FOMO $1.7B ｜ Axiom $1.6B，两窗口我们均第一",
     "引用公开报道：FOMO 已在 <strong>Solana 单链</strong>超过 Axiom 日交易量、单周收入超 Phantom / Jupiter",
     "align",
     "两边都对，但<strong>口径不同</strong>（全链交易量 vs Solana 单链 + 收入）",
     "<strong>已处理。</strong>主报告 §3.3 加了统一口径说明，并指出这与我发现的「98.5% 是 DefiLlama 测量产物」<strong>是同一个根因</strong>：DefiLlama 漏掉 FOMO 跨链收入，也漏掉我们的 Robinhood 链"),

    ("C3", "Privy 的定性", "「Privy 托管」「托管 ＝ 私钥不在用户手里」",
     "<strong>分片托管</strong>：Privy 服务端一份 share + 设备一份，签名时前端 iframe 本地重组；Privy 持 recovery share ≈ 具备全权控制",
     "conflict",
     "他：结论方向对<br>我们：<strong>一手 HAR，机制可复现</strong>",
     "<strong>对外口径必须用我们的表述。</strong>FOMO 一直讲 non-custodial，说「托管钱包」它一句话就能反驳，反显我方不专业"),

    ("C4", "费率高低", "被公开指偏高且不透明，用户拿 Pump.fun 零费与 Jupiter 对比",
     "$95 是临界点：以下我们便宜，<strong>$200–$10k 它便宜一半，$10k 以上便宜 20 倍</strong>",
     "align",
     "两者并存（用户拿它跟零费的 PF 比，不是跟我们比）",
     "<strong>对外别主动挑费率话题。</strong>我方已撤销「小额费率对比做传播物料」的 P1"),

    ("C5", "「站内战绩」的含义", "排行榜 PnL <strong>不区分</strong> transferred / bought，连上钱包展示已有仓位即可造榜",
     "原表述：「粉丝数由<strong>站内战绩</strong>决定」",
     "conflict",
     "他：<strong>claymore 私信一手确认</strong>（榜第 20 名，PnL +$278,533，仓位为转入）",
     "<strong>已修正。</strong>改为「站内<strong>表现</strong>决定」并加注：表现≠交易。离散度塌缩的结论方向不变，且被这条<strong>强化</strong> —— 影响力市场比原判断更合成"),

    # ── 互补：他有我们没有 ──
    ("A1", "拉盘是飞轮燃料", "BenTodar 亲述 PF 四步：给低市值币合约地址 → 让他先买 → 平台拉盘 → PnL 亮眼；Helen 当场确认「FOMO 不也一样」",
     "完全没有这一层",
     "add",
     "<strong>当事人亲述（最强）</strong>",
     "<strong>已并入闭环页 §01 + 新增图 2「造榜链路」。</strong>它修正了我的铰链判断：内容零边际成本，但<strong>可信度是买来的</strong>"),

    ("A2", "「渠道不能卖」的真实成因", "Dani 亲历：1万→7万，<strong>一卖即归零</strong>；退出理由「不想让别人亏钱」，99% 交易仍在 GMGN",
     "无",
     "add",
     "<strong>一手对话</strong>",
     "已并入。把「平台给渠道的约束」纠正为<strong>卖不掉</strong> —— 约束由流动性实现，不靠自觉"),

    ("A3", "24h 榜刷新是关键设计", "终身榜会被大户永久霸占；24h 刷新制造「人人都有机会」，官方转发给<strong>社交货币</strong>而非现金",
     "只写了 Leaderboard / CLANS 的存在，<strong>没抓到 24h 刷新才是动力源</strong>",
     "add",
     "交易员原话：「That's the secret sauce」",
     "<strong>建议补进获客导图的社交裂变分支。</strong>这条直接决定我们自建造星机制该抄什么"),

    ("A4", "破圈层两条子路径", "UGC 铺量（话题标签 + 模板化晒单）＋ <strong>圈外泛类博主</strong>（TikTok 泛娱乐，粉丝画像即圈外散户）；#fomoapp 实测 41 条视频三类打法",
     "KOL 矩阵只覆盖<strong>圈内 X</strong>，完全没有短视频与圈外维度",
     "add",
     "实测爬取样本",
     "<strong>我方盲区。</strong>建议补进导图的付费投放分支"),

    ("A5", "PF 的 UGC 已明码标价", "08-11 Alon 官方 Discord @everyone：$0.25/推荐 · $0.10/转发 · $0.05/评论，覆盖 X / TikTok / Instagram",
     "无",
     "add",
     "官方公告",
     "从「社交货币」升级到<strong>现金 + 分币级单价 + 全员开放</strong>。窗口在收窄"),

    ("A6", "产品债清单", "入金全面失效（<strong>德国用户看不到任何入金选项</strong>）、08-02 ToS 允许第三方未加密传输私钥、假客服已实际盗资、风控误杀 honeypot、ETH/BNB 自动 wrap 致无 gas",
     "只有「出金跳 Spritz」一条",
     "add",
     "社群监控，条目具体",
     "<strong>比我们详细得多。</strong>建议整体替换主报告 §8.3 的对应部分"),

    ("A7", "竞品同期翻车窗口", "08-12：DeBot 两轮机房故障 + 成交价严重偏离；Axiom 无法买入 / 永久封禁争议；社群已出现「Ave 与 GMGN 很少宕机」的有机口碑",
     "无",
     "add",
     "社群监控",
     "<strong>时效性强</strong>，素材现在就该做"),

    # ── 互补：我们有他没有 ──
    ("B1", "Relay 交易解析归属 bug", "完全没提",
     "<strong>P0</strong>：FOMO 买单走 Relay 代发，买入被归到 relayer，用户钱包只剩 0 金额转入 → 聪明钱转战 FOMO 后在我们这里「消失」。已立项 GMGN-8687/8688/8689",
     "mine",
     "<strong>一手，含坐实样本</strong>（BSC tx 0xed986e6a…）",
     "<strong>建议并入他的下一版。</strong>这是当前唯一正在流失专业用户信任的活口子"),

    ("B2", "技术架构拆解", "只提到 Privy 托管 + USDC 统一跨链",
     "Relay intent 桥 / EIP-7702 + ERC-4337 / feePayer 代付 / Jito 提交 / 完整供应商依赖地图 / HAR 实测时序",
     "mine", "<strong>一手 HAR + 7 笔样本</strong>",
     "支撑「USDC 统一跨链＝速度天花板」这个判断的<strong>底层证据</strong>，他的观察哨 ③ 需要它"),

    ("B3", "费率三档与临界点", "只说「偏高且不透明」",
     "≤200U 固定 0.95／200–10k 0.5%／≥10k 0.05%，与我们 1% 的临界点 <strong>$95</strong>，完整对照表",
     "mine", "<strong>链上多笔实测</strong> + 我方费率三处内部资料互证",
     "定价决策的<strong>唯一量化依据</strong>"),

    ("B4", "收入可实时监控", "无",
     "Solana 收费钱包 <code>HrTf9CzX…XcSq</code> 净流入即 FOMO 收入的实时代理指标",
     "mine", "一手",
     "比等第三方报道<strong>快一周</strong>，建议做成日报"),

    ("B5", "影响力放大与离散度塌缩", "无（但 A5 transferred 事实<strong>修正了这条的解读</strong>）",
     "X 粉丝跨度 10.7× → FOMO 粉丝跨度仅 2.8×；倍数与 X 粉丝量成反比",
     "mine", "X 抓取二手，n=5，<strong>有选择偏差</strong>",
     "结论方向被他强化，但样本质量弱于他的一手对话。<strong>两条合起来才完整</strong>"),

    ("B6", "资本与规模", "无",
     "$550M 估值 / 累计 $94M / Index·USV·Benchmark；625k 用户；周收入 ATH $2.64M",
     "mine", "公开报道，已标未审计",
     "补充背景，他的 deck 不需要"),

    # ── 一致 ──
    ("D1", "CLANS / social perps 上线", "已提及并列为它在补短板的动作", "已记录（CLANS 8/10 上线，50+）",
     "same", "双方独立观察一致", "无需处理"),
    ("D2", "出金受限、导出私钥去 Phantom", "官方建议导出私钥去 Phantom，把用户往外推", "同，且列为漏损点之一",
     "same", "双方一致", "<strong>他多一层洞察</strong>：出口已经开了，我方应做迁移引导落地页"),
    ("D3", "25% referral 分佣", "社交层内建，产内容本身有收益", "卖出侧 75/25 拆分，链上实测",
     "same", "他讲机制，我们有链上证据", "互为佐证"),
    ("D4", "弱化链概念 / 首页极简", "它的产品设计选择，已被验证可抄", "同（获客导图「产品即获客」分支）",
     "same", "一致", "Ava 排期第 ③ 条已在做"),
    ("D5", "分层共存但边界会移动", "FOMO 是社交涨粉工具、GMGN 是交易工具；但迁移是双向的，<strong>不是护城河</strong>",
     "同：巨鲸迁移需量化监控（待验证队列 #17）", "same", "一致，他的现场证据更强",
     "他的表述更准：<strong>当前均衡 ≠ 护城河</strong>"),
]

REL = {
    "conflict": ("冲突", "p-hi"),
    "align":    ("待统一口径", "p-mid"),
    "add":      ("他有·我无", "p-add"),
    "mine":     ("我有·他无", "p-us"),
    "same":     ("一致", "p-lo"),
}

def rows_html():
    out = []
    for num, topic, theirs, ours, rel, ev, action in ROWS:
        label, cls = REL[rel]
        out.append(
            f'<tr><td class="num">{num}</td><td><strong>{topic}</strong></td>'
            f'<td>{theirs}</td><td>{ours}</td>'
            f'<td><span class="pill {cls}">{label}</span></td>'
            f'<td>{ev}</td><td>{action}</td></tr>')
    return "\n      ".join(out)

def counts():
    from collections import Counter
    c = Counter(r[4] for r in ROWS)
    return c

C = counts()

HTML = f'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>FOMO 情报对账表</title>
<style>
:root{{
  --ground:#EDF0F3; --surface:#FFFFFF; --surface-2:#F5F7F9;
  --line:#D3DAE1; --line-soft:#E3E8ED;
  --ink:#121820; --ink-2:#3A4551; --muted:#66727F;
  --accent:#A8500B; --accent-soft:#F3E3D2; --accent-line:#D8A46B;
  --hot:#A8291F; --hot-soft:#F6DEDA;
  --ours:#0B6E6C; --ours-soft:#D9EDEC;
  --add:#5B3FA8; --add-soft:#EAE3F7; --add-line:#A48CD8;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Songti SC",serif;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,monospace;
}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{
  --ground:#0E1319; --surface:#151C24; --surface-2:#1B242E;
  --line:#2C3945; --line-soft:#222C37;
  --ink:#E6EBF0; --ink-2:#BCC7D2; --muted:#8695A3;
  --accent:#E9A44C; --accent-soft:#33261A; --accent-line:#7A5828;
  --hot:#EE8378; --hot-soft:#3A1F1C;
  --ours:#54C9C4; --ours-soft:#123331;
  --add:#B49BEC; --add-soft:#241C38; --add-line:#5B4A86;
}}}}
:root[data-theme="dark"]{{
  --ground:#0E1319; --surface:#151C24; --surface-2:#1B242E;
  --line:#2C3945; --line-soft:#222C37;
  --ink:#E6EBF0; --ink-2:#BCC7D2; --muted:#8695A3;
  --accent:#E9A44C; --accent-soft:#33261A; --accent-line:#7A5828;
  --hot:#EE8378; --hot-soft:#3A1F1C;
  --ours:#54C9C4; --ours-soft:#123331;
  --add:#B49BEC; --add-soft:#241C38; --add-line:#5B4A86;
}}
*,*::before,*::after{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);
     font-size:15px;line-height:1.65;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1400px;margin:0 auto;padding:0 22px 72px}}
header{{padding:46px 0 22px;border-bottom:2px solid var(--ink);margin-bottom:24px}}
.kicker{{font-family:var(--mono);font-size:10.5px;letter-spacing:.17em;text-transform:uppercase;
        color:var(--accent);margin:0 0 12px}}
h1{{font-family:var(--serif);font-weight:600;font-size:clamp(1.9rem,4.4vw,2.6rem);
   line-height:1.13;letter-spacing:-.015em;margin:0 0 12px}}
.dek{{font-family:var(--serif);font-size:clamp(1.02rem,2vw,1.18rem);line-height:1.58;
     color:var(--ink-2);margin:0;max-width:70ch}}
h2{{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;
   color:var(--accent);margin:34px 0 13px;display:flex;align-items:center;gap:11px}}
h2::after{{content:"";flex:1;height:1px;background:var(--line)}}
p{{margin:0 0 14px;max-width:78ch}}
strong{{font-weight:650;color:var(--ink)}}
code{{font-family:var(--mono);font-size:.85em;background:var(--surface-2);
     border:1px solid var(--line-soft);border-radius:2px;padding:1px 5px;word-break:break-all}}
.metrics{{display:grid;gap:1px;background:var(--line);
        grid-template-columns:repeat(auto-fit,minmax(132px,1fr));
        border:1px solid var(--line);border-radius:3px;overflow:hidden;margin:0 0 26px}}
.metric{{background:var(--surface);padding:14px 16px}}
.metric .v{{font-family:var(--mono);font-size:1.5rem;font-weight:600;
          font-variant-numeric:tabular-nums;display:block;line-height:1.15}}
.metric .k{{display:block;font-size:11.5px;color:var(--muted);margin-top:5px;line-height:1.4}}
.scroll{{overflow-x:auto;margin:0 0 22px;border:1px solid var(--line);border-radius:3px;background:var(--surface)}}
table{{border-collapse:collapse;width:100%;font-size:13px;line-height:1.55;min-width:1180px}}
th,td{{padding:11px 13px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line-soft)}}
thead th{{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;
        color:var(--muted);font-weight:600;background:var(--surface-2);
        border-bottom:1px solid var(--line);white-space:nowrap;position:sticky;top:0}}
tbody tr:last-child td{{border-bottom:none}}
td.num{{font-family:var(--mono);font-weight:600;color:var(--accent);white-space:nowrap}}
.pill{{display:inline-block;font-family:var(--mono);font-size:10px;font-weight:600;
     padding:3px 7px;border-radius:2px;white-space:nowrap;border:1px solid transparent}}
.p-hi{{background:var(--hot-soft);color:var(--hot);border-color:var(--hot)}}
.p-mid{{background:var(--accent-soft);color:var(--accent);border-color:var(--accent-line)}}
.p-us{{background:var(--ours-soft);color:var(--ours);border-color:var(--ours)}}
.p-add{{background:var(--add-soft);color:var(--add);border-color:var(--add-line)}}
.p-lo{{background:var(--surface-2);color:var(--muted);border-color:var(--line)}}
.note{{background:var(--surface-2);border:1px solid var(--line-soft);
     border-left:3px solid var(--muted);border-radius:3px;padding:15px 19px;
     margin:0 0 20px;font-size:14.5px}}
.note.alert{{border-left-color:var(--hot);background:var(--hot-soft)}}
.note.gain{{border-left-color:var(--ours);background:var(--ours-soft)}}
.note.add{{border-left-color:var(--add);background:var(--add-soft)}}
.note h3{{margin:0 0 8px;font-size:1rem;font-weight:650}}
.note p:last-child{{margin-bottom:0}}
ul{{margin:0 0 14px;padding-left:21px;max-width:78ch}}
li{{margin:0 0 8px}}
li::marker{{color:var(--accent)}}
footer{{margin:56px 0 0;padding:20px 0 0;border-top:1px solid var(--line);
       font-family:var(--mono);font-size:11px;color:var(--muted);line-height:1.7}}
@media (max-width:640px){{.wrap{{padding:0 15px 48px}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}}}
</style>
</head>
<body>
<div class="wrap">

<header>
  <p class="kicker">Arthur v5 × GMGN 三层文档 · 逐条对账 · {F.AS_OF}</p>
  <h1>两份 FOMO 分析的对账表</h1>
  <p class="dek">Arthur 打的是<strong>增长机制与渠道网络</strong>，我们打的是<strong>技术架构与产品事实</strong>。<strong>互补远大于重叠</strong> —— 但有 5 处必须对账，其中 3 处是真冲突。</p>
</header>

<div class="metrics">
  <div class="metric"><span class="v" style="color:var(--hot)">{C["conflict"]}</span><span class="k">真冲突<br>需要裁决</span></div>
  <div class="metric"><span class="v" style="color:var(--accent)">{C["align"]}</span><span class="k">口径不同<br>需统一表述</span></div>
  <div class="metric"><span class="v" style="color:var(--add)">{C["add"]}</span><span class="k">他有我无<br>应并入</span></div>
  <div class="metric"><span class="v" style="color:var(--ours)">{C["mine"]}</span><span class="k">我有他无<br>建议给他</span></div>
  <div class="metric"><span class="v" style="color:var(--muted)">{C["same"]}</span><span class="k">一致<br>互为佐证</span></div>
</div>

<div class="note alert">
  <h3>三处真冲突，按优先级</h3>
  <p><strong>C1 · 0.95 USDC 是 gas 还是平台费</strong> —— 两份文档给了两种解释，<strong>不可能都对</strong>。我们这侧是链上多笔实测（顶层 <code>transferChecked</code> 打进其收费 ATA），他那侧未标来源。若确为平台费，「SOL gas 涨了导致卖不掉」这个叙事站不住，<strong>对外用会被打脸</strong>。</p>
  <p><strong>C3 · Privy 是「托管」还是「分片托管」</strong> —— 结论方向一致（Privy 实际具备全权控制），但机制表述必须用我们的：FOMO 对外一直讲 non-custodial，说「托管钱包」它一句话就能反驳。</p>
  <p><strong>C5 · 「站内战绩」的含义</strong> —— 他的 claymore 一手证据推翻了我的措辞。<strong>已修正</strong>，且这条<strong>强化</strong>了我的结论：影响力市场比原判断更合成。</p>
</div>

<div class="note add">
  <h3>他带来的最重要一层：飞轮的燃料</h3>
  <p>我的闭环把铰链定为「交易即内容、零边际成本」。他的 A1／A2 补上了关键前提：<strong>内容零成本，但可信度是花钱造出来的</strong> —— 平台出资拉盘 → 种子交易员低价进场 → 人为拉升 → 亮眼 PnL 上榜。</p>
  <p>由此得出的修正：<strong>渠道端边际成本≈0，但平台端不是。</strong>渠道不拿现金只拿确定性与曝光，可规模化；平台仍要自己出手拉盘，<strong>这笔 MM 钱至今没人算过</strong>。</p>
  <p style="color:var(--add)"><strong>已并入闭环页 §01，并新增「图 2 · 造榜链路」。</strong></p>
</div>

<h2>逐条对账</h2>
<div class="scroll">
<table>
  <thead><tr>
    <th class="num">#</th><th>议题</th><th>Arthur v5 的说法</th><th>我们的说法</th>
    <th>关系</th><th>证据强度</th><th>处理</th>
  </tr></thead>
  <tbody>
      {rows_html()}
  </tbody>
</table>
</div>

<h2>已经动手的三件</h2>
<div class="note gain">
  <ul>
    <li><strong>并入闭环页</strong>（A1／A2／C5）：§01 新增「铰链的前提」小节 + <strong>图 2 造榜链路</strong>；§04 新增 transferred/bought 一节；「站内战绩」改为「站内表现」并加注。</li>
    <li><strong>统一量级口径</strong>（C2）：主报告 §3.3 新增口径说明，指出 DefiLlama 漏链<strong>两边都中招</strong> —— 漏 FOMO 跨链收入，也漏我们的 Robinhood 链。「98.5% 来自 Solana」与「Axiom 第一」是同一个测量缺陷的两面。</li>
    <li><strong>本对账表</strong>：{len(ROWS)} 条交叉点全部标注关系、证据强度与处理方式。</li>
  </ul>
</div>

<h2>建议下一步</h2>
<div class="note">
  <p><strong>给他的三条</strong>：B1 Relay 解析 bug（P0，他完全没提）、B2 技术架构（支撑他观察哨 ③ 的底层证据）、B3 费率对照（定价决策的唯一量化依据）。</p>
  <p><strong>要他确认的一条</strong>：C1 的 0.95 到底是 gas 还是平台费 —— 这条不澄清，两份文档对外说法会互相矛盾。</p>
  <p><strong>我方待补的三条</strong>：A3 24h 榜刷新机制（决定自建造星该抄什么）、A4 短视频与圈外维度（我方盲区）、A6 产品债细节（他比我们详细得多）。</p>
</div>

<footer>
  对账基准：Arthur《FOMO 增长与产品机制拆解及 GMGN 应对计划》v5（2026-08-13）
  × GMGN 三层文档（决策简报 / 增长闭环 / 全面产品调研）。<br>
  数字取自单一事实源 <code>docs/_build/fomo_facts.py</code>。竞品情报，内部使用。
</footer>

</div>
</body>
</html>
'''

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "fomo-reconciliation.html")
open(out, "w", encoding="utf-8").write(HTML)
print("written:", len(HTML), "bytes ->", out)
print("rows:", len(ROWS), dict(C))
