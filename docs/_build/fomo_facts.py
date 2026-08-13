# -*- coding: utf-8 -*-
"""
FOMO 竞品情报 · 单一事实源（Single Source of Truth）

所有在多份文档中出现的数字都定义在这里。
  · 生成型文档（fomo-brief.html / fomo-growth-loop.html）在构建时从此注入
  · 手写型文档（fomo-product-research-2026-08.md/.html）由 check-facts.py 校验一致性

改数字只改这里。改完跑：
    python3 docs/_build/check-facts.py
"""

AS_OF = "2026-08-11"

# ── 资本 ────────────────────────────────────────────────
CAPITAL = {
    "valuation":      "$550M",
    "raised_total":   "$94M",
    "series_a":       "$17M",
    "series_b":       "$75M",
    "series_b_date":  "2026-06-22",
    "launch_date":    "2025-05-06",
}

# ── 规模（均为官方口径，未经审计）────────────────────────
SCALE = {
    "users":            "625,000+",
    "users_per_day":    "3,000+",
    "volume_total":     "$4B+",
    "first_time_buyers":"68,000",
    "first_time_value": "$25M",
    "app_store_rating": "4.6",
    "trades_per_day":   "128,000",
}

# ── 收入 ────────────────────────────────────────────────
REVENUE = {
    "weekly_ath":       "$2.64M",       # 截至 2026-08-08
    "weekly_ath_date":  "2026-08-08",
    "weekly_prev":      "$1.57M",       # 截至 2026-07-27
    "solana_share":     "98.5%",        # ⚠️ DefiLlama 口径，跨链收入不在其中
    "perps_weekly":     "$38.8K",
    "fee_per_trade":    "$0.76",        # 推断：实测日收 ÷ 日笔数
    "measured_daily":   "$96,789",      # 一手：2026-07-13 Solana 收费钱包净流入
    "measured_date":    "2026-07-13",
    "fees_30d":         "$9.48M",
    "revenue_30d":      "$8.79M",
    "referral_share":   "29%",          # 推断：由 30 天 fees/revenue 差额反推
}

# ── 费率 ────────────────────────────────────────────────
FEES = {
    "tier_small":       "0.95",         # ≤200 USDC 固定 USDC/笔
    "tier_small_eff":   "47.5%",        # $2 交易的实际费率
    "tier_mid":         "0.5%",         # 200–10,000 USDC
    "tier_large":       "0.05%",        # ≥10,000 USDC
    "cross_chain":      "0.5%",
    "referral_code":    "0.45%",        # 填邀请码后
    "referrer_cut":     "25%",          # 卖出侧分给推荐人
    "platform_cut":     "75%",
}

# ── 我们自己的费率（对照基准，内部三源一致）──────────────
#   《0427 运营活动方案》：每交易 $10 收 1% = $0.10
#   《竞品社群更新》：官方对用户口径「平台仅收 1% 手续费」
#   《App Store 投放策略》：中位月交易额 $609–630 → 月产生 ~$6 手续费 ≈ 0.98%
#   ⚠️ 是否全链/全产品线一致、有无 VIP 折扣待确认，见待验证队列 #16
GMGN_FEES = {
    "flat":       "1%",
    "breakeven":  "$95",     # 0.95 USDC 固定档 = 1% × 95
}

# ── 交易量对照（Arthur v5 · 同窗口同链重算）─────────────
#   ⚠️ 口径警告（两边都适用）：DefiLlama 的链覆盖不完整——
#     · 漏掉 FOMO 的跨链收入（平台费在 Relay 报价内含扣除，链上无独立转账）
#     · 漏掉 GMGN 的 Robinhood 链（把我们算低了）
#   所以"Axiom 第一 / 我们与 FOMO 差距不到 2%"的旧口径已作废。
#   引用任何 DefiLlama 排名前，先确认它覆盖了哪几条链。
VOLUME = {
    "gmgn_30d":  "$2.6B",
    "fomo_30d":  "$1.7B",
    "axiom_30d": "$1.6B",
    "gmgn_24h":  "$89M",
    "fomo_24h":  "$71M",
    "axiom_24h": "$69M",
    "note":      "同窗口同链重算，两个窗口 GMGN 均第一",
}

