# -*- coding: utf-8 -*-
"""
《GMGN App 产品侧打法》正文。

模块划分照 Ava 08-13 的口述结构：
    定位 → 发现层 → 放大层 → 拉新与承接 → 地基
每个模块一张表，一行一个动作，不写长段落。
"""


def body(F, V, A, FIG):
    return f'''
<header>
  <p class="kicker">竞品情报 · FOMO 系列 · 产品侧 · 内部使用 · {F.AS_OF} 起算</p>
  <h1>GMGN App 产品侧打法</h1>
  <p class="dek"><strong>定位不动：专业交易能力与专业交易员是我们的主导区。</strong>App 的侧重点放在<strong>发现层</strong>——第一时间发现热门币并推到用户面前，放大其中 KOL 与大户的<strong>真实</strong>持仓与赚钱效应，把<strong>链上新用户</strong>拉进来。</p>
</header>

<section id="s1">
  <p class="snum">01 — 全局</p>
  <h2>五个模块，一张图</h2>
  <figure>{FIG["map"]}<figcaption>{FIG["map_cap"]}</figcaption></figure>
</section>

<section id="s2">
  <p class="snum">02 — 定位</p>
  <h2>不按人群切，按环节切</h2>

  <div class="scroll">
  <table>
    <thead><tr><th>环节</th><th>归属</th><th>面向</th></tr></thead>
    <tbody>
      <tr><td><strong>发现</strong></td><td>App 主轴</td><td>全体，也是拉新入口</td></tr>
      <tr><td><strong>执行</strong></td><td>App 与 Web 都保专业深度</td><td>参数可控 · 真限价 · 止盈止损</td></tr>
      <tr><td><strong>深度分析</strong></td><td>Web 为主</td><td>专业交易员</td></tr>
    </tbody>
  </table>
  </div>

  <div class="note key">
    <p><strong>这条回答了 v8 的待裁决 ①。</strong>那三个选项（分端定位 / 加社交层 / 分层不分家）都在争「服务小白还是专业」。<strong>按环节切就不用二选一</strong>——发现层天然对新用户友好，执行层天然对专业用户友好，同一个 App 不冲突，也不必放弃主导区。</p>
  </div>
</section>

<section id="s3">
  <p class="snum">03 — 发现层</p>
  <h2>第一时间发现，推到用户面前</h2>

  <div class="scroll">
  <table>
    <thead><tr><th>动作</th><th>状态</th><th>要点</th></tr></thead>
    <tbody>
      <tr><td><strong>热门精选代币 push</strong></td><td><span class="pill p-us">已上线</span></td><td>比 FOMO 稳健：我们有质量闸；实测覆盖 {F.PUSH["our_coverage"]}、{F.PUSH["our_earlier"]} 个币首触更早，FOMO 是 {F.PUSH["their_coverage"]} 且无质量闸（BSC 对倒盘、代币化股票会误触）</td></tr>
      <tr><td><strong>Callout 全方位铺开</strong></td><td><span class="pill p-mid">推进中</span></td><td>直接对标 FOMO thesis。K 线页 / 单人单币页 / 持仓页，监控默认推全局 callout</td></tr>
      <tr><td><strong>热门列表混链整合</strong></td><td><span class="pill p-mid">推进中</span></td><td>弱化链概念（FOMO 已验证该方向），与热搜差异互补，解决金狗在首页找不到</td></tr>
      <tr><td><strong>新用户默认推热门榜单</strong></td><td><span class="pill p-mid">本季度</span></td><td>App 端新用户的第一屏＝热门，不是交易面板</td></tr>
      <tr><td>推送延迟 {V["push_delay"]}</td><td><span class="pill p-hi">拦路</span></td><td>对比 Dexscreener 近实时。<strong>不修，「第一时间」这四个字站不住</strong></td></tr>
    </tbody>
  </table>
  </div>
</section>

<section id="s4">
  <p class="snum">04 — 放大层</p>
  <h2>放大真实的赚钱效应</h2>

  <figure>{FIG["lanes"]}<figcaption>{FIG["lanes_cap"]}</figcaption></figure>

  <div class="scroll">
  <table>
    <thead><tr><th>动作</th><th>状态</th><th>要点</th></tr></thead>
    <tbody>
      <tr><td><strong>热门币里的 KOL 持仓</strong></td><td><span class="pill p-mid">本季度</span></td><td>谁在拿、拿了多少、什么时候进的</td></tr>
      <tr><td><strong>大户持仓与动向</strong></td><td><span class="pill p-mid">本季度</span></td><td>接到热门列表与代币页，作为「为什么它热」的解释</td></tr>
      <tr><td><strong>FOMO Leaderboard</strong></td><td><span class="pill p-us">新增</span></td><td>见下方</td></tr>
      <tr><td>relay 数据标注与可信度规范</td><td><span class="pill p-hi">前置</span></td><td>上面三条的合规底座，见 §06</td></tr>
    </tbody>
  </table>
  </div>

  <div class="note gain">
    <h3>FOMO Leaderboard —— 这条是最锋利的一个</h3>
    <p>它同时解决三件事：<strong>①</strong> 满足现有 GMGN 用户对 FOMO 用户钱包的追踪需求；<strong>②</strong> 用户不必为了看那个榜去装 FOMO——堵住一条正在发生的流失路径；<strong>③</strong> 拆解它的造富效应，把我们的数据看板变成入口。</p>
    <p><strong>关键是「重算」，不是「镜像」。</strong>直接搬它的数字等于替它做背书。机制事实：<strong>{A["leaderboard"]}</strong>——所以我们按自己的口径重算，每一行拆出<strong>站内买入 / 外部转入 / 关联钱包内转</strong>，PnL 默认只算买入部分。</p>
    <p>一手样本：claymore（@claymorepx）确认自己是 {A["claymore_rank"]}、PnL {A["claymore_pnl"]}，而{A["claymore_fact"]}。<span class="tag">v8 要求保留</span> 他自述动机是移动端体验好、社交曝光强，不完全是被动配合平台策略——引用时这句不能省。</p>
  </div>

  <div class="note warn">
    <p><strong>两条红线。</strong>（一）呈现为<strong>数据服务，不是打假</strong>：只陈列链上事实，让用户自己得结论；口径是「它的榜不区分来源」，不是「它造假」。（二）我们目前把 relay 交易解析为「转入/转出」而非「买/卖」，是因为<strong>无法识别投毒</strong>（对方已把投毒金额提到 50~100U）——所以这个榜<strong>必须带来源标注与可信度提示</strong>，不能当成用户的真实战绩直接展示。</p>
  </div>
</section>

<section id="s5">
  <p class="snum">05 — 拉新与承接</p>
  <h2>客源是链上新用户，不是圈外小白</h2>

  <div class="scroll">
  <table>
    <thead><tr><th>动作</th><th>状态</th><th>要点</th></tr></thead>
    <tbody>
      <tr><td><strong>法币入金</strong></td><td><span class="pill p-us">已支持</span></td><td><strong>新链上的天然优势</strong>：新链没有原生资产存量，用户无从入金——我们这条通道直接跨过去。见待核 ②</td></tr>
      <tr><td><strong>热门代币支持 USDC 购买</strong></td><td><span class="pill p-mid">本季度</span></td><td><strong>限新用户</strong>。见下方边界</td></tr>
      <tr><td>跨链</td><td><span class="pill p-hi">待调研</span></td><td>调研清单见下方，不进老用户主路径</td></tr>
      <tr><td><strong>迁移引导路径</strong></td><td><span class="pill p-us">新增</span></td><td>一键导入私钥 / 一键接管持仓 / 落地页。<strong>出口是它自己开的</strong>：官方在两处高优主题里建议用户「导出私钥到 Phantom 操作」</td></tr>
    </tbody>
  </table>
  </div>

  <div class="note key">
    <h3>USDC 的边界：为什么限定在「已经热门的代币」是对的</h3>
    <p>热门币＝已毕业、流动性好、Relay 报价源（标准 AMM）覆盖得到。<strong>这恰好是 relay 路径唯一不拖后腿的集合</strong>，也正好是新用户会买的东西。所以这不是妥协，是把 relay 用在它劣势最小的地方。</p>
    <p><strong>验收口径：老用户主交易路径上 relay 占比 = 0。</strong>要能被监控查出来，不能只写在文档里。</p>
  </div>

  <div class="note">
    <h4>跨链调研清单（让「进一步调研」可执行）</h4>
    <ol>
      <li>relay 分发延迟实测分布（p50 / p95），对比我们的{V["our_path"]}。<strong>机制已由产品侧 08-13 核实：它是{V["relay_path"]}，多一跳。</strong></li>
      <li>哪些链 / 哪些代币 relay 报价源覆盖不到（内盘、新链）。</li>
      <li>失败或卡单时的资金状态——FOMO 用户投诉的「失败交易资金冻结 1–3 工作日」是不是 relay 本身带来的。</li>
      <li>与 Relay 的商务条款（07-14 会议结论：需深度商务合作保障服务质量）。<strong>它是 FOMO 的单点依赖，也应该是我们的谈判杠杆。</strong></li>
    </ol>
  </div>
</section>

<section id="s6">
  <p class="snum">06 — 地基</p>
  <h2>四条在拦着上面的模块</h2>

  <div class="scroll">
  <table>
    <thead><tr><th>地基</th><th>拦着谁</th><th>要点</th></tr></thead>
    <tbody>
      <tr><td><strong>Relay 交易解析</strong><br><span class="tag">GMGN-8687 / 8688 / 8689 / 8665</span></td><td>FOMO Leaderboard · 迁移引导 · 进场点位</td><td>买单走 relay 代发，用户钱包只出现在最后一跳，买入被记在 relayer 名下。修复方向：按「路由合约收币后转给谁」定归属。<strong>Debot / basedbot 已能解析，不是不可解</strong></td></tr>
      <tr><td><strong>标注与可信度规范</strong></td><td>放大层全部</td><td>无法识别投毒 → 所有 relay 来源的数据都要带来源与可信度提示。<strong>产品侧交付物，不是可选项</strong></td></tr>
      <tr><td><strong>推送延迟 {V["push_delay"]}</strong></td><td>发现层 · 所有「快」的叙事</td><td>宣传比修复先落地＝自己给对手递素材</td></tr>
      <tr><td><strong>客服口径</strong></td><td>执行可靠性叙事</td><td>它的「清缓存 / 切节点」<strong>已被用户与我们的「检查 ms / fps / 切代理」并列批评</strong>——我们在同一句吐槽里被点名</td></tr>
    </tbody>
  </table>
  </div>
</section>

<section id="s7">
  <p class="snum">07 — 打</p>
  <h2>它的四个结构性短板</h2>

  <figure>{FIG["bite"]}<figcaption>{FIG["bite_cap"]}</figcaption></figure>

  <div class="scroll">
  <table>
    <thead><tr><th>咬合点</th><th>它为什么跟不了</th></tr></thead>
    <tbody>
      <tr><td><strong>① 榜单重算</strong></td><td>要区分 transferred / bought 并追资金关系，需要整条自研数据管线。它路由 / 跨链 / 密钥 / 出入金全外包——<strong>审计不了自己</strong></td></tr>
      <tr><td><strong>② 进场点位</strong></td><td>Relay 只询价标准 AMM，未毕业代币无法交易 → 它的用户<strong>结构性地只能在毕业后进场</strong>，恰好对上它口碑里「总在当退出流动性」的抱怨</td></tr>
      <tr><td><strong>③ 三件事一道墙</strong></td><td>真自动跟单 / 真限价 / 止盈止损都要平台<strong>代用户签名</strong>，而 Privy 分片密钥必须前端拉 share 本地重组 → 用户不在场签不了。要补就得动钱包架构或放弃自托管叙事<br><span class="tag">口径</span> 对外只说「它的跟单需要用户手动确认」，<strong>不要说「它没有跟单」</strong></td></tr>
      <tr><td><strong>④ 资金进出</strong></td><td>卖不出（gas {V["gas_bump"]} 后最低卖出门槛{V["sell_floor"]}，小仓位死锁）· 入不进（{V["onramp_fail"]}）· 拿不走（{V["withdraw_only"]}）</td></tr>
    </tbody>
  </table>
  </div>

  <div class="note">
    <p><strong>判别标准：</strong>只收结构性短板。费率、本地化、出金体验属于<strong>窗口期</strong>——v8 已证实它改得动（{V["they_fix"]}），<strong>别写进产品叙事</strong>。它 07-01 RH 链上线、07-05 创始人只回一个 👀、07-13 我们就抓到它的完整跨链交易——<strong>从表态到落地 ≤ 8 天</strong>。任何「它还没有 X」型机会，寿命按一个季度估。</p>
  </div>
</section>

<section id="s8">
  <p class="snum">08 — 并稿</p>
  <h2>v8 里属于产品侧的七条</h2>

  <div class="scroll">
  <table>
    <thead><tr><th>v8 内容</th><th>对产品做法的影响</th></tr></thead>
    <tbody>
      <tr><td><strong>三个功能卡在同一道墙上</strong></td><td>从「我们多一个功能」升级为「<strong>这类功能它的架构给不了</strong>」，素材保质期变长 → §07 ③</td></tr>
      <tr><td><strong>债在资金进出，不在速度</strong></td><td>原来只盯「出金复杂」（体验问题），真正结构性的是<strong>小仓位卖不掉</strong>（死锁）→ §07 ④、§05 迁移引导</td></tr>
      <tr><td><strong>速度机制被核实</strong>：{V["relay_path"]}<span class="tag">08-13 非推断</span></td><td>「快」有了机制层解释；直接决定 USDC 边界 → §05</td></tr>
      <tr><td><strong>它在主动补短板</strong>但 {V["they_cant"]}</td><td>给「窗口期 vs 结构性」一个来自对手行为的验证 → §07 判别标准</td></tr>
      <tr><td><strong>用链上数据审计跟单质量</strong></td><td>与 FOMO Leaderboard 同向。v8 的话更准：<strong>我们的社交层卖的是可信度，不是 feed 形态</strong></td></tr>
      <tr><td><strong>托管信任危机</strong>：{V["tos_date"]} {V["tos_risk"]}；{V["scam_dates"]} 假客服已有实际盗资</td><td>攻自托管叙事从技术论证升级为它自己写的条款。<strong>但只给 KOL 号，官方产品文案不碰</strong></td></tr>
      <tr><td><strong>「清缓存 / 切节点」被与我们并列批评</strong></td><td>这是<strong>我们自己的债</strong> → §06 客服口径</td></tr>
    </tbody>
  </table>
  </div>

  <div class="note">
    <p>未提取：增长线（抄 B 不碰 A、UGC 定价、素材主轴）与渠道线（跨 BD 动员存量关系、盯合约到期窗口）归 v8 主线，本文不重复排优先级。</p>
  </div>
</section>

<section id="s9">
  <p class="snum">09 — 要定的 / 待核</p>
  <h2>三件要你定，三件要核</h2>

  <h3>要定</h3>
  <div class="scroll">
  <table>
    <thead><tr><th>#</th><th>事项</th><th>建议</th><th>时机</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>USDC relay 的边界</td><td>限新用户 × 限热门代币；<strong>老用户主路径 relay 占比 = 0</strong> 并可监控</td><td><span class="pill p-hi">内部过稿前</span></td></tr>
      <tr><td>2</td><td>FOMO Leaderboard 的呈现口径</td><td><strong>重算，不镜像</strong>；数据服务，不是打假</td><td><span class="pill p-hi">立项时</span></td></tr>
      <tr><td>3</td><td>Relay 解析的定性</td><td>从「P0 止血」改为「<strong>放大层与承接层的前置条件</strong>」——它拦着三条主线，排期即启动时间</td><td><span class="pill p-hi">本周</span></td></tr>
    </tbody>
  </table>
  </div>

  <h3>待核</h3>
  <div class="scroll">
  <table>
    <thead><tr><th>#</th><th>事项</th><th>为什么会改结论</th></tr></thead>
    <tbody>
      <tr><td>1</td><td><strong>FOMO 的 Apple Pay 是否已被移除</strong></td><td>两个口径直接冲突：外部仍把它列为最强护城河（约 {F.SCALE["first_time_buyers"]} 首次买币用户 / 约 {F.SCALE["first_time_value"]}），我方 08-13 产品债清单说疑似已移除。<strong>若属实，它「零门槛进人」这一环结构性倒退</strong>，而那是整条飞轮的入水口</td></tr>
      <tr><td>2</td><td><strong>我们法币入金的实际口径</strong></td><td>覆盖哪些链 / 哪些国家？是<strong>一键直购代币</strong>还是入金到余额再买？主报告 §9 目前写的是「入金门槛 ❌ FOMO 明显领先」——<strong>要改这一行得先有这几个口径</strong>，否则对外讲「入金优势」会被当场问倒</td></tr>
      <tr><td>3</td><td><strong>持仓来源解析的多链准确率</strong></td><td>FOMO Leaderboard 的「重算」整个建立在能可靠区分 transferred / bought 上。<strong>没量化之前不要对外承诺「可验真」</strong>；同时决定 BSC / Base 的进场点位能不能上</td></tr>
    </tbody>
  </table>
  </div>

  <div class="note warn">
    <p><strong>一条要盯的：FOMO 的排行榜口径会不会变。</strong>它持仓页<strong>已经区分</strong> transferred / bought，说明<strong>数据结构里有这个字段，只是榜没用</strong>——改口径的成本可能远低于我们的假设。它一改，「重算」的对比锋利度会下降；但跟单质量审计与资金关系追踪它仍然做不了（需要自研数据）。<strong>建议加进 v8 的观察哨。</strong></p>
  </div>
</section>

<footer>
  文档矩阵 ·
  <a href="{F.DOCS["brief"][1]}">{F.DOCS["brief"][0]}</a> ·
  <a href="{F.DOCS["loop"][1]}">{F.DOCS["loop"][0]}</a> ·
  <a href="{F.DOCS["full"][1]}">{F.DOCS["full"][0]}</a> · 本文（产品侧）<br>
  数据截至 {F.AS_OF}　·　已并入 Arthur v8（2026-08-13）的产品侧内容，见 §08<br>
  数字统一取自 fomo_facts.py，改数字请改那里并跑 check-facts.py<br>
  分工：v8 主线管增长与渠道，本文管产品；主报告 §10.2 管防守。三处不重复排优先级。
</footer>
'''
