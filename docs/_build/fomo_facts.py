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
DOCS = {
    "brief": ("一页纸决策简报", "fomo-brief.html",
              "结论 · 威胁分级 · P0/P1，一屏"),
    "loop":  ("增长闭环（诊断层）", "fomo-growth-loop.html",
              "飞轮机制 · 铰链 · 漏损点 · 获客导图"),
    "full":  ("全面产品调研（参考层）", "fomo-product-research-2026-08.html",
              "资本 · 数据 · 技术拆解 · 费率 · 口碑 · 行动清单 · 附录"),
}


def all_values():
    """把所有标量事实摊平成 {名称: 值}，供 check-facts.py 校验。"""
    out = {}
    for group, d in (("CAPITAL", CAPITAL), ("SCALE", SCALE), ("REVENUE", REVENUE),
                     ("FEES", FEES), ("GMGN_FEES", GMGN_FEES), ("PUSH", PUSH),
                     ("VENDORS", VENDORS), ("ADDRESSES", ADDRESSES)):
        for k, v in d.items():
            out[f"{group}.{k}"] = v
    out["INFLUENCE.x_spread"] = INFLUENCE["x_spread"]
    out["INFLUENCE.fomo_spread"] = INFLUENCE["fomo_spread"]
    return out
