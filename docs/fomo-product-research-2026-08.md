# FOMO 全面产品调研（2026-08-11）

> 作者：Ava（GMGN）· 数据截止 2026-08-11
> 性质：竞品情报，内部使用，非对外材料
> 信息标注约定：**〔一手〕** = GMGN 内部实测/抓包/影子测试；**〔公开〕** = 外部公开报道或官方口径；**〔推断〕** = 基于以上两类数据的推理，未经验证

---

## 目录

1. [一页结论](#一一页结论)
2. [公司与资本](#二公司与资本)
3. [业务数据与增长曲线](#三业务数据与增长曲线)
4. [产品全貌](#四产品全貌)
5. [技术架构拆解（内部一手）](#五技术架构拆解内部一手)
6. [商业模式与费率](#六商业模式与费率)
7. [增长与市场策略](#七增长与市场策略)
8. [用户口碑与真实问题](#八用户口碑与真实问题)
9. [我们 vs FOMO：能力对照](#九我们-vs-fomo能力对照)
10. [威胁评估与行动建议](#十威胁评估与行动建议)
11. [情报缺口与待验证清单](#十一情报缺口与待验证清单)
12. [附录：地址/接口索引与资料来源](#十二附录)

---

## 一、一页结论

**FOMO 是什么**：一款自托管（non-custodial）的**移动端优先 + 社交优先**的多链交易 App。核心命题不是"更快的终端"，而是**"把链上交易变成一件社交的、零门槛的事"**——用 USDC 一个余额买全网、Apple Pay 直接入金、交易实时进 feed 被人抄。

**为什么必须重视**：

1. **增长曲线陡且没有减速** —— 2026-08-08 单周协议收入 $2.64M 创历史新高，比 7/27 的 $1.57M 又高 68%；已连续 6 周交易量创新高；日均新增用户 3k+〔公开〕。
2. **它已经在 Solana 上超过 Axiom 的日交易量** —— 这是 memecoin 终端战场的权力转移信号；单周收入超过 Phantom、Jupiter，24h 收入曾超 Hyperliquid〔公开〕。
3. **它抢占了我们不占的用户层** —— 68,000+ 首次买币用户从 Apple Pay 进来（$25M）；KOL 反馈"很多巨鲸的高市值币交易跑到 FOMO 上去了"〔一手，2025-11 Tyrelle 反馈〕。
4. **它在正面抢我们的心智** —— 热门代币推送（callout）先于我们上线，07-23 对 GME 一天推 11 次，用户心智正在被建立；同时 FOMO 的交易在我们的 Wallet Tracker 里**追踪不到**，用户已经在投诉这件事〔一手〕。
5. **迭代速度极快** —— Robinhood Chain 2026-07-01 主网上线，创始人 07-05 对"支持 RH 链"的请求只回了一个 👀，**07-13 我们已抓到 FOMO 在 RH 链上的完整跨链买入交易**。即从表态到落地 ≤ 8 天〔一手 + 公开交叉〕。

**它的结构性弱点（我们的机会）**：

| 弱点 | 本质 | 可打击性 |
|---|---|---|
| **不支持内盘** | 跨链只询价 Uniswap V3 标准 AMM，未毕业代币无法交易 | 高——首发/内盘是 alpha 最集中的地方 |
| **交易参数不可控** | 无滑点自定义、无加速/priority fee 设置 | 高——专业用户刚需 |
| **跨链 ~3s 延迟** | Intent-based 异步结算，非原子 | 中——散户无感，大户敏感 |
| **分析深度浅** | 无自研数据，靠外部路由 + 简单看板 | 高——GMGN 的护城河所在 |
| **BNB 链执行差** | 高波动时不填充/延迟填充，官方承认在修但方案未定 | 中——窗口期有限 |
| **"限价单"非链上真单** | 创始人公开承认非托管跨 5 链做真限价单"极难"，只能先做 SOL | 中——可作为对比素材 |
| **技术全外包** | 路由、跨链、密钥、入金、出金全靠第三方 | 长期——供应商风险，但短期是它的速度优势 |
| **本地化几乎为零** | 只有英文，无阿拉伯语等 RTL 语言 | 高——新兴市场空白 |

**一句话判断**：FOMO 走的是**"消费级金融 App"**路线，不是"专业终端"路线。它用**极简 + 社交 + 零 gas 感知**换取了增量小白用户和高频小额交易，收入由**笔数**而非**单笔金额**驱动〔推断：07-13 实测日均每笔平台费仅 ≈ $0.76〕。它在专业性上短期不会赢我们，但它可能把整个市场的**新增用户入口**吃掉，然后再往上做专业功能（perps 已上线、限价单在做）。这是**入口战**，不是功能战。

---

## 二、公司与资本

### 2.1 基本信息〔公开〕

| 项 | 内容 |
|---|---|
| 产品名 | fomo（品牌全小写）· 域名 `fomo.family` |
| 主体 | FOMO Labs，纽约 |
| 成立 | 2024 年（公司），产品 2025-05-06 公开上线 |
| 创始人 | Paul Erlanger、Se Yong Park（X: @seyong）、Prashan Dharmasena |
| 团队背景 | 三人均出自 dYdX（Erlanger 2021-07~2024-10 任 BD 负责人；Park 与其先后共事于 Deutsche Bank、dYdX 约 5 年）；团队还有 Uniswap、OpenSea、Square、Google 背景 |
| 定位口径 | "social-first crypto trading app"、"#1 cross-chain trading app in crypto" |

### 2.2 融资历史〔公开〕

| 轮次 | 时间 | 金额 | 估值 | 领投 / 参投 |
|---|---|---|---|---|
| 早期 | 2024~2025 | ~$2M | — | （合计口径推得） |
| Series A | 2025-11 | $17M | — | Benchmark 领投（Benchmark 罕见的加密投资） |
| Series B | 2026-06-22 | **$75M** | **$550M** | **Index Ventures 领投**，Union Square Ventures、Benchmark 跟投 |
| **累计** | | **≈ $94M** | | |

> Series B 融资公告是 GMGN 内部最早的正式警觉点之一：2026-06-22 内部 Slack 同步了官方口径的四个数字——625,000+ 用户 / $4B+ 累计交易量 / 110M+ 社交互动 / 68,000+ 首次买币用户（$25M）〔一手〕。

### 2.3 资本含义

- **$550M 估值 + Index/USV/Benchmark 组合** = 这是被当作**消费级 fintech**而非 crypto 工具在定价。这决定了它的战略必然是"用户规模优先"，会持续烧钱补贴费率、KOL、入金。
- **无代币**：截至 2026-06 官方从未提及发币计划〔公开〕。第三方评级机构认为积分/空投"仍很可能"，若发币预期用途为手续费折扣、销毁、治理〔公开，属推测〕。**对我们的含义**：它目前的增长是**纯产品 + 纯现金补贴**驱动的，没有代币预期的虚假繁荣——这让增长质量比 airdrop farming 型竞品更硬。

---

## 三、业务数据与增长曲线

### 3.1 用户与交易量〔公开〕

| 时点 | 用户 | 累计交易量 | 备注 |
|---|---|---|---|
| 2025-11（A 轮） | 120,000 用户 / 35,000 交易者 | — | trader/user = **29%**；净新增币圈用户 ~15,000；onramp 入金 $5M |
| A 轮后某时点 | 250,000 | $1.5B | |
| 2026 年中 | 470,000+ | $2.5B | Crossmint 口径 |
| 2026-06（B 轮） | **625,000+** | **$4B+** | 官方/USV 口径；110M+ 社交互动；68,000+ 首次买币（$25M，经 Apple Pay） |
| 2026-08 | 625,000+ | — | 日新增 **3,000+** 用户 |

⚠️ **数据可信度**：全部为公司/投资人自述，未经审计。"user"很可能指**注册数**而非入金或活跃账户。唯一能干净算出的漏斗比率是 2025-11 的 **29% trader/user**，且是单点观测而非留存队列〔公开，insights4vc 的批评意见〕。**建议我们对外引用时统一注明"官方口径"**。

### 3.2 收入曲线（关键）〔公开 + 一手交叉验证〕

| 口径 | 数值 | 来源 |
|---|---|---|
| Q1 2026 日均 | ~$103k/日 | DefiLlama 口径 |
| Q2 2026 日均 | ~$79k/日 | 同上 |
| **2026-07-13 实测** | **$96,789/24h**（Solana 收费钱包净流入），约 **128,000 笔/日** | **〔一手〕HAR + 链上实测** |
| Q3 前 27 天 | $6.03M，日均 **~$223k/日** | DefiLlama 口径 |
| 周收入 ATH ①| **$1.39M**（约 7 月中） | Solana 协议收入第 3 名 |
| 周收入 ATH ②| **$1.57M**（截至 7/27） | |
| 周收入 ATH ③| **$2.64M**（截至 8/08） | 比 ATH② 高 **68%**，超过 Phantom（+86%）与 Jupiter（≈3×） |
| 收入构成（8/08 周） | Solana **$2.6M** + Hyperliquid perps builder fee **$38.8K** | **DefiLlama 口径下** 98.5% 来自 Solana 现货 —— ⚠️ 见下方"口径陷阱" |
| 近 30 天（截至 8/08） | 总手续费 **$9.48M**，其中协议收入 **$8.79M** | 差额 $0.69M（7.3%）应为推荐人分润 |
| 年化口径分歧 | DefiLlama 年化 **$22.68M** ／ 第三方 ARR 口径 **$72M run-rate（YoY 10×）** | 两者差异大，见下 |

> ### ⚠️ 口径陷阱："98.5% 来自 Solana"很可能不包含 Robinhood 链
>
> **这个数字不能按字面理解为"FOMO 的收入 98.5% 产生在 Solana"。** 它只能读作：**DefiLlama 所能测到的那部分收入里，98.5% 在 Solana。**
>
> **理由（一手证据支撑的结构性原因）**：
>
> 1. **DefiLlama 的 fomo 适配器只有两条线** —— 公开拆分里只出现 Solana 与 Hyperliquid，**没有 Base / BNB / Monad / Robinhood 的任何一行**。〔公开〕
> 2. **同链 Solana swap 的手续费是链上可见的独立转账** —— 顶层 `transferChecked` 打进收费 ATA。这种形态适配器一抓一个准。〔一手〕
> 3. **跨链 swap 的平台费在链上根本没有独立转账** —— 原文实测结论："链上 token flow 看不到 Fomo 平台费的独立 transfer（与同链 swap 不同），因为平台费在 Relay 报价阶段已经内含扣除"。只有 HAR 里的 `feeTierBps: 50` / `usdFees.app` 能证明它存在。**链上抓不到 ⇒ 适配器抓不到。**〔一手〕
> 4. **而 FOMO 的架构决定了非 Solana 交易几乎全是跨链交易** —— 用户资金以 USDC 沉淀在 Solana，其他链只是执行层。在 Robinhood / Base / BNB 上买币 = 从 Solana 发起的跨链买入；卖出 = 跨链卖回 Solana。**所以非 Solana 链上的那部分收入，按其收费形态本来就是"隐形"的。**〔一手 + 推断〕
>
> **结论**：98.5% 是**测量口径的产物，不是业务事实**。FOMO 真实的链间收入结构目前**未知**，Robinhood 链的贡献既没有被证实、也没有被证伪。报告中所有"perps 只占 1.5%""收入几乎全在 Solana"的表述，都应加上"DefiLlama 口径"这个限定。
>
> **同一批数字内部也不自洽**：不同报道对同一周 Hyperliquid perps 的贡献给出 $38.8K 与 $47,484 两个值（后者被称作"约占 3.4%"，但 47,484 / 2.64M = 1.8%）。**这批第三方数字精度有限，不宜作为决策的唯一依据。**
>
> **如何做实（建议交给数据侧执行，我们有全部所需地址）**：
>
> | 方法 | 做法 | 产出 |
> |---|---|---|
> | **A. 跨链买入量反推（推荐，最易落地）** | 统计 Solana 跨链桥程序 `99vQwtBwYtrqqD9YSXbdum3KBdxPAVxYTaQ3cfnJSrN2` 的 USDC 存入总量，× 0.5% | 跨链买入平台费的**下限**，可直接与 Solana 同链费用对比得出真实比例 |
> | **B. 跨链卖出量反推** | 统计 Solana Relayer `F7p3dFrjRTbtRp8FRF6qHLomXbKRBzpvBLjtQcfcgmNe` 转给用户的 USDC，× 0.5%。**注意剔除纯 USDC 归集**（该场景不收平台费），可按源链是否发生 swap 区分 | 跨链卖出平台费 |
> | **C. 按链拆分** | 对 Robinhood（4663）上 `RelayRouterV3 0xb92fe925…fff4f` 的成交按链分别统计 | Robinhood 链单独贡献 |
> | **D. 直接问 Relay** | 我们本来就要启动 Relay BD —— app fee 的结算口径和账单是可以在商务谈判中直接问到的 | 权威口径 |
>
> 方法 A 一个人一天就能出结果，且**不依赖任何第三方数据源**。在拿到之前，本报告涉及链间结构的判断请按"未验证"对待。

**交叉验证与解读**：

- 我们 07-13 实测的 $96.8k/日 ≈ 周 $67.8万，而外部报道 7/27 周 $157万、8/08 周 $264万 —— **说明 7 月中到 8 月初，FOMO 收入翻了约 3.9 倍**。这不是线性增长，是**爆发段**。〔一手 × 公开 交叉，可信度高〕
- 年化口径分歧的解释〔推断〕：DefiLlama 的 $22.68M 更像是**滚动/加权年化**（含低基数月份），$72M run-rate 是**按近期峰值外推**。按 8/08 周 $2.64M 外推，年化约 **$137M**。真实"当期运行率"大概在 **$80M~$137M** 区间，取决于是否假设 8 月峰值可持续。
- **推荐人分润的实际渗透率**〔推断，新〕：近 30 天总手续费 $9.48M、协议收入 $8.79M，差额占比 **7.3%**。若差额全部来自卖出侧 75/25 分润，则 `0.25 × r = 7.3%` → **r ≈ 29%，即约三成手续费来自绑定了推荐人的用户**。这与 A 轮时 29% 的 trader/user 比例数值巧合，但含义不同：它说明 **FOMO 的联盟体系确实在贡献可观流量，但主体（七成）仍是自然增长**。（前提：DefiLlama 的 fees / revenue 采用"用户支付 / 协议留存"的标准定义。）
- **单笔经济学**〔推断，重要〕：07-13 日收 $96,789 / 128,000 笔 ≈ **$0.76/笔**。而 FOMO ≤200U 档是**固定 0.95 USDC/笔**——说明绝大多数交易落在最低档，**客单价极小**。结论：**FOMO 的收入是"笔数生意"，用户画像是小额高频散户**，不是大额巨鲸。（与 2025-11 KOL 说"巨鲸跑去 FOMO 交易高市值币"并不矛盾——巨鲸带来的是**心智与内容**，散户带来的是**笔数与收入**。）

### 3.3 市场份额格局〔公开〕

- **FOMO 已超过 Axiom 的 Solana 日交易量**（2026 年 6 月 6 天内交易量增长 57%，随后完成超越）。Axiom 曾在 2025-04 峰值占 Solana meme 交易量 72%、2026-07 终端份额峰值 74%。
- **Photon 份额从 2026-01 的 30.7% 跌到 7 月不足 10%**。
- **Pump.fun 正面应战**：2026-08-07 上线社交交易功能（直接对标 FOMO 的 copy-trading/社群）；**2026-08-09 开出挖角条件——给 FOMO 用户 $20,000 签约金 + $30,000/月**，条件包括公开转移资金、永久删除 FOMO 账号。〔公开〕
  → **这是市场对 FOMO 威胁级别的第三方定价**。Pump.fun 愿意付这个价挖人，说明 FOMO 的用户粘性与钱包质量被同行认为是真实的。

---

## 四、产品全貌

### 4.1 链与资产覆盖

| 类别 | 覆盖 | 来源 |
|---|---|---|
| 现货链 | **Solana、Base、BNB Chain、Monad**（公开口径 4 条）；创始人 2026-07-05 原话 "5 diff chains" | 公开 + 一手 |
| **Robinhood Chain（4663）** | **已支持**——我们 07-13 抓到完整跨链买入/卖出/归集交易 | **〔一手，外部尚无报道〕** |
| 统一余额 | 单一 USD/USDC 余额跨全部链使用，用户**感知不到跨链**，交易在各链原生结算层执行 | 公开 + 一手 |
| Perps | 2026-06-11 对**非美用户**上线，由 **Hyperliquid + Trade[XYZ]** 提供；可交易 pre-IPO、股票、加密、指数、商品 perps | 公开 |
| 内盘 / 未毕业代币 | **不支持**（跨链只询价 Uniswap V3） | 〔一手〕 |
| 语言 | **仅英文**，无阿拉伯语等 RTL | 〔一手，2026-08-11 实查〕 |

> **战略含义**：FOMO 把"链"这个概念对用户彻底隐藏了。用户只有一个 USDC 余额，买什么链的币都不需要知道自己在跨链。这是它对小白最强的一击，也是我们 Q3 立项"FOMO 的交易模式，用 U 买一切"的直接动因〔一手，纯前端遗留需求文档〕。

### 4.2 功能矩阵

**交易**
- USDC 一键买全网（含跨链，用户无感）
- Apple Pay / 卡 直接入金买币（Crossmint Token Checkout 提供）
- Gas 全代付（用户无需持有任何原生代币）
- 提现：链上提现 + 法币出金经 **Spritz Finance**（`app.spritz.finance`）
- 限价单 / TP / SL：**在做，先只做 SOL**（创始人公开承认非托管跨 5 链做真限价单"extremely technical"）
- 无滑点自定义、无加速档位〔一手〕

**社交（核心差异化）**
- **Feed**：交易实时进流，可看可抄
- **Copy trading / 跟单**：看他人操作与持仓走势
- **Leaderboard**：顶级交易者排行
- **Friends**：好友一起交易
- **Thesis**：直接在 K 线图上发表对某代币的观点
- **Profiles**：个人交易主页（含 avg entry/exit lines，Web 版缺）
- **CLANS**（2026-08-10 上线）：组队交易、组建"family"、共同积累受众；上线即 50+ clans
  → 内部研判：与 GMGN 的社交跟投/跟单场景**直接重叠**，是重点跟踪项〔一手〕
- Perps 与 feed / leaderboard / thesis / profile **完全打通**

**发现与信号**
- Trending / 已验证代币 / 持仓分布
- 代币关联 X 账号（帮用户判断真伪）
- **MC alerts / 热门代币推送（callout）**：按活跃交易者人数档位推送
  → 〔一手实测〕07-23 对 GME **一天推 11 次**；单日最高推送 23 条；档位为 20/40/80 traders

**Web vs App**〔一手〕
- Web 版**落后** App 版：缺 perps、缺 avg entry/exit lines
- 结论：FOMO 是**移动端优先**，Web 是补充

---

## 五、技术架构拆解（内部一手）

> 来源：Confluence《Fomo 交易方案调研》（Tun Liu，2026-07-14），基于 7 笔样本交易 + fomo.family HAR 抓包。这是本次调研最有价值的一手资产。

### 5.1 架构定位（五句话看懂）

1. **Solana 是资金主链** —— 用户资产最终全部归集到 Solana 钱包，其他链（含 Robinhood）只是**交易执行层**。
2. **Intent-based 跨链，非 lock-mint** —— 用户在源链存入 → Relay 的 solver 在目标链以**较少金额**执行（差价即桥费）→ 异步结算，约 **3 秒**。
3. **EIP-7702 + ERC-4337 做统一地址** —— 用户在 EVM 侧用 EOA，首次操作时由 Bundler 携带**预签的 7702 授权**一并上链，无需预部署合约钱包；gas 由 Bundler/Relayer 代付。
4. **Privy 密钥分片托管** —— 私钥拆成多份 share（Privy 服务端一份 + 设备一份），签名时前端 iframe 拉 share、本地重组、签名、销毁；换设备用 OAuth 恢复。
   ⚠️ **名义上 Privy 单方无法签名，但它持有 recovery share ≈ 实际具备全权控制能力**。这是 FOMO"自托管"叙事的**最大水分**，也是可用于对比传播的点。
5. **无自研路由，全外包** —— 同链走 **DFlow / Jupiter**（动态选路），跨链路由由 **Relay** 的 solver 决定。FOMO 只做前端 + 收费。

### 5.2 交易链路（HAR 实测时序）

```
T+0.000s  POST /swaps/v2  { inTokenId, outTokenId, amount, retry }
          → 后端构建 Solana 交易，用 feePayer 私钥签 sig[0]，返回半签名 tx + relaySwapId + 费用明细
T+0.696s  Privy iframe 从服务端拉 key share → iframe 内重组私钥 → 签 sig[1] → 销毁
T+0.697s  POST /swaps/v2/fast-fill   （意图是目标链预执行以缩短等待；当前未启用，返回 400）
T+1.254s  前端直连 Jito sendTransactionWeb（单笔提交，带 MEV 保护，非 bundle）
T+2.106s  每 500ms 轮询 /swaps/v2/status?relaySwapId=
T+4.5s    刷新 balances / swaps 确认到账
```

**关键观察**：
- **前端不构建交易**（只传币对和金额），**后端不参与提交**（签好的 tx 从不回传后端）。这是一个"后端构建 + 前端签名提交"的混合模式。
- Solana 交易带 `jitodontfront1111111111111111111TradeonFomo` 的 ComputeBudget hint（防抢跑标记 + 品牌植入）。

### 5.3 四种场景的资金与费用流

| 维度 | 同链 Swap | 跨链买入 (Sol→RH) | 跨链卖出 (RH→Sol) | 纯 USDC 归集 |
|---|---|---|---|---|
| 执行路径 | DFlow/Jupiter | USDC→WETH→Target | Target→WETH→USDC→桥 | 直接转账，无 swap |
| **平台费** | **阶梯（见 §6）** | **0.5%** | **0.5%** | **无** |
| 桥费 | 无 | Relay 隐含价差 | Relay 隐含价差 | Relay 隐含价差 |
| 收费方式 | 顶层独立 `transferChecked` 指令 | Relay 报价内含 `usdFees.app` | 同左 | 仅桥价差 |
| 确认时间 | 即时 | ~3s | ~3s | ~3s |
| 技术栈 | Solana Program | Solana Program + Relay | EIP-7702 + ERC-4337 + Relay | 同左 |

### 5.4 供应商依赖地图（外包程度极高）

| 环节 | 供应商 |
|---|---|
| 同链路由 | DFlow / Jupiter |
| 跨链 | **Relay**（solver、报价、代扣平台费、桥费） |
| 上链提交 | Jito（`sendTransactionWeb`，MEV 保护） |
| 密钥与钱包 | **Privy**（分片托管 + OAuth 恢复） |
| 法币入金 | **Crossmint**（Apple Pay Token Checkout） |
| 法币出金 | **Spritz Finance** |
| Perps | **Hyperliquid + Trade[XYZ]**（FOMO 收 builder-code 费） |
| EVM 智能账户 | EntryPoint v0.7 + Simple7702Account |
| 数据追踪 | PostHog |
| RPC | QuickNode（Robinhood mainnet） |

> **判断**〔推断〕：FOMO 的速度优势来自"**全部核心技术外包，自己只做体验和分发**"。这让它能在 8 天内接一条新链，但也意味着：① 无法做内盘；② 无法给用户交易参数控制权；③ 单点故障风险集中在 Relay 和 Privy；④ 一旦要做真限价单/更深的执行优化，会撞上外包的天花板——创始人自己承认了这一点。

### 5.5 已确认的硬伤〔一手〕

1. **跨链 ~3s 延迟**，vs 同链即时。
2. **7702 委托地址一个区块只能一笔交易** —— Robinhood 出块 0.1s 无感，但若扩展到 ETH（12s）连续操作必须等块。
3. **跨链仅支持外盘** —— Relay 只询价 Uniswap V3，内盘无法跨链交易。
4. **feePayer 代付 gas 无保护** —— 用户 USDC 余额不足导致 deposit 失败时，FOMO 后端**白亏链上 gas**，无前置余额校验或惩罚机制（已抓到失败样本）。
5. **仓位与 PnL 计算复杂** —— 跨链持仓数据导致盈亏口径复杂〔一手，07-14 会议结论〕。
6. **交易成功率与退款机制存在不确定性**〔一手，同上〕。

---

## 六、商业模式与费率

### 6.1 费率结构〔一手，链上多笔验证〕

**同链 Swap — 三档阶梯：**

| 交易额 | 费率 | 实测样本 |
|---|---|---|
| ≤ 200 USDC | **固定 0.95 USDC/笔** | 2.00U 交易收 0.95（**实际费率 47.5%!**）；184.64U 收 0.95（0.51%）|
| 200 ~ 10,000 USDC | **0.5%** | 226.67U 收 1.133362（0.50%）|
| ≥ 10,000 USDC | **0.05%** | — |

> ⚠️ **最重要的一条**：小额用户被**极度惩罚**。买 $2 收 $0.95 = 47.5%。这解释了 App Store 上"这个应用只有你有 1 万美元以上才好用""费用太高不推荐"的负评来源，也是**我们最直接的攻击点**：对小额用户，GMGN 的比例费率完胜。

**跨链 Swap**：统一 **0.5% 平台费**（由 Relay 在报价中代扣，HAR 确认 `feeTierBps: 50`、`usdFees.app`）+ Relay 桥费（隐含价差）。
**纯 USDC 归集**：不收平台费（系统自动行为）。

**邀请码折扣**〔一手〕：未填邀请码 0.5%，填了 **0.45%**（即 10% 折扣）。

### 6.2 分润机制〔一手〕

卖出交易中 0.95 USDC 被拆成两笔：
- **75%（0.7125 USDC）→ FOMO 平台**（`R4rNJHaffSUotNmqSKNEfDcJE8A7zJUkaoM5Jkd7cYX`）
- **25%（0.2375 USDC）→ 推荐人/前端**（`Hy9JKVSEjgZgui13cgzfXvEtHL22ZUfm9V31Lj9uC2p9`）

买入交易未观察到分成——**分成是否发生取决于用户是否绑定推荐人**〔推断〕。

官方 referral 文档口径〔公开〕：所有 USD 推荐奖励从 FOMO **净费**中分出（合作方扣除后为 0.1% 总交易费口径），按推荐层级分配，实时结算、无上限。

### 6.3 推荐码泛滥现象〔公开，值得警惕〕

搜索"fomo referral code"会出现大量第三方站点，宣称的折扣从 10%、20% 一路虚标到 **90%、95%**（`SAVE90`、`OFF95` 等）。实际官方口径是 10% 终身折扣。
→ **含义**〔推断〕：FOMO 的增长有很大一部分被**联盟/SEO 套利者**驱动。这带来量，但也带来质量噪音和虚假宣传的品牌风险。**这是可以在舆情上使用的素材，也提醒我们自己的 affiliate 体系要控预期。**

### 6.4 收入结构小结

- **DefiLlama 口径下 98.5% 收入来自 Solana 现货**（8/08 周），perps 只贡献 $38.8K —— 就该口径而言 **perps 目前是叙事而非收入**。⚠️ 但跨链平台费在链上无独立转账、大概率不在该口径内，**Robinhood 等链的真实贡献未知**，详见 §3 的口径陷阱。
- 收入 = 笔数 × 约 $0.76/笔〔推断〕→ 增长必须靠**用户数与交易频次**，而非提高客单价。
- 收费钱包（Solana）：owner `R4rNJHaffSUotNmqSKNEfDcJE8A7zJUkaoM5Jkd7cYX`，USDC ATA `HrTf9CzXR1dRH4Sof5QrpmGWwpwAf3qZzwCsEjQpXcSq` —— **可持续监控其净流入作为 FOMO 收入的实时代理指标**〔一手，建议做成日报〕。

---

## 七、增长与市场策略

### 7.1 KOL 矩阵〔一手，25+ 账号分析〕

**打法规律**：
1. **月初用链官方号造势** —— @BNBCHAIN（3.9M）、@base（1M）先起量。
2. **随后每天有 KOL 发声**，主力粉丝量 **10k~400k**。
3. **KOL 画像**：大部分给 **Coinbase** 做过宣传，少部分给币安/Bybit；覆盖 @farokh(454.8K)、@frankdegods(430k)、@brave(353.1k)、@Bankless(328.4k)、@econoar(191.9k)、@SpiderCrypto0x(117.3k)、@TaikiMaeda2(102k)、@js_horne(zora 联创)、@j0hnwang(Kalshi 加密主管)、@KaitoAI、@privy_io 等。
4. **少量 2k~10k 小号专职为 FOMO 做增长**（如 @PaulErlanger —— 即创始人本人账号）。

**判断**〔推断〕：这是一套**"西方主流加密 + 消费科技"**的 KOL 组合，不是华语/亚洲交易员圈。它在争夺的是 **Coinbase/Robinhood 溢出的美国零售用户**，与 GMGN 的核心用户池**部分错位**——这既是我们的缓冲，也是我们的盲区。

### 7.2 争议：KOL favoritism〔一手〕

X 上唯一带**情绪对立**的议题（4 条 + 引用扩散）：用户指责 FOMO 优先 KOL listing、忽视 bagworkers / meme 社区 / 零售用户。
创始人**没有正面否认**，而是选择"增加 sponsored creators 透明度"侧面回应 → **说明确有其事**。
→ 可用素材：FOMO 的排行榜与推送公信力存在被质疑的空间。

### 7.3 推送（callout）作为增长武器〔一手，影子测试实测〕

FOMO 已上线 20/40/80 traders 档位的热门代币推送。07-23 实测：
- 单日最高推送 **23 条**，对单一热点（GME）**一天推 11 次**
- 推送极其激进，市值回落中仍做同档重推

**我们的影子测试对照结果（07-23 全天）**：

| 指标 | 我们（规则口径） | FOMO |
|---|---|---|
| 覆盖币数 | **14 / 14**（FOMO 推的 8 个全覆盖） | 8 / 14 |
| 20t 首触更早 | **6 币**（AI 早 26min / TREX 早 6min / BUCK 早 35min / GME 早 12min / AMC 早 8min / DIH 同分钟） | 1 币（Hoodog 早 24min） |
| 独有推送 | 6 币 + GME 飙升晋级③ | GME 回落重推 3 条 |

→ **结论**：在信号质量与时效上**我们的数据基础更好**（能拦下 FOMO 无法识别的 BSC 鲸鱼对倒盘、代币化股票伪触发）。但**FOMO 已经先上线，用户心智正在被建立**。这是典型的"技术领先、心智落后"局面。

### 7.4 其他增长杠杆

- **Apple Pay 入金**（Crossmint）：68,000+ 首次买币用户，$25M —— 这是**最难被复制的一环**，涉及支付合规。
- **Affiliate 计划**：`fomo.family/affiliates`，实时结算、无上限。
- **Pump.fun 挖角战**（2026-08-09）：$20k 签约 + $30k/月抢 FOMO 用户 → 反向证明 FOMO 用户价值。

---

## 八、用户口碑与真实问题

### 8.1 评分与整体情绪

- App Store：**4.6★**，698+ 评价（2026-07）
- Trustpilot：仅 2 条评价，均 1 星〔公开〕
- X 上情绪〔一手，2026-07-05~06 盘点〕：**18+ 条泛支持 vs ~25 条具体抱怨** —— 仍处**蜜月期**，但抱怨已具体化

### 8.2 用户最认可的点（按提及密度）〔一手〕

1. **Apple Pay 买 meme 币**——被反复称为 "game changer"
2. **UI 直观、对新手极友好**——"这才是现代加密货币交易应有的方式"
3. **社交/跟单**——"X 上太多账号要关注，很多 KOL 偷偷抛售；这是最透明的方式看谁在赚钱"
4. **费用低**——多人明确对比 Moonshot："Moonshot 对 $250 以下交易收 2.5%，比 FOMO 高 5 倍"
5. **上市前接触代币**——"像在 crypto 语境下打开了私募市场"
6. **执行快、发版频繁**

### 8.3 用户最不满的点（按严重度）

| 问题 | 严重度 | 细节 | 官方态度〔一手〕 |
|---|---|---|---|
| **提现困难 / 出金复杂** | 🔴 高 | 多起"卖了币点提现 5 天没到账"、"没有直接提到银行的功能"、客服只回自动消息 | 开发者回复：出金要去 `app.spritz.finance` 走——**即出金体验被外包且不在 App 内闭环** |
| **BNB 链性能** | 🔴 高 | 约 7 条：交易慢、高波动时延迟填充/不填充 | 承认在修，"have a few things in mind"，**方案未定** |
| 入金扣款未到账 / 资金冻结 | 🔴 高 | "存 100 被扣款但没到账"；失败交易资金冻结 1-3 工作日 | 未系统回应 |
| 成交价偏差 | 🟡 中 | 买入价高于设定、卖出价低于设定 | 未单独回复 |
| 价格更新滞后 | 🟡 中 | "应用上的价格严重滞后，也无法快速下单" | 未回应 |
| 缺止损/限价/买入限制 | 🟡 中 | 6 条 | 承认技术难，**先做 SOL** |
| 无私信、无自定义货币、无卖出 bot | 🟢 低 | 单点请求 | **一律不回** |
| Web 版功能缺失 | 🟢 低 | 缺 perps、avg entry/exit lines | 未回应 |
| **成为退出流动性** | 🟡 中 | "所有那些交易者都会利用你提供退出流动性"、"故意在即将下跌时推送买入警报" | 未回应 |
| 合作方信任风险 | 🟡 中 | 用户警告选 Rasmr 需谨慎，类比 Axiom 出过的问题 | 未回应 |

### 8.4 创始人回复策略画像〔一手〕

- **只正面接技术/性能类反馈**（BNB、限价单）
- **单点功能请求一律不回**（sell bot、货币显示、holder 切换、Web 功能）
- **情绪类用幽默化解**（"how about just manifesting a great july"）
- 回复集中在 **7/5 晚 22:16–22:41 一个时间窗** —— 典型 founder 集中扫 mentions 模式
- 对新链请求给 👀（有兴趣不承诺）——**但 8 天后就上线了 Robinhood Chain**

> **判断**〔推断〕：FOMO 的产品决策**高度创始人驱动、高度机会主义**。公开表态保守，实际执行激进。**不要用它的公开表态预测它的路线图。**

### 8.5 关键结构性矛盾

FOMO 的核心矛盾是：**它用"简单"吸引小白进来，但小白遇到的第一个真问题（出金、失败交易、被当退出流动性）恰恰是"简单"掩盖掉的复杂性。** 目前靠人工客服个案补偿在扛（有用户因客服"破例赔付"而把 1 星改成好评）。这套打法在 62.5 万用户量级还能撑，**到几百万量级会成为它的定时炸弹**〔推断〕。

---

## 九、我们 vs FOMO：能力对照

| 维度 | GMGN | FOMO | 判断 |
|---|---|---|---|
| **入金门槛** | 需自备链上资产/原生代币 | **Apple Pay 直接买 + USDC 全链通用 + gas 全代付** | ❌ **FOMO 明显领先** |
| **跨链体验** | 有跨链概念，用户需感知 | 用户完全无感，单一余额 | ❌ FOMO 领先 |
| **内盘/首发** | ✅ 支持 | ❌ 不支持（Relay 只询价 Uniswap V3） | ✅ **我们领先** |
| **交易参数控制** | 滑点/优先费/加速可调 | ❌ 全无 | ✅ 我们领先 |
| **执行速度（同链）** | 自研，可加速 | 即时但无加速选项 | ✅ 我们领先 |
| **执行速度（跨链）** | — | ~3s 异步 | 🟡 各有取舍 |
| **数据与分析深度** | 自研链上数据（Smart Money、鲸鱼、税率、DYOR、钱包画像） | 浅（外部路由 + 简单看板） | ✅ **我们大幅领先** |
| **信号/推送质量** | 07-23 实测 14/14 覆盖，6 币首触更早，有质量闸拦假热度 | 8/14 覆盖，无质量闸（BSC 对倒盘、代币化股票会误触） | ✅ 我们领先（但**上线晚**） |
| **社交** | 跟单/跟投在做 | **Feed + Leaderboard + Thesis + Friends + CLANS**，与 perps 全打通 | ❌ **FOMO 明显领先** |
| **Perps** | — | 已上线（Hyperliquid + Trade[XYZ]，非美用户），可交易 pre-IPO/股票/指数/商品 | ❌ FOMO 领先 |
| **限价单/TP/SL** | ✅ 有 | ❌ 在做，只 SOL | ✅ 我们领先 |
| **费率（小额）** | 比例费率 | **≤200U 固定 0.95U（$2 交易收 47.5%）** | ✅ **我们大幅领先** |
| **费率（大额）** | — | ≥10,000U 仅 0.05% | ❌ FOMO 更狠 |
| **自托管真实性** | 用户自持 | Privy 分片，**Privy 持 recovery share ≈ 具备全权控制** | ✅ 我们更真 |
| **移动端体验** | 专业但重 | 极简、消费级 | ❌ FOMO 领先 |
| **本地化** | 多语言（正在做阿拉伯语） | **仅英文** | ✅ **我们领先** |
| **出金** | 链上 | 需跳出 App 到 Spritz，投诉集中区 | ✅ 我们领先 |
| **可被追踪性** | 我们的交易可被解析 | **FOMO 的 Relay 代发交易在我们的 Tracker 里追踪不到** | ⚠️ **这是我们的 bug，不是它的优势** |

### 9.1 特别说明：FOMO 交易解析缺口（我们的当前故障）〔一手〕

**现象**：同一钱包在第三方工具（Ray Quartz、Debot、basedbot）能看到 FOMO 交易，在 GMGN Wallet Tracker / K 线买卖点里**看不到**。已有 KOL（Gabbens）正式提诉求。

**根因**（已定位）：FOMO 买单走 Relay 代发 —— relayer 先在 DEX 把币买下，再由 Relay 路由合约（`0xb92fe925dc43a0ecde6c8b1a2709c170ec4fff4f`）转给用户钱包。**用户钱包既不是发起方也不是接收合约，只出现在最后一跳转账里**。我们把这笔"买入"记在了 relayer 名下，用户钱包名下只剩一条金额为 0 的转入记录 → K 线买卖点、关注/追踪列表（都按钱包维度取数）全部看不到。

**坐实样本**：BSC 2026-07-25 11:23:57，tx `0xed986e6a...cd4f8`，$584.28 买入被归属到 relayer `0xa67d7eb4...93fbb`。同钱包近 10 天在 BSC 有 11 笔、Base 有 2 笔同类交易全部未归属。（对照：该钱包的**卖出**走 ERC-4337 通道，归属正确 → 用户看到"有卖出、没买入"。）

**修复方向**：把 Relay 路由合约识别为中转，按「路由合约收币后转给谁」定买卖归属，而非按交易发起方。

**已立项**〔一手 Jira〕：
- `GMGN-8687` BSC 链支持 FOMO relay 交易解析为转入/转出（父任务）
- `GMGN-8688` FOMO relay 解析异常：合约地址一直转出无转入
- `GMGN-8689` FOMO 账号从 BSC 经 relay 跨链兑换仍被解析为卖出（预期应为转出）
- `GMGN-8665` 代币页 Trades 新增「转入/转出」类型 + fomo 子 tab
- `GMGN-8409` 持仓 token 信号提示优化——**文案直接采用 Fomo 风格**（主标题涨幅 + 副标题买入时长，无 emoji，倍数用大写 X）

⚠️ **风险提示**〔一手〕：为免责，我们目前把 relay 交易解析为「转入/转出」而非「买/卖」——因为**无法识别投毒**。历史上 FOMO 相关地址的投毒币种主要是链上直接发出的、安全检测不合规的小额代币；**在我们做过一次攻防对抗后，对方已把金额提高到 50~100U**。Kenny 的技术结论：链上没有准确数据可区分真实发起人与伪造，Relay 接口虽能拿到实际发起人地址但爬虫调用不稳定（延迟 + 限频），跨链场景下发起人地址无法在 EVM 上归属。**"技术上完全规避投毒并且还能识别"目前不现实**——需要产品侧用标注/提示来兜。

---

## 十、威胁评估与行动建议

### 10.1 威胁分级

| 威胁 | 等级 | 理由 |
|---|---|---|
| **抢占新增用户入口** | 🔴 **最高** | Apple Pay + USDC 全链 + gas 代付，68k 首次买币用户，日增 3k+。这些用户**从未见过 GMGN**，心智一旦形成极难夺回 |
| **社交护城河成型** | 🔴 高 | Feed + Leaderboard + Thesis + CLANS 已形成网络效应；Pump.fun 都在抄。社交是**越晚做越贵**的能力 |
| **推送心智抢跑** | 🟠 中高 | 我们信号质量更好但上线更晚；FOMO 已在建立"FOMO 会告诉我哪个币要涨"的心智 |
| **追踪缺口导致用户流失** | 🟠 中高 | 我们看不到 FOMO 交易 → 我们的 Smart Money / 跟单数据出现系统性盲区 → **KOL 已在投诉，且第三方工具能做到而我们做不到**，直接伤专业用户信任 |
| **巨鲸/高市值币交易迁移** | 🟡 中 | 2025-11 KOL 反馈已有迁移迹象，需量化监控 |
| **perps 打通社交** | 🟡 中 | 目前只占收入 1.5%，但一旦跑通就是第二增长曲线 |
| 费率战 | 🟢 低 | 它小额费率比我们贵，大额才便宜，不构成全面价格威胁 |

### 10.2 建议行动（按优先级）

**P0 — 止血（本周）**
1. **修完 Relay 交易解析归属**（GMGN-8687/8688/8689）。这是**正在流失专业用户信任**的活口子。第三方（Debot/basedbot）能做，我们做不到，说明这不是不可解的技术问题。
2. **给 FOMO 交易打专属标签**并在代币页 Trades 加 fomo 子 tab（GMGN-8665 已立项）——把"看不到"转成"看得比别人清楚"，反手变成差异化：**我们是唯一能标出"这是 FOMO 用户在买"的终端**。
3. **上线 FOMO 收费钱包监控日报** —— 监控 `HrTf9CzXR1dRH4Sof5QrpmGWwpwAf3qZzwCsEjQpXcSq` 净流入，作为 FOMO 收入的实时代理指标。这比等第三方报道快一周。

**P1 — 对标补齐（本季度）**
4. **热门代币推送尽快全量上线**（PRD v1.2 已定稿）。我们的规则在时效与覆盖上实测胜出，**唯一劣势是时间**。同档重推规则已按 FOMO 口径（够条件就推）调整——方向对。
5. **"用 U 买一切"专项**（Q3 已立项）—— 这是 FOMO 最强的一击。**建议明确拆成两步走**：
   - 第一步：**统一 USDC 余额 + gas 代付**（用户体验的 80% 来自这里，不必先解决跨链）
   - 第二步：跨链无感。技术路径上，07-14 会议结论是"自建跨链桥复杂度极高、不现实，Relay 是目前唯一可行方案，但需与 Relay 建立深度商务合作以保障服务质量"。**建议尽快启动 Relay BD**——它是 FOMO 的单点依赖，也应该是我们的谈判杠杆。
6. **小额费率对比作为增长素材** —— FOMO $2 交易收 47.5%。这是可以做成传播物料的硬事实。

**P2 — 差异化（下季度）**
7. **社交/组队**：CLANS 与我们的跟投场景直接重叠，需要产品层给出应对（不一定是抄 CLANS，可以是"用真实链上数据背书的组队"——FOMO 的排行榜有 KOL 偏袒争议，我们有数据公信力）。
8. **本地化打差异**：FOMO 仅英文。阿拉伯语等 RTL 语种是**它短期不会碰**的市场（阿语适配已在推进，周期约 2 周）。这是低成本高确定性的增量。
9. **攻它的"自托管"叙事**：Privy 持有 recovery share ≈ 实际具备全权控制。这是可验证的技术事实，不是攻击性言论。

**P3 — 持续监控**
10. 建立 FOMO 周报机制：收费钱包净流入、DefiLlama 收入、App Store 排名/评分、X 舆情、新功能上线（CLANS 之后是什么）、链覆盖变化。竞品社群自动监控页已在跑，建议把 FOMO 单独拉出成一页。

---

## 十一、情报缺口与待验证清单

| # | 待查 | 为什么重要 | 建议方法 |
|---|---|---|---|
| 1 | FOMO 真实 DAU / 留存曲线 | 625k 是注册数，29% trader/user 是单点观测。**没有留存数据就无法判断增长质量** | 第三方 App 数据（Sensor Tower/data.ai）；链上活跃钱包数估算 |
| 2 | **各链收入拆分（已升级为 P0 级情报缺口）** | "98.5% 来自 Solana"是 DefiLlama 的测量口径产物；跨链平台费链上无独立转账，**Robinhood / Base / BNB / Monad 的真实贡献完全未知**。这直接影响我们对"要不要跟进 RH 链"的判断 | 见 §3 口径陷阱中的方法 A/B/C/D —— 方法 A（统计跨链桥程序 USDC 存入量 × 0.5%）一天可出结果 |
| 3 | Robinhood Chain 上 FOMO 的实际体量 | 我们已知它技术上支持，但不知道用了多少。RH 链 7 月上线即 $305M TVL、1M 周活地址，且**memecoin 而非股票主导** | RH 链上 FOMO 相关合约统计 |
| 4 | Privy recovery 的实际治理条件 | "≈全权控制"目前是技术推断，若要对外使用需坐实 | Privy 公开文档 / 安全审计报告 |
| 5 | FOMO 的 KOL/sponsored creator 商务条件 | 决定我们抢 KOL 的报价 | BD 侧打听 |
| 6 | 限价单 SOL 版何时上线 | 上线即抹平我们一个优势 | 监控 App 更新日志 + X |
| 7 | Pump.fun 挖角战果 | 检验 FOMO 用户粘性的天然实验 | 监控双方交易量变化 |
| 8 | FOMO 是否会发币/上积分 | 会大幅改变增长曲线和用户质量 | 监控官方渠道 |
| 9 | 团队规模与组织 | 判断它的迭代上限 | LinkedIn / 招聘信息 |
| 10 | 出金（Spritz）失败率 | 它最大的软肋，量化后可作为攻击点 | 舆情抓取 + 实测 |

---

## 十二、附录

### 12.1 FOMO 关键地址与接口索引〔一手〕

**Solana**

| 名称 | 地址 |
|---|---|
| 收费钱包 owner | `R4rNJHaffSUotNmqSKNEfDcJE8A7zJUkaoM5Jkd7cYX` |
| 收费 ATA (USDC) | `HrTf9CzXR1dRH4Sof5QrpmGWwpwAf3qZzwCsEjQpXcSq` |
| 推荐人分润样本钱包 | `Hy9JKVSEjgZgui13cgzfXvEtHL22ZUfm9V31Lj9uC2p9` |
| 跨链桥程序 | `99vQwtBwYtrqqD9YSXbdum3KBdxPAVxYTaQ3cfnJSrN2` |
| feePayer（后端持有） | `AgmLJBMDCqWynYnQiPCuj9ewsNNsBJXyzoUhD9LJzN51` |
| Solana Relayer (RH→Sol) | `F7p3dFrjRTbtRp8FRF6qHLomXbKRBzpvBLjtQcfcgmNe` |
| DFlow 路由 | `DF1ow4tspfHX9JwWJsAb9epbkA8hmpSEAtxXy1V27QBH` |
| Jupiter 路由 | `JUP6LkbZbjS1jKKwapdHNy74zcZ3tLUZoi5QNyVTaV4` |
| ComputeBudget hint | `jitodontfront1111111111111111111TradeonFomo` |

**Robinhood Chain（Chain ID 4663）**

| 名称 | 地址 |
|---|---|
| RelayApprovalProxyV3（跨链入口） | `0xccc88a9d1b4ed6b0eaba998850414b24f1c315be` |
| Relayer (Sol→RH) | `0xa67d7eb4dc68fa6ce8e34ef8cadaf075b9893fbb` |
| Filler | `0xf70da97812cb96acdf810712aa562db8dfa3dbef` |
| **RelayRouterV3（解析归属关键）** | `0xb92fe925dc43a0ecde6c8b1a2709c170ec4fff4f` |
| RobinHoodSettler（V3 路由） | `0xe72688f7d25d7318b9a81f21edda640ca948c83b` |
| 桥合约 (RH→Sol) | `0x4cd00e387622c35bddb9b4c962c136462338bc31` |
| EntryPoint v0.7 | `0x4337084d9e255ff0702461cf8895ce9e3b5ff108` |
| Smart Account 实现 (EIP-7702) | `0xe6cae83bde06e4c305530e199d7217f42808555b` |
| Bundler（归集 / 卖出） | `0x433702873e33d4846d399a75aaf96eacf181d0b2` / `0x4337001fff419768e088ce247456c1b892888084` |

**接口**

| 用途 | 端点 |
|---|---|
| 后端 API | `prod-api.fomo.family` |
| 建交易 | `POST /swaps/v2` |
| 预执行（未启用） | `POST /swaps/v2/fast-fill` |
| 状态轮询 | `GET /swaps/v2/status?relaySwapId=` |
| WebSocket | `wss://prod-api.fomo.family/ws` |
| EVM RPC 代理 | `evm-data.prod-edge.fomo.family/robinhood-mainnet/v2` |
| 上链提交 | `mainnet.hudson.jito.wtf/api/v1/sendTransactionWeb` |
| 分析 | PostHog (`app-actions.fomo.family`) |

**Network ID 映射**：`792703809` = Solana（Relay 内部）· `1399811149` = Solana（FOMO tokenId 拼接）· `4663` = Robinhood Chain

### 12.2 内部资料索引

| 文档 | 链接 |
|---|---|
| Fomo 交易方案调研（技术一手，最有价值） | [nfttrack/2306736154](https://pionex.atlassian.net/wiki/spaces/nfttrack/pages/2306736154/Fomo) |
| Fomo App 用户反馈盘点（X 平台）2026-07-05~06 | [GMGNA/2294843000](https://pionex.atlassian.net/wiki/spaces/GMGNA/pages/2294843000/Fomo+App+X+2026-07-05~06) |
| fomo 体验（产品结构 + App Store 评论全量） | [GMGNA/1545994241](https://pionex.atlassian.net/wiki/spaces/GMGNA/pages/1545994241/fomo) |
| fomo 在 twitter 合作 KOL 背景分析 | [GMGNA/1576534179](https://pionex.atlassian.net/wiki/spaces/GMGNA/pages/1576534179/fomo+twitter+KOL) |
| 07-23 推送实盘复盘 · 我们 vs FOMO 对照总表 | [GMGNA/2318106804](https://pionex.atlassian.net/wiki/spaces/GMGNA/pages/2318106804/07-23+vs+FOMO) |
| 热门代币推送 PRD v1.2 | [GMGNA/2315976817](https://pionex.atlassian.net/wiki/spaces/GMGNA/pages/2315976817/v1.2) |
| 竞品社群更新&讨论汇总（自动更新） | [个人空间/2307850289](https://pionex.atlassian.net/wiki/spaces/~712020158205a1add2439fae73253b196308bc/pages/2307850289) |
| Jira | GMGN-8687 / 8688 / 8689 / 8665 / 8409 |

### 12.3 外部资料来源

**融资与公司**
- [Fortune — Index Ventures, USV back Fomo at $550M valuation](https://fortune.com/2026/06/22/fomo-series-b-fundraise-index-ventures-union-square-ventures/)
- [The Block — Fomo raises $75M at $550M valuation](https://www.theblock.co/post/405563/crypto-trading-app-fomo-raises-75-million-at-550-million-valuation-in-index-ventures-led-series-b-report)
- [insights4vc — FOMO: Behind the $75M Series B（含单位经济学质疑）](https://insights4vc.substack.com/p/fomo-behind-the-75m-series-b-from)
- [Yahoo Finance — Why Benchmark made a rare crypto bet, $17M Series A](https://finance.yahoo.com/news/why-benchmark-made-rare-crypto-140000489.html)
- [FinTech Futures — New York start-up Fomo raises $75m Series B](https://www.fintechfutures.com/venture-capital-funding/fomo-lands-75m-series-b)
- [TechTimes — Fomo raises $75M as SEC clears non-custodial wallets](https://www.techtimes.com/articles/318895/20260623/social-crypto-trading-app-fomo-raises-75m-sec-clears-non-custodial-wallets-operate.htm)

**数据与市场份额**
- [Solana Compass — FOMO $2.64M weekly revenue ATH, outpacing Phantom & Jupiter](https://solanacompass.com/news/fomo-posts-264m-weekly-revenue-all-time-high-on-solana-outpacing-phantom-and-jupiter)
- [Solana Compass — FOMO breaks weekly revenue ATH at $1.57M](https://solanacompass.com/news/fomo-social-trading-app-hits-157m-weekly-revenue-all-time-high-on-solana)
- [Solana Compass — Fomo surpasses Axiom as Solana's top daily trading terminal](https://solanacompass.com/news/fomo-overtakes-axiom-as-solanas-top-daily-trading-terminal-by-volume)
- [CryptoBriefing — Fomo surpasses Axiom for top daily Solana volume](https://cryptobriefing.com/fomo-surpasses-axiom-solana-trading-volume/)
- [CryptoBriefing — Fomo and Pump.fun battle for trader flow](https://cryptobriefing.com/fomo-pumpfun-solana-memecoin-competition/)
- [CryptoBriefing — Fomo overtakes Hyperliquid in 24-hour revenue](https://cryptobriefing.com/fomo-overtakes-hyperliquid-24-hour-revenue/)
- [DefiLlama — fomo Fees, Revenue & Volume](https://defillama.com/protocol/fomo)

**产品与生态**
- [fomo.family](https://fomo.family/) · [Clans](https://fomo.family/clans) · [Affiliates](https://fomo.family/affiliates) · [Series B 公告](https://fomo.family/blog/fomo-series-b)
- [docs.onfomo.com — Referral Rewards](https://docs.onfomo.com/rewards-system/referral-rewards)
- [Crossmint — How fomo scaled to $2.5B volume with Token Checkout](https://www.crossmint.com/announcement/fomo-crossmint-token-checkout)
- [QuickNode Builders Guide — fomo by FOMO Labs](https://www.quicknode.com/builders-guide/tools/fomo-by-fomo-labs)
- [Bankless — Fomo Is Leading the Charge for Social Trading's Next Wave](https://www.bankless.com/read/fomo-is-leading-the-charge-for-social-tradings-next-wave)
- [App Store — fomo: never miss out](https://apps.apple.com/us/app/fomo-never-miss-out/id6741115427) · [Google Play](https://play.google.com/store/apps/details?id=family.fomo.app)
- [CoinLaunch — Fomo 项目分析（含发币可能性推测）](https://coinlaunch.space/projects/fomo-family/)

**行业背景**
- [CoinDesk — Robinhood built a blockchain for tokenized stocks, memecoins took over](https://www.coindesk.com/tech/2026/07/13/robinhood-built-a-blockchain-for-tokenized-stocks-memecoins-took-over)
- [Motley Fool — Robinhood's new blockchain has tripled in size since mid-July](https://www.fool.com/investing/2026/07/31/robinhoods-new-blockchain-has-tripled-in-size-sinc/)

**用户口碑（第三方评测，质量参差，仅作情绪参考）**
- [BrokerListings — Fomo App Review: Legit Or A Scam?](https://brokerlistings.com/scams/fomo)
- [CoinSpot — Fomo Crypto App Review 2026](https://coinspot.io/en/reviews/fomo-crypto-app/)

---

*本报告基于 GMGN 内部一手调研（链上实测、HAR 抓包、影子测试、社群监控）与公开信息交叉整理。所有未审计的第三方数字均已标注口径。*
