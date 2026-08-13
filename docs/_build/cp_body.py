# -*- coding: utf-8 -*-
"""
《GMGN App 产品侧打法》正文。

模块划分照 Ava 08-13 的口述：定位 → 发现层 → 放大层 → 拉新与承接 → 地基。
写作约束（Ava 08-13 要求）：一模块一表，一行一动作；
每处注释最多 1–2 句，不写大段解释。
"""


def body(F, V, A, FIG):
    return f'''
<header>
  <p class="kicker">竞品情报 · FOMO 系列 · 产品侧 · 内部使用 · {F.AS_OF} 起算</p>
  <h1>GMGN App 产品侧打法</h1>
  <p class="dek">专业交易能力与专业交易员是主导区，不动。App 侧重<strong>发现层</strong>——第一时间发现热门币，放大其中 KOL 与大户的真实持仓，把链上新用户拉进来。</p>
</header>

<section id="s1">
  <p class="snum">01 — 全局</p>
  <h2>五个模块</h2>
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
    <p>这条回答了 v8 的待裁决 ①：那三个选项都在争「服务小白还是专业」，<strong>按环节切就不用二选一</strong>，也不必让出主导区。</p>
  </div>
</section>

<section id="s3">
  <p class="snum">03 — 发现层</p>
  <h2>第一时间发现，推到用户面前</h2>

  <div class="scroll">
  <table>
    <thead><tr><th>动作</th><th>状态</th><th>要点</th></tr></thead>
    <tbody>
      <tr><td><strong>热门精选代币 push</strong></td><td><span class="pill p-us">已上线</span></td><td>我们有质量闸，实测覆盖 {F.PUSH["our_coverage"]}、{F.PUSH["our_earlier"]} 币首触更早；FOMO {F.PUSH["their_coverage"]} 且无质量闸</td></tr>
      <tr><td><strong>Callout 全方位铺开</strong></td><td><span class="pill p-mid">推进中</span></td><td>对标 FOMO thesis。K 线页 / 单人单币页 / 持仓页，监控默认推全局</td></tr>
      <tr><td><strong>热门列表混链整合</strong></td><td><span class="pill p-mid">推进中</span></td><td>弱化链概念，与热搜差异互补，解决金狗首页找不到</td></tr>
      <tr><td><strong>新用户第一屏＝热门榜单</strong></td><td><span class="pill p-mid">本季度</span></td><td>不是交易面板</td></tr>
      <tr><td><strong>我们自己的推送延迟</strong>：{V["push_delay"]}<br><span class="tag">v8 最高优先级，但未给测量来源</span></td><td><span class="pill p-hi">待核</span></td><td>对比 Dexscreener 近实时（不是对比 FOMO）。若属实，「第一时间」这条主线站不住；<strong>先测出真实数字再决定要不要立项</strong></td></tr>
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
      <tr><td><strong>热门币里的 KOL 持仓</strong></td><td><span class="pill p-mid">本季度</span></td><td>谁在拿、拿多少、什么时候进的</td></tr>
      <tr><td><strong>大户持仓与动向</strong></td><td><span class="pill p-mid">本季度</span></td><td>接到热门列表与代币页，作为「为什么它热」的解释</td></tr>
      <tr><td><strong>FOMO Leaderboard</strong></td><td><span class="pill p-us">新增</span></td><td>见下</td></tr>
      <tr><td>relay 数据标注与可信度规范</td><td><span class="pill p-hi">前置</span></td><td>上面三条的合规底座</td></tr>
    </tbody>
  </table>
  </div>

  <div class="note gain">
    <h3>FOMO Leaderboard：重算，不镜像</h3>
    <p>它一条解决三件事：满足用户对 FOMO 钱包的追踪需求、堵住「为看榜去装 FOMO」的流失、拆解它的造富效应。</p>
    <p>机制事实是<strong>{A["leaderboard"]}</strong>，所以直接搬数字等于替它背书——每行按我们的口径拆成<strong>站内买入 / 外部转入 / 关联钱包内转</strong>，PnL 默认只算买入部分。</p>
  </div>

  <div class="note warn">
    <p>两条红线：<strong>呈现为数据服务，不是打假</strong>（口径是「它的榜不区分来源」，不是「它造假」）；<strong>必须带来源标注与可信度提示</strong>，因为我们目前无法识别投毒，relay 交易只敢解析成转入/转出。</p>
  </div>

  <div class="note">
    <p>一手样本：claymore（@claymorepx）确认是 {A["claymore_rank"]}、PnL {A["claymore_pnl"]}，而{A["claymore_fact"]}。<span class="tag">v8 要求保留</span> 他自述动机是移动端体验好、社交曝光强，引用时这句不能省。</p>
  </div>
</section>

<section id="s5">
  <p class="snum">05 — 拉新与承接</p>
  <h2>客源是链上新用户，不是圈外小白</h2>

  <div class="scroll">
  <table>
    <thead><tr><th>动作</th><th>状态</th><th>要点</th></tr></thead>
    <tbody>
      <tr><td><strong>法币入金</strong></td><td><span class="pill p-us">已支持</span></td><td>新链上的天然优势：新链没有原生资产存量，用户无从入金。口径待核，见 §09</td></tr>
      <tr><td><strong>热门代币支持 USDC 购买</strong></td><td><span class="pill p-mid">本季度</span></td><td><strong>限新用户</strong>。见下</td></tr>
      <tr><td>跨链</td><td><span class="pill p-hi">待调研</span></td><td>清单见下，不进老用户主路径</td></tr>
      <tr><td><strong>迁移引导路径</strong></td><td><span class="pill p-us">新增</span></td><td>一键导入私钥 / 接管持仓 / 落地页。出口是它自己开的——官方建议用户「导出私钥到 Phantom 操作」</td></tr>
    </tbody>
  </table>
  </div>

  <div class="note key">
    <p>限定在<strong>已经热门的代币</strong>是对的：热门币已毕业、流动性好、Relay 报价源覆盖得到，<strong>恰好是 relay 唯一不拖后腿的集合</strong>，也正好是新用户会买的东西。</p>
    <p>验收口径：<strong>老用户主交易路径上 relay 占比 = 0</strong>，且要能被监控查出来。</p>
  </div>

  <div class="note">
    <h4>跨链调研清单</h4>
    <ol>
      <li>relay 分发延迟实测 p50 / p95，对比我们的{V["our_path"]}。<span class="tag">08-13 已核实</span> 它是{V["relay_path"]}，多一跳</li>
      <li>哪些链 / 代币 relay 报价源覆盖不到（内盘、新链）</li>
      <li>失败或卡单时的资金状态——FOMO 用户投诉的「资金冻结 1–3 工作日」是不是 relay 带来的</li>
      <li>与 Relay 的商务条款。它是 FOMO 的单点依赖，也该是我们的谈判杠杆</li>
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
      <tr><td><strong>Relay 交易解析</strong><br><span class="tag">GMGN-8687 / 8688 / 8689 / 8665</span></td><td>FOMO Leaderboard · 迁移引导 · 进场点位</td><td>买单走 relay 代发，用户钱包只出现在最后一跳，买入被记在 relayer 名下。改按「路由合约收币后转给谁」定归属。Debot / basedbot 已能解析</td></tr>
      <tr><td><strong>标注与可信度规范</strong></td><td>放大层全部</td><td>无法识别投毒，所有 relay 来源数据都要带提示。产品侧交付物</td></tr>
      <tr><td><strong>我们自己的推送延迟</strong><br><span class="pill p-hi">待核</span> {V["push_delay"]}</td><td>发现层 · 所有「快」的叙事</td><td>数字来自 v8，未给测量来源。<strong>先测，不要直接当事实排期</strong>——但若属实，宣传比修复先落地就是自己给对手递素材</td></tr>
      <tr><td><strong>客服口径</strong></td><td>执行可靠性叙事</td><td>它的「清缓存 / 切节点」已被用户与我们的「检查 ms / fps / 切代理」并列批评</td></tr>
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
      <tr><td><strong>① 榜单重算</strong></td><td>区分 transferred / bought 并追资金关系需要自研数据管线，而它路由 / 跨链 / 密钥 / 出入金全外包——<strong>审计不了自己</strong></td></tr>
      <tr><td><strong>② 进场点位</strong></td><td>Relay 只询价标准 AMM，未毕业代币无法交易，它的用户<strong>结构性地只能毕业后进场</strong>——恰好对上它口碑里「总在当退出流动性」</td></tr>
      <tr><td><strong>③ 三件事一道墙</strong></td><td>真自动跟单 / 真限价 / 止盈止损都要平台代用户签名，而 Privy 分片密钥必须前端本地重组，用户不在场签不了<br><span class="tag">口径</span> 只说「它的跟单需要手动确认」，<strong>不说「它没有跟单」</strong></td></tr>
      <tr><td><strong>④ 资金进出</strong></td><td>卖不出（gas {V["gas_bump"]} 后门槛{V["sell_floor"]}，小仓位死锁）· 入不进 · 拿不走（{V["withdraw_only"]}）</td></tr>
    </tbody>
  </table>
  </div>

  <div class="note">
    <p>只收结构性短板。费率、本地化、出金体验属<strong>窗口期</strong>——它 08 月已在降费率，<strong>别写进产品叙事</strong>；参考它从创始人一个 👀 到上线 RH 链只用了 8 天。</p>
  </div>
</section>

<section id="s8">
  <p class="snum">08 — 并稿</p>
  <h2>v8 里属于产品侧的七条</h2>

  <div class="scroll">
  <table>
    <thead><tr><th>v8 内容</th><th>对产品做法的影响</th></tr></thead>
    <tbody>
      <tr><td><strong>三个功能卡在同一道墙上</strong></td><td>从「多一个功能」升级为「它的架构给不了」，素材保质期变长 → §07 ③</td></tr>
      <tr><td><strong>债在资金进出，不在速度</strong></td><td>原来只盯出金复杂（体验），真正结构性的是小仓位卖不掉（死锁）→ §05、§07 ④</td></tr>
      <tr><td><strong>速度机制被核实</strong><span class="tag">08-13</span></td><td>{V["relay_path"]}，「快」有了机制解释，并直接决定 USDC 边界 → §05</td></tr>
      <tr><td><strong>它在主动补短板</strong>，但 {V["they_cant"]}</td><td>给「窗口期 vs 结构性」一个来自对手行为的验证 → §07</td></tr>
      <tr><td><strong>用链上数据审计跟单质量</strong></td><td>与 FOMO Leaderboard 同向：<strong>我们的社交层卖可信度，不是 feed 形态</strong></td></tr>
      <tr><td><strong>托管信任危机</strong>：{V["tos_date"]} {V["tos_risk"]}</td><td>攻自托管从技术论证升级为它自己写的条款，<strong>但只给 KOL 号，官方文案不碰</strong></td></tr>
      <tr><td><strong>「清缓存 / 切节点」被与我们并列批评</strong></td><td>这是我们自己的债 → §06</td></tr>
    </tbody>
  </table>
  </div>

  <div class="note">
    <p>未提取：增长线与渠道线归 v8 主线，本文不重复排优先级。</p>
  </div>
</section>

<section id="s9">
  <p class="snum">09 — 要定的 / 待核</p>
  <h2>三件要你定，四件要核</h2>

  <h3>要定</h3>
  <div class="scroll">
  <table>
    <thead><tr><th>事项</th><th>建议</th><th>时机</th></tr></thead>
    <tbody>
      <tr><td>USDC relay 的边界</td><td>限新用户 × 限热门代币；老用户主路径 relay 占比 = 0 且可监控</td><td><span class="pill p-hi">内部过稿前</span></td></tr>
      <tr><td>FOMO Leaderboard 的呈现口径</td><td>重算，不镜像；数据服务，不是打假</td><td><span class="pill p-hi">立项时</span></td></tr>
      <tr><td>Relay 解析的定性</td><td>从「P0 止血」改为「放大层与承接层的前置条件」——排期即启动时间</td><td><span class="pill p-hi">本周</span></td></tr>
    </tbody>
  </table>
  </div>

  <h3>待核</h3>
  <div class="scroll">
  <table>
    <thead><tr><th>事项</th><th>为什么会改结论</th></tr></thead>
    <tbody>
      <tr><td><strong>FOMO 的 Apple Pay 是否已移除</strong></td><td>外部仍列为它最强护城河（约 {F.SCALE["first_time_buyers"]} 首次买币 / 约 {F.SCALE["first_time_value"]}），我方 08-13 产品债清单说疑似已移除。若属实，它「零门槛进人」这一环结构性倒退</td></tr>
      <tr><td><strong>我们法币入金的实际口径</strong></td><td>覆盖哪些链 / 国家？一键直购还是入金到余额再买？主报告 §9 现在写的是「入金门槛 ❌ FOMO 明显领先」，改这行得先有口径</td></tr>
      <tr><td><strong>持仓来源解析的多链准确率</strong></td><td>「重算」建立在能可靠区分 transferred / bought 上；没量化前不要对外承诺「可验真」</td></tr>
      <tr><td><strong>我们自己的推送延迟到底是多少</strong></td><td>v8 把「修 6–20min 延迟」列为产品线最高优先级，<strong>但未给测量来源</strong>，App PM 也不认这个数。它决定「第一时间」这条主线能不能讲——<strong>先测，再决定要不要立项</strong></td></tr>
    </tbody>
  </table>
  </div>

  <div class="note warn">
    <p>要盯：<strong>它的榜单口径会不会变</strong>。持仓页已经区分 transferred / bought，说明字段在数据结构里、只是榜没用，改的成本可能远低于我们的假设。建议加进 v8 观察哨。</p>
  </div>
</section>

<footer>
  文档矩阵 ·
  <a href="{F.DOCS["brief"][1]}">{F.DOCS["brief"][0]}</a> ·
  <a href="{F.DOCS["loop"][1]}">{F.DOCS["loop"][0]}</a> ·
  <a href="{F.DOCS["full"][1]}">{F.DOCS["full"][0]}</a> · 本文（产品侧）<br>
  数据截至 {F.AS_OF}　·　已并入 Arthur v8（2026-08-13）产品侧内容，见 §08<br>
  数字取自 fomo_facts.py　·　v8 主线管增长与渠道，本文管产品，主报告 §10.2 管防守
</footer>
'''
