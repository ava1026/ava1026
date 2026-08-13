# -*- coding: utf-8 -*-
"""
把《GMGN App 产品侧打法》渲染成 Confluence HTML body。

为什么要单独一份：Artifact 页面没有服务端保存（平台只开放 downloads / mcp），
做不到「线上改、实时存、别人打开就是新版」。Confluence 原生支持这三件事。

用法：
    python3 docs/_build/gen-confluence-counterplay.py > /tmp/body.html
然后用 MCP 的 createConfluencePage / updateConfluencePage 推上去（contentFormat=html）。

限制：Confluence 不吃内联 SVG，四张矢量图留在 Artifact 版；
本页把闭环图与导图降级为原生表格 / 嵌套列表——好处是它们也能被在线编辑。
数字仍从 fomo_facts 注入，改数字改那里。
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import fomo_facts as F

V, A, P = F.V8, F.ARTHUR, F.PUSH
ART = F.DOCS["play"][1]


def st(label, color):
    return f'<span data-type="status" data-color="{color}">{label}</span>'


OK   = lambda: st("已上线", "green")
GO   = lambda: st("推进中", "blue")
NEW  = lambda: st("新增", "purple")
Q    = lambda: st("本季度", "neutral")
HOLD = lambda: st("待调研", "green")
CHK  = lambda: st("待核", "red")
PRE  = lambda: st("前置", "yellow")


def table(headers, rows, widths=None):
    ws = widths or []
    cells = []
    for i, h in enumerate(headers):
        attr = ' data-colwidth="%s"' % ws[i] if i < len(ws) else ""
        cells.append("<th%s><p>%s</p></th>" % (attr, h))
    head = "".join(cells)
    body = ""
    for r in rows:
        body += "<tr>" + "".join(f"<td><p>{c}</p></td>" for c in r) + "</tr>"
    return (f'<table data-layout="default"><thead><tr>{head}</tr></thead>'
            f'<tbody>{body}</tbody></table>')


def panel(kind, html):
    return f'<div data-type="panel-{kind}">{html}</div>'


BODY = f"""
{panel("info",
  "<p><strong>这是可在线编辑的版本。</strong>直接在本页改，Confluence 自动保存，"
  f"所有人打开就是最新版。带四张矢量图的只读版见 "
  f'<a href="{ART}">Artifact 图文版</a>——那边不能保存改动。</p>'
  f"<p>数据截至 {F.AS_OF}。数字统一取自仓库 <code>docs/_build/fomo_facts.py</code>，"
  "本页由 <code>gen-confluence-counterplay.py</code> 生成；"
  "<strong>手动改动不会被覆盖，但重新生成时会——大改请同步回仓库。</strong></p>")}

<p><strong>定位不动：专业交易能力与专业交易员是主导区。</strong>App 侧重<strong>发现层</strong>——第一时间发现热门币，放大其中 KOL 与大户的真实持仓，降低门槛，把圈外小白与链上新用户拉进来。</p>

<h2>01 — 全局：五个模块怎么转起来</h2>

{table(["①发现", "②放大", "③拉新承接", "④交易"],
       [["热门币第一时间抓到并推出", "KOL 与大户的真实持仓",
         "法币入金 · Apple Pay · USDC · 迁移引导", "专业执行 · 参数可控"]])}

<p>④ 的链上数据<strong>回流</strong>到 ①，让下一轮「什么在热、谁在赚」更准——环就是这样合上的。</p>


