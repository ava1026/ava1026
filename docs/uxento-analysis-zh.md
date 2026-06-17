# Uxento 发币 / 交易工具分析

> 整理日期:2026-06-17。本文基于公开网络资料(官网、GitBook 文档、Chrome Web Store / chrome-stats、X/Twitter、DEX Screener、第三方信誉评级站点)整理。**部分官网与文档页在采集时返回 403,行情、用户数等为公开快照,可能与实时不符。本文仅供研究与尽职调查参考,不构成任何投资或使用建议。** 加密领域(尤其是 memecoin 工具)风险极高,使用前请独立核实。

## 一、Uxento 是什么

Uxento 是一套面向加密货币(主要是 Solana 生态,并扩展到多链)的 **"degen" 投机交易者与代币发行者**工具集,核心卖点是"既能交易、又能一键发币 / 抄盘(vamp)"。它**不是**传统意义上的合规募资平台(launchpad),而更接近 **pump.fun 一类 memecoin 的"部署 + 狙击 + 跟单 + 信息追踪"自动化工具**。

产品形态主要有三块:

1. **uxtension(Chrome 浏览器扩展)** —— 主力交易与发币工具,内嵌交易面板、狙击、跟单、信息流追踪,深度集成 Axiom 交易前端。
2. **uxento.io 主站 / app(uLaunch 平台)** —— CT(Crypto Twitter)、Truth Social、Streamflow 锁仓、Telegram 合约地址(CA)、DEX、News 等多源"alpha 信息"追踪看板,以及面向活跃 deployer 的页面。
3. **uDev** —— 发币(部署 / 抄盘)引擎,贯穿扩展与主站。

官方自报数据(未经第三方审计,应视为营销口径):2026 年"#1 部署平台",约 2 万+ 扩展用户、1 万+ 网站注册、63.1 万+ 次部署。

## 二、发展历史 / 时间线

> 时间点据 X 官方/社区帖与 Chrome 商店元数据推断,可能有数日误差。

| 时间 | 事件 |
|---|---|
| **2025 年 5 月** | uxtension 浏览器扩展正式上架 Chrome Web Store,**免费**下载;早期以"快速 CT/meme 追踪器 + Axiom 增强"切入,积累首批用户。 |
| **2025 年 7 月 11 日** | **主平台正式上线**:整合 CT 追踪、Truth Social 追踪、Streamflow 锁仓追踪、Telegram CA 追踪,以及 uDev 发币/抄盘。 |
| **2025 年下半年** | 推出 **uLaunch**(私有 CT Tracker、大量 UI 自定义、面向活跃 deployer 的新页面);bundler 钱包上限由 3 个提升到 **10 个**;多链发币(BNB、Monad、BASE)陆续加入。 |
| **后续迭代** | 推出 **uAI**(AI 自动发币/自动跟单"自动驾驶"),uPoints 积分与多级返佣体系。 |
| **2026 年(快照)** | 扩展最新版本约 **2.8.x**(2026-05 前后更新),Chrome 商店评分约 **4.4 星 / 约 58 条评分**,在架用户约 **2 万**(官方口径含网站注册等可达更高)。 |

总体节奏:**先用免费追踪器扩展引流 → 再叠加发币/抄盘等高变现工具 → 再用积分/返佣/AI 自动化做留存与裂变**,迭代频率高。

## 三、核心功能全景

### 1. 发币 / 部署:uDev
- **基本流程**:填写代币字段(名称、符号、图片/元数据)→ 选择附加工具 → 输入首发买入的 SOL 或代币百分比 → 点击 **Deploy** 上链。
- **最低推荐启动资金:0.1 SOL**;默认 Solana,经左上角币种切换可在 **BNB Chain、Monad、BASE** 发币。
- 各链能力差异:Monad 支持 multi/cross-deploy;BASE 支持 multi/cross-deploy 与 auto-sell。

### 2. 抄盘:Vamp / Insta Vamp
- 一键**克隆已有(通常正在热炒的)代币**的元数据/形象并在数秒内重新发行。Insta Vamp 为一键动作。

### 3. 批量与开发者工具
- **Multi-Deploy / Cross-Deploy**:批量/跨链同时部署多个代币。
- **uDupe / uPloys**:复制、批量化部署。
- **Bundler + Sniper**:面向用多个钱包发币的 dev,可通过 Snipe/Bundle 配置按钮联动 uDev;**捆绑钱包上限 10 个**(可用 10 个钱包同时买入自己发的币——典型的"开盘护盘/做量/控盘"用途)。
- **Feed-based deployment**:基于信息流热点快速部署。

### 4. 信息追踪:Vision / AIO
- **AIO**:All-In-One 单一聚合信息流;**Vision**:把不同追踪器拆成多个独立流,**最多同时 3 个**(开 AIO 可看更多)。
- 可追踪来源:CA、CT、DEX、Streamflow Lock、Truth Social、Telegram、News。
- 支持关键词高亮、CA 检测自动狙击(Auto-Snipe)、关键词触发买入、通知声音等。

### 5. AI 自动化:uAI
- "自动驾驶"发币与交易:Quick Deploy 预设、Scraper(抓取)、Auto-Deployer、Auto-Sniper。

### 6. 交易与账户
- 内置交易面板,买/卖**手续费 0.75%**;狙击、双击发币、键位(keybinds)、白名单、组合(portfolio)跟踪。
- **Reclaim SOL**:关闭空代币账户、回收租金(rent)。

