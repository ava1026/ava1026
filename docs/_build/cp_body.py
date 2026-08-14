# -*- coding: utf-8 -*-
"""
《GMGN App 产品侧打法》正文。

模块划分照 Ava 08-13 的口述：定位 → 发现层 → 放大层 → 拉新与承接 → 地基。
写作约束（Ava 08-13 要求）：一模块一表，一行一动作；
不带注释块与图注（Ava 08-13：注释文案全部去掉）。
"""


def body(F, V, A, FIG):
    return f'''
<header>
  <h1>产品为增长玩法服务</h1>
  <p class="dek">在现有 App 基础上改，包袱重，兼容两个群体，拧巴。<br><strong>启动 fomo 栏目，为增长打法服务，丢包袱。</strong></p>
</header>

<section id="s0">
  <p class="snum">00 — fomo 专栏</p>
  <h2>把增长玩法装进一个新栏目，不动主 App</h2>

  <div class="scroll">
  <table>
    <thead><tr><th>问题</th><th>答案</th></tr></thead>
    <tbody>
      <tr><td><strong>为什么单开</strong></td><td>在现有 App 基础上改，包袱重，兼容两个群体，拧巴；<br><strong>fomo 专栏为增长打法服务，丢包袱</strong></td></tr>
      <tr><td><strong>装什么</strong></td><td>直接抄 fomo，降低门槛，简化内容，突出社交</td></tr>
      <tr><td><strong>不装什么</strong></td><td>专业执行与深度分析留在主 App / Web，主导区不动</td></tr>
      <tr><td><strong>给谁用</strong></td><td>圈外小白</td></tr>
      <tr><td><strong>前置地基</strong></td><td>USDC自动跨链交易</td></tr>
    </tbody>
  </table>
  </div>
</section>

<section id="s1">
  <p class="snum">01 — 全局</p>
  <h2>五个模块</h2>
  <figure>{FIG["loop"]}</figure>
  <figure>{FIG["map"]}</figure>
</section>

<section id="s2">
  <p class="snum">02 — 定位</p>
  <h2>按环节切不同人群</h2>

  <div class="scroll">
  <table>
    <thead><tr><th>环节</th><th>人群</th><th>归属</th><th>抓手</th></tr></thead>
    <tbody>
      <tr><td><strong>发现</strong></td><td>圈外小白 · 链上新用户 · 打二段用户</td><td>App 主轴</td><td>热门混链 · push · callout。<strong>同时是拉新入口</strong></td></tr>
      <tr><td><strong>执行</strong></td><td>专业交易员 · 高意图执行用户</td><td>App 与 Web 都保专业深度</td><td>参数可控 · 真限价 · 止盈止损</td></tr>
      <tr><td><strong>深度分析</strong></td><td>专业交易员 · Web3 老手</td><td>Web 为主</td><td>数据看板 · 钱包画像 · 资金关系</td></tr>
    </tbody>
  </table>
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
      <tr><td><strong>热门列表混链整合</strong></td><td><span class="pill p-mid">推进中</span></td><td>1. 弱化链概念<br>2. 更稳健的代币，给<strong>打二段用户</strong>与<strong>链上新用户</strong>，风险低</td></tr>
      <tr><td><strong>新用户第一屏＝热门列表</strong></td><td><span class="pill p-mid">本季度</span></td><td>第一笔交易</td></tr>
    </tbody>
  </table>
  </div>
</section>

<section id="s4">
  <p class="snum">04 — 放大层</p>
  <h2>放大真实的赚钱效应</h2>

  <figure>{FIG["lanes"]}</figure>

  <div class="scroll">
  <table>
    <thead><tr><th>动作</th><th>状态</th><th>要点</th></tr></thead>
    <tbody>
      <tr><td><strong>热门币里的 KOL 持仓</strong></td><td><span class="pill p-mid">本季度</span></td><td>谁在拿、拿多少、什么时候进的</td></tr>
      <tr><td><strong>大户持仓与动向</strong></td><td><span class="pill p-mid">本季度</span></td><td>接到热门列表与代币页，作为「为什么它热」的解释</td></tr>
      <tr><td><strong>FOMO Leaderboard</strong></td><td><span class="pill p-us">新增</span></td><td><strong>重算，不镜像</strong>：按我们口径拆 站内买入 / 外部转入 / 关联钱包内转，PnL 默认只算买入；带来源标注与可信度提示</td></tr>
      <tr><td>relay 数据标注与可信度规范</td><td><span class="pill p-hi">前置</span></td><td>上面三条的合规底座</td></tr>
    </tbody>
  </table>
  </div>



</section>

<section id="s5">
  <p class="snum">05 — 拉新与承接</p>
  <h2>降低门槛，为圈外用户做准备</h2>

  <div class="scroll">
  <table>
    <thead><tr><th>动作</th><th>状态</th><th>要点</th></tr></thead>
    <tbody>
      <tr><td><strong>法币入金</strong></td><td><span class="pill p-us">已支持</span></td><td>已经支持 50+ 个国家法币入金</td></tr>
      <tr><td><strong>Apple Pay 直接购买 meme 代币</strong></td><td><span class="pill p-us">待调研</span></td><td>提升圈外用户第一笔交易成功率</td></tr>
      <tr><td><strong>USDC 交易</strong></td><td><span class="pill p-mid">推进中</span></td><td><strong>新用户充USDC - 默认本链开USDC交易模式</strong></td></tr>
      <tr><td>USDC自动跨链交易</td><td><span class="pill p-hi">新增调研</span></td><td>非华语新用户进此流程，不进老用户主路径</td></tr>
      <tr><td><strong>迁移引导路径</strong></td><td><span class="pill p-us">新增</span></td><td>一键导入私钥 / 接管持仓 / 落地页。出口是它自己开的——官方建议用户「导出私钥到 Phantom 操作」</td></tr>
    </tbody>
  </table>
  </div>


</section>

<section id="s6">
  <p class="snum">06 — 地基</p>
  <h2>两条在拦着上面的模块</h2>

  <div class="scroll">
  <table>
    <thead><tr><th>地基</th><th>拦着谁</th><th>要点</th></tr></thead>
    <tbody>
      <tr><td><strong>Relay 交易解析</strong><br><span class="tag">GMGN-8687 / 8688 / 8689 / 8665</span></td><td>FOMO Leaderboard · 迁移引导 · 进场点位</td><td>买单走 relay 代发，用户钱包只出现在最后一跳，买入被记在 relayer 名下。改按「路由合约收币后转给谁」定归属。Debot / basedbot 已能解析</td></tr>
      <tr><td><strong>标注与可信度规范</strong></td><td>放大层全部</td><td>无法识别投毒，所有 relay 来源数据都要带提示。产品侧交付物</td></tr>
    </tbody>
  </table>
  </div>
</section>

<section id="s7">
  <p class="snum">07 — 打</p>
  <h2>它的四个结构性短板</h2>

  <figure>{FIG["bite"]}</figure>

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
      <tr><td><strong>我们法币入金的链覆盖</strong></td><td>已确认：50+ 国家（Ava 08-13）；<strong>Apple Pay 直购不支持，待调研</strong>。剩一问：<strong>覆盖哪些链</strong>——它决定「新链天然优势」能不能对外讲，也决定主报告 §9「入金门槛 ❌ FOMO 明显领先」那行怎么改</td></tr>
      <tr><td><strong>持仓来源解析的多链准确率</strong></td><td>「重算」建立在能可靠区分 transferred / bought 上；没量化前不要对外承诺「可验真」</td></tr>
      <tr><td><strong>我们自己的推送延迟到底是多少</strong></td><td>v8 把「修 6–20min 延迟」列为产品线最高优先级，<strong>但未给测量来源</strong>，App PM 也不认这个数。它决定「第一时间」这条主线能不能讲——<strong>先测，再决定要不要立项</strong></td></tr>
    </tbody>
  </table>
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