<h3>每个模块里装什么</h3>
<ul>
  <li><strong>定位</strong>
    <ul>
      <li>专业交易能力与专业交易员：主导区，不让</li>
      <li>按环节切不同人群：发现给新客，执行与分析守专业</li>
    </ul>
  </li>
  <li><strong>发现层</strong>
    <ul>
      <li>热门代币第一时间发现 → 推出 → 到达</li>
      <li>热门精选 push（已上线，质量闸比 FOMO 稳健）</li>
      <li>Callout 对标 FOMO thesis（推进中）</li>
      <li>热门列表混链整合：弱化链 · 更稳健的币（推进中）</li>
      <li>新用户第一屏＝热门榜单，不是交易面板</li>
    </ul>
  </li>
  <li><strong>放大层</strong>
    <ul>
      <li>热门币里的 KOL 持仓</li>
      <li>大户持仓与动向</li>
      <li>赚钱效应：链上可验真，不是造出来的</li>
      <li>FOMO Leaderboard —— 重算，不镜像</li>
    </ul>
  </li>
  <li><strong>拉新与承接</strong>
    <ul>
      <li>降低门槛，拉小白用户进来</li>
      <li>法币入金（已支持 50+ 国家）</li>
      <li>Apple Pay 直购 meme 代币（待调研）</li>
      <li>USDC 交易：新用户充 USDC，默认本链 USDC 模式（推进中）</li>
      <li>USDC 自动跨链：非华语新用户，不进老用户主路径（新增调研）</li>
      <li>迁移引导：一键导入私钥 / 接管持仓</li>
    </ul>
  </li>
  <li><strong>地基</strong>
    <ul>
      <li>Relay 交易解析　GMGN-8687 / 8688 / 8689 / 8665</li>
      <li>relay 数据的标注与可信度规范</li>
      <li>推送延迟 6–20min〔待核〕—— 拦着「第一时间」</li>
      <li>客服口径 —— 与 FOMO 被并列批评</li>
    </ul>
  </li>
</ul>

<h2>02 — 定位：按环节切不同人群</h2>

{table(["环节", "人群", "归属", "抓手"],
       [["<strong>发现</strong>", "圈外小白 · 链上新用户 · 打二段用户", "App 主轴",
         "热门混链 · push · callout。<strong>同时是拉新入口</strong>"],
        ["<strong>执行</strong>", "专业交易员 · 高意图执行用户", "App 与 Web 都保专业深度",
         "参数可控 · 真限价 · 止盈止损"],
        ["<strong>深度分析</strong>", "专业交易员 · Web3 老手", "Web 为主",
         "数据看板 · 钱包画像 · 资金关系"]])}


<h2>03 — 发现层：第一时间发现，推到用户面前</h2>

{table(["动作", "状态", "要点"],
       [["<strong>热门精选代币 push</strong>", OK(),
         f"我们有质量闸，实测覆盖 {P['our_coverage']}、{P['our_earlier']} 币首触更早；"
         f"FOMO {P['their_coverage']} 且无质量闸"],
        ["<strong>Callout 全方位铺开</strong>", GO(),
         "对标 FOMO thesis。K 线页 / 单人单币页 / 持仓页，监控默认推全局"],
        ["<strong>热门列表混链整合</strong>", GO(),
         "1. 弱化链概念<br />2. 更稳健的代币，给<strong>打二段用户</strong>与"
         "<strong>链上新用户</strong>，风险低"],
        ["<strong>新用户第一屏＝热门榜单</strong>", Q(), "不是交易面板"],
        [f"<strong>我们自己的推送延迟</strong>：{V['push_delay']}", CHK(),
         "对比 Dexscreener 近实时（不是对比 FOMO）。v8 列为最高优先级但未给测量来源，"
         "<strong>先测出真实数字再决定要不要立项</strong>"]])}

<h2>04 — 放大层：放大真实的赚钱效应</h2>

{table(["动作", "状态", "要点"],
       [["<strong>热门币里的 KOL 持仓</strong>", Q(), "谁在拿、拿多少、什么时候进的"],
        ["<strong>大户持仓与动向</strong>", Q(),
         "接到热门列表与代币页，作为「为什么它热」的解释"],
        ["<strong>FOMO Leaderboard</strong>", NEW(), "见下"],
        ["relay 数据标注与可信度规范", PRE(), "上面三条的合规底座"]])}

<h3>FOMO Leaderboard：重算，不镜像</h3>
<p>它一条解决三件事：满足用户对 FOMO 钱包的追踪需求、堵住「为看榜去装 FOMO」的流失、拆解它的造富效应。</p>
<p>机制事实是<strong>{A['leaderboard']}</strong>，所以直接搬数字等于替它背书——每行按我们的口径拆成<strong>站内买入 / 外部转入 / 关联钱包内转</strong>，PnL 默认只算买入部分。</p>