### 7. 经济激励:uPoints + 返佣
- **uPoints**:通过交易量与拉新获取积分。
- **多级返佣**:推荐他人(直接/间接/扩展三级)可分得其费用的一部分,外加 uPoints。
- 自有代币 **UXTO**:总量 10 亿,参考价约 $0.00078(微市值、高波动);在 Solana(FluxBeam/DEX)有交易对,并出现 BNB Chain 合约。**公开资料未清晰披露 UXTO 的具体效用与收入分成机制。**

## 四、X / 社区与用户反馈

> 综合 X(Twitter)官方与社区帖、Chrome Web Store / chrome-stats 用户评价。评分约 4.4 星(全时)、近期评分约 3.1,呈现明显两极分化。

### 正面反馈
- **快**:CT/追踪器响应快、可靠,被反复称赞"抓 runner(早期暴涨币)很快"。
- **免费 + 高频更新**:扩展免费,更新勤,社区活跃。
- **集成顺手**:与 Axiom 深度集成,All-in-One 工作流和 UI 增强受好评,被部分用户称为打 meme 的"alpha 利器"。

### 负面反馈 / 警示(重点)
- **钱包被盗(wallet drain)与疑似欺诈行为**在评论中**反复出现**——这是最严重、最值得警惕的信号。
- 与 Axiom 同用时**卡顿/性能问题**。
- 个别用户反映**账号被封**、申诉无回应。
- 注意:此类社区/商店评论真假混杂,既可能是真实安全事件,也可能是竞品抹黑或仿冒站连带影响,**不能单凭评论定性,但"wallet drain"反复出现必须高度重视**。

## 五、风险与尽调要点

### 1. 工具性质本身
- Vamp 抄盘克隆、批量/跨链发币、10 钱包捆绑买入、狙击、AI 自动发币——**天然服务于 memecoin 的高风险投机乃至"拉盘—砸盘(pump & dump)/收割"玩法**,与 rug pull 生态高度重合。使用者既可能获利,也极易成为接盘方。
- "0.1 SOL 即可发币 + 一键克隆热门币 + 10 钱包护盘"显著降低了发行欺诈性 memecoin 的门槛。

### 2. 浏览器扩展安全(最现实的威胁)
- 交易/发币扩展需**连接钱包并签名**,恶意或被劫持版本可发起钓鱼签名、恶意授权(approve)、窃取私钥/助记词。**商店评论里已多次出现 wallet drain 投诉。**
- 官方"完全不收集个人数据"为**自我声明**,无第三方审计佐证。
- **底线做法**:仅用全新隔离的 **burner 钱包** + 极小额资金 + 独立浏览器配置;绝不在主钱包连接;逐笔审查签名;定期撤销(revoke)授权。

### 3. 域名仿冒与信誉评级矛盾
- 存在 `uxento.io` / `.to` / `.cc` 等多个相似域名——**钓鱼仿冒高发信号**,务必只走官方核实过的入口。
- 第三方评级互相矛盾:Scam Detector 对 `.to` 给极低分并套用"预付费骗局"模板(很可能是通用误报);Scamadviser 对 `.to` 偏中性、对 `.io` 表示**无法确定、不推荐**。

### 4. 透明度不足
- 团队匿名、无可验证的合约/扩展代码审计、UXTO 代币经济学不清晰、自报数据无法核验——信任成本完全由用户承担。

## 六、结论(中立评估)

- **定位**:Uxento 是一款功能完整、迭代积极、在 degen 圈有真实用户量的 **Solana 多链 memecoin 交易 + 发币 + 信息追踪自动化工具**;追踪快、集成 Axiom、免费引流是其真实优势。
- **它没有板上钉钉是骗局的定论,但其核心功能服务于高风险投机/收割生态**;叠加商店里反复出现的 wallet drain 投诉、域名仿冒风险、扩展权限风险、透明度不足、评级矛盾——**整体风险等级判定为"高"**。
- **给尽调者/使用者的底线建议**:
  1. 只通过官方核实域名访问,警惕 .to/.cc 等仿冒站;
  2. 任何"发币/交易"操作都用 burner 钱包 + 小额,逐笔审签,定期 revoke;
  3. 不向任何"解锁/提现/税费"名目转账(经典预付费骗局特征);
  4. UXTO 视为高波动微市值投机品,而非有明确效用的资产;
  5. 多数司法辖区用此类工具批量发币/拉盘可能触及证券、欺诈、市场操纵红线,合规风险自担。

## 参考来源
- Uxento 官网:https://www.uxento.io/ ；app:https://app.uxento.io/login ；状态页:https://status.uxento.io/
- uDev 文档(GitBook):https://uxento.gitbook.io/uxento/tools/udev
- Uxento Vision 文档:https://uxento.gitbook.io/uxento/tools/uxento-vision
- uxtension(Chrome Web Store):https://chromewebstore.google.com/detail/uxtension/pljeffieceahpjcgldlglfidenecjloh
- uxtension 用户评价(chrome-stats):https://chrome-stats.com/d/pljeffieceahpjcgldlglfidenecjloh/reviews
- DEX Screener(UXTO 行情):https://dexscreener.com/solana/cx5naje7v5a8cljwstzstw2r2uqcp1ovzbjkrx61repo
- Bitget Wiki(UXTO 代币信息):https://web3.bitget.com/en/wiki/uxto-wallet
- X:扩展发布帖 https://x.com/twizzyGen/status/1921320397644959892 ；主平台上线 https://x.com/SolTraderLS/status/1943531244396122408 ；uLaunch 更新 https://x.com/uxento/status/1963035017472282917 ；官方账号 https://x.com/uxento
- Scamadviser:https://www.scamadviser.com/check-website/uxento.io
- Scam Detector:https://www.scam-detector.com/validator/uxento-to-review/