# ── Arthur v5 带来的机制事实（一手对话 / 当事人亲述）──────
#   这些是我们此前完全没有的一层：飞轮的燃料。
ARTHUR = {
    # BenTodar 亲述 Pump.fun「配合造战绩」四步
    "pump_playbook": "给低市值币合约地址 → 让他先买 → 平台拉盘 → PnL 亮眼",
    # Dani（daniworldwidee）亲历，2026-08-12
    "dani_run":      "1万 → 7万",
    "dani_outcome":  "卖出即归零，无承接盘",
    "dani_quote":    "99% of all my trading is still GMGN",
    # claymore（@claymorepx）私信确认
    "claymore_rank": "FOMO 30 日榜第 20 名",
    "claymore_pnl":  "+$278,533.79",
    "claymore_fact": "仓位性质为 transferred（转入），主要交易在 GMGN 与 Robinhood",
    # 排行榜机制
    "leaderboard":   "持仓记录区分 transferred / bought，排行榜 PnL 不区分",
    # PF 的 UGC 明码标价，2026-08-11 Alon 官方 Discord @everyone
    "pf_ugc":        "$0.25/推荐 · $0.10/转发 · $0.05/评论",
}

# ── Arthur v8 新增：产品侧一手事实 ────────────────────────
#   来源为 v8 deck（2026-08-13）中标注为一手 / 产品侧核实的条目。
#   ⚠️ 凡标〔待核〕的，引用前必须先落实，见 counterplay 文档「待核」节。
V8 = {
    # 资金进出（v8 认定的产品债重心：债在进出，不在速度）
    "sell_floor":     "约 $2",          # SOL gas 从 $0.1 涨到 $0.95 后的最低卖出门槛
    "gas_bump":       "$0.1 → $0.95",
    "withdraw_only":  "仅 SOL / USDC 可提现，其他资产须导出私钥",
    "onramp_fail":    "Apple Pay / Cash App / 非美银行卡持续失败；德国用户看不到任何入金选项",
    "card_min":       "约 $10",         # 借记卡最低充值
    # 托管信任
    "tos_date":       "2026-08-02",
    "tos_risk":       "ToS 允许第三方以未加密方式传输私钥、可无通知封号",
    "scam_dates":     "2026-08-03 / 08-07",   # 假客服骗局，已有实际盗资事件
    # 速度机制〔产品侧 08-13 核实，非推断；婉云向产品与 Tylor 核实〕
    "relay_path":     "USDC 先到 relay，再分发到各链",
    "our_path":       "单链对单链",
    # 它改得动 vs 改不动
    "they_fix":       "已公开回应费率、给出 $0.10 floor 口径并预告 Solana 升级后继续降；同期上线 Clans 与 social perps",
    "they_cant":      "USDC 统一跨链＝速度天花板，改不动",
    # 我们自己的债（宣传前置）
    # ⚠️ 待核：v8 把「修推送延迟」列为产品线最高优先级，但未给测量来源，
    #    App PM 亦不认这个数。对比对象是 Dexscreener，不是 FOMO。先测再排期。
    "push_delay":     "6–20 min〔待核〕",
    # 渠道对照
    "pf_poach":       "约 $20K 签约 + 约 $30K/月，要求永久删除 FOMO 账号并签排他",
    # 榜单机制原话（Telegram，交易员自述）
    "leaderboard_q":  "The 24h anyone can jump to it — that's the secret sauce",
}

# ── 推送 / 信号 ─────────────────────────────────────────
PUSH = {
    "tiers":            "20 / 40 / 80",
    "gme_pushes":       "11",           # 07-23 单日对 GME
    "max_daily":        "23",
    "our_coverage":     "14 / 14",      # 07-23 影子测试
    "their_coverage":   "8 / 14",
    "our_earlier":      "6",            # 我们首触更早的币数
}