<p><strong>一手样本：</strong>claymore（@claymorepx）确认是 {A['claymore_rank']}、PnL {A['claymore_pnl']}，而{A['claymore_fact']}。<em>v8 要求保留</em>：他自述动机是移动端体验好、社交曝光强，引用时这句不能省。</p>

<h2>05 — 拉新与承接：降低门槛，拉小白用户进来</h2>

{table(["动作", "状态", "要点"],
       [["<strong>法币入金</strong>", OK(),
         "已经支持 50+ 个国家法币入金。新链上的天然优势：新链没有原生资产存量，用户无从入金"],
        ["<strong>Apple Pay 直接购买 meme 代币</strong>", HOLD(),
         "提升圈外用户第一笔交易成功率"],
        ["<strong>USDC 交易</strong>", GO(),
         "<strong>新用户充USDC - 默认本链开USDC交易模式</strong>"],
        ["USDC自动跨链交易", st("新增调研", "red"),
         "非华语新用户进此流程，不进老用户主路径"],
        ["<strong>迁移引导路径</strong>", NEW(),
         "一键导入私钥 / 接管持仓 / 落地页。出口是它自己开的——"
         "官方建议用户「导出私钥到 Phantom 操作」"]])}


<h3>跨链调研清单</h3>
<ol>
  <li>relay 分发延迟实测 p50 / p95，对比我们的{V['our_path']}。<em>08-13 已核实</em>：它是{V['relay_path']}，多一跳</li>
  <li>哪些链 / 代币 relay 报价源覆盖不到（内盘、新链）</li>
  <li>失败或卡单时的资金状态——FOMO 用户投诉的「资金冻结 1–3 工作日」是不是 relay 带来的</li>
  <li>与 Relay 的商务条款。它是 FOMO 的单点依赖，也该是我们的谈判杠杆</li>
</ol>

<h2>06 — 地基：四条在拦着上面的模块</h2>

{table(["地基", "拦着谁", "要点"],
       [["<strong>Relay 交易解析</strong><br />GMGN-8687 / 8688 / 8689 / 8665",
         "FOMO Leaderboard · 迁移引导 · 进场点位",
         "买单走 relay 代发，用户钱包只出现在最后一跳，买入被记在 relayer 名下。"
         "改按「路由合约收币后转给谁」定归属。Debot / basedbot 已能解析"],
        ["<strong>标注与可信度规范</strong>", "放大层全部",
         "无法识别投毒，所有 relay 来源数据都要带提示。产品侧交付物"],
        [f"<strong>我们自己的推送延迟</strong>：{V['push_delay']}",
         "发现层 · 所有「快」的叙事",
         "数字来自 v8，未给测量来源。<strong>先测，不要直接当事实排期</strong>"],
        ["<strong>客服口径</strong>", "执行可靠性叙事",
         "它的「清缓存 / 切节点」已被用户与我们的「检查 ms / fps / 切代理」并列批评"]])}

<h2>07 — 打：它的四个结构性短板</h2>

{table(["咬合点", "它为什么跟不了"],
       [["<strong>① 榜单重算</strong>",
         "区分 transferred / bought 并追资金关系需要自研数据管线，"
         "而它路由 / 跨链 / 密钥 / 出入金全外包——<strong>审计不了自己</strong>"],
        ["<strong>② 进场点位</strong>",
         "Relay 只询价标准 AMM，未毕业代币无法交易，它的用户"
         "<strong>结构性地只能毕业后进场</strong>——恰好对上它口碑里「总在当退出流动性」"],
        ["<strong>③ 三件事一道墙</strong>",
         "真自动跟单 / 真限价 / 止盈止损都要平台代用户签名，"
         "而 Privy 分片密钥必须前端本地重组，用户不在场签不了。"
         "<br /><em>口径</em>：只说「它的跟单需要手动确认」，<strong>不说「它没有跟单」</strong>"],
        ["<strong>④ 资金进出</strong>",
         f"卖不出（gas {V['gas_bump']} 后门槛{V['sell_floor']}，小仓位死锁）· "
         f"入不进 · 拿不走（{V['withdraw_only']}）"]])}


<h2>08 — 并稿：v8 里属于产品侧的七条</h2>

{table(["v8 内容", "对产品做法的影响"],
       [["<strong>三个功能卡在同一道墙上</strong>",
         "从「多一个功能」升级为「它的架构给不了」，素材保质期变长 → §07 ③"],
        ["<strong>债在资金进出，不在速度</strong>",
         "原来只盯出金复杂（体验），真正结构性的是小仓位卖不掉（死锁）→ §05、§07 ④"],
        [f"<strong>速度机制被核实</strong>（08-13）",
         f"{V['relay_path']}，「快」有了机制解释，并直接决定 USDC 边界 → §05"],
        [f"<strong>它在主动补短板</strong>，但 {V['they_cant']}",
         "给「窗口期 vs 结构性」一个来自对手行为的验证 → §07"],
        ["<strong>用链上数据审计跟单质量</strong>",
         "与 FOMO Leaderboard 同向：<strong>我们的社交层卖可信度，不是 feed 形态</strong>"],
        [f"<strong>托管信任危机</strong>：{V['tos_date']} {V['tos_risk']}",
         "攻自托管从技术论证升级为它自己写的条款，"
         "<strong>但只给 KOL 号，官方文案不碰</strong>"],
        ["<strong>「清缓存 / 切节点」被与我们并列批评</strong>", "这是我们自己的债 → §06"]])}

<p>未提取：增长线与渠道线归 v8 主线，本页不重复排优先级。</p>

<h2>09 — 三件要定，四件要核</h2>

<h3>要定</h3>
{table(["事项", "建议", "时机"],
       [["USDC relay 的边界", "限新用户 × 限热门代币；老用户主路径 relay 占比 = 0 且可监控",
         st("内部过稿前", "red")],
        ["FOMO Leaderboard 的呈现口径", "重算，不镜像；数据服务，不是打假", st("立项时", "red")],
        ["Relay 解析的定性",
         "从「P0 止血」改为「放大层与承接层的前置条件」——排期即启动时间", st("本周", "red")]])}

<h3>要核</h3>
{table(["事项", "为什么会改结论"],
       [["<strong>FOMO 的 Apple Pay 是否已移除</strong>",
         f"外部仍列为它最强护城河（约 {F.SCALE['first_time_buyers']} 首次买币 / "
         f"约 {F.SCALE['first_time_value']}），我方 08-13 产品债清单说疑似已移除。"
         "若属实，它「零门槛进人」这一环结构性倒退"],
        ["<strong>我们法币入金的链覆盖</strong>",
         "已确认：50+ 国家（Ava 08-13）；Apple Pay 直购不支持，待调研。"
         "剩一问：<strong>覆盖哪些链</strong>——它决定「新链天然优势」能不能对外讲，"
         "也决定主报告 §9「入金门槛 ❌ FOMO 明显领先」那行怎么改"],
        ["<strong>持仓来源解析的多链准确率</strong>",
         "「重算」建立在能可靠区分 transferred / bought 上；没量化前不要对外承诺「可验真」"],
        ["<strong>我们自己的推送延迟到底是多少</strong>",
         "v8 把「修 6–20min 延迟」列为产品线最高优先级但未给测量来源，App PM 也不认这个数。"
         "它决定「第一时间」这条主线能不能讲"]])}


<hr />
<p><em>文档矩阵：</em>
<a href="{F.DOCS['brief'][1]}">{F.DOCS['brief'][0]}</a> ·
<a href="{F.DOCS['loop'][1]}">{F.DOCS['loop'][0]}</a> ·
<a href="{F.DOCS['full'][1]}">{F.DOCS['full'][0]}</a> ·
<a href="{ART}">本文图文版</a>　|
v8 主线管增长与渠道，本页管产品，主报告 §10.2 管防守。</p>
"""

if __name__ == "__main__":
    sys.stdout.write(BODY)