# ── 影响力放大（X 抓取，二手；FOMO 粉丝除注明外为推算）──
INFLUENCE = {
    "x_spread":     "10.7×",
    "fomo_spread":  "2.8×",
    "traders": [
        # (账号, X 粉丝, 倍数, FOMO 粉丝是否本人自报)
        ("@wwayfboss",    752, 27.0, False),
        ("@octoseaa",    2636,  5.1, False),
        ("@hdegrootvan", 7943,  2.9, True),
        ("@f4vel",       3055,  2.7, False),
        ("@thokani",     8073,  2.0, False),
    ],
}

# ── 供应商 ──────────────────────────────────────────────
VENDORS = {
    "bridge":   "Relay",
    "keys":     "Privy",
    "onramp":   "Crossmint",
    "offramp":  "Spritz",
    "perps":    "Hyperliquid + Trade[XYZ]",
    "routing":  "DFlow / Jupiter",
    "submit":   "Jito",
}

# ── 链上地址（一手抓包）─────────────────────────────────
ADDRESSES = {
    "fee_owner":    "R4rNJHaffSUotNmqSKNEfDcJE8A7zJUkaoM5Jkd7cYX",
    "fee_ata":      "HrTf9CzXR1dRH4Sof5QrpmGWwpwAf3qZzwCsEjQpXcSq",
    "bridge_prog":  "99vQwtBwYtrqqD9YSXbdum3KBdxPAVxYTaQ3cfnJSrN2",
    "sol_relayer":  "F7p3dFrjRTbtRp8FRF6qHLomXbKRBzpvBLjtQcfcgmNe",
    "relay_router": "0xb92fe925dc43a0ecde6c8b1a2709c170ec4fff4f",
    "rh_chain_id":  "4663",
}

# ── 文档矩阵（三层结构，互相引用时用这里的路径）──────────
#   URL 用 Artifact 绝对地址：三份发布后各自是独立 URL，
#   相对路径（fomo-brief.html）只在本地同目录有效，线上必然 404。
DOCS = {
    "brief": ("一页纸决策简报",
              "https://claude.ai/code/artifact/76b7997d-e74f-4e77-bb3e-66d986048bef",
              "结论 · 威胁分级 · P0/P1，一屏"),
    "loop":  ("增长闭环（诊断层）",
              "https://claude.ai/code/artifact/64861aa8-fe7c-4912-b01a-1ee52aae0087",
              "飞轮机制 · 铰链 · 漏损点 · 获客导图"),
    "full":  ("全面产品调研（参考层）",
              "https://claude.ai/code/artifact/0bf4ad28-129d-4594-83bf-7f5fa741271b",
              "资本 · 数据 · 技术拆解 · 费率 · 口碑 · 行动清单 · 附录"),
    "play":  ("产品侧应对：抄 · 打 · 建",
              "https://claude.ai/code/artifact/67b79931-8d26-49da-8c28-205966d1dd50",
              "并入 Arthur v8 的产品侧 · 四个咬合点 · 排期 · 待核"),
}


def all_values():
    """把所有标量事实摊平成 {名称: 值}，供 check-facts.py 校验。"""
    out = {}
    for group, d in (("CAPITAL", CAPITAL), ("SCALE", SCALE), ("REVENUE", REVENUE),
                     ("FEES", FEES), ("GMGN_FEES", GMGN_FEES), ("VOLUME", VOLUME), ("PUSH", PUSH),
                     ("VENDORS", VENDORS), ("ADDRESSES", ADDRESSES)):
        for k, v in d.items():
            out[f"{group}.{k}"] = v
    out["INFLUENCE.x_spread"] = INFLUENCE["x_spread"]
    out["INFLUENCE.fomo_spread"] = INFLUENCE["fomo_spread"]
    return out
