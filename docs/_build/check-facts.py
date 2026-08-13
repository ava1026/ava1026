# -*- coding: utf-8 -*-
"""
校验手写文档与单一事实源是否一致。

生成型文档（brief / growth-loop）在构建时直接注入 fomo_facts，不会漂移；
手写型文档（主报告 md / html）靠本脚本兜底。

    python3 docs/_build/check-facts.py

退出码 0 = 一致，1 = 发现漂移。
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fomo_facts as F  # noqa: E402

DOCS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HANDWRITTEN = [
    "fomo-product-research-2026-08.md",
    "fomo-product-research-2026-08.html",
]

# 漂移规则：(说明, 正则含一个捕获组, 期望值)
# 只收录能可靠正则化、且一旦写错影响判断的高风险数字。
RULES = [
    ("小额档实际费率", r"实收 ([\d.]+)%",                        "47.5"),
    ("小额档固定费",   r"固定 ([\d.]+) USDC",                     "0.95"),
    ("每笔平均平台费", r"≈?\s?\$([\d.]+)\s?/\s?笔",               "0.76"),
    ("推荐渗透率",     r"约(?:三成|\s?([\d.]+)%)\s?手续费来自",     "29"),
    ("Solana 占比",    r"([\d.]+)% (?:来自|收入来自) Solana",      "98.5"),
    # 周收入 ATH 不用正则校验：文档里保留 $1.39M / $1.57M 的历史序列是正确的，
    # 只要求当前值必须出现（见 MUST_APPEAR）。
]

# 必须出现的关键值（缺失说明文档被删改过头）
MUST_APPEAR = {
    "收费钱包 ATA":   F.ADDRESSES["fee_ata"],
    "跨链桥程序":     F.ADDRESSES["bridge_prog"],
    "Relay 路由合约": F.ADDRESSES["relay_router"],
    "估值":           F.CAPITAL["valuation"],
    "用户数":         F.SCALE["users"],
    "当前周收入 ATH": F.REVENUE["weekly_ath"],
    "每笔平均费":     F.REVENUE["fee_per_trade"],
}


def check(path):
    problems, notes = [], []
    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    for label, pattern, expected in RULES:
        if expected is None:
            continue
        found = [m for m in re.findall(pattern, text) if m]
        if not found:
            continue  # 该文档没提这个数字，不算问题
        for v in set(found):
            if v != expected:
                problems.append(f"  ✗ {label}：文档写 {v}，事实源是 {expected}")

    for label, value in MUST_APPEAR.items():
        if value not in text:
            notes.append(f"  · 未出现：{label}（{value}）")

    return problems, notes


def main():
    print(f"事实源 AS_OF = {F.AS_OF}　共 {len(F.all_values())} 条标量事实\n")
    failed = False
    for name in HANDWRITTEN:
        path = os.path.join(DOCS_DIR, name)
        if not os.path.exists(path):
            print(f"{name}\n  ✗ 文件不存在")
            failed = True
            continue
        problems, notes = check(path)
        status = "✗ 发现漂移" if problems else "✓ 一致"
        print(f"{name}\n  {status}")
        for p in problems:
            print(p)
            failed = True
        for n in notes:
            print(n)
        print()

    print("发现漂移，请以 fomo_facts.py 为准修正文档。" if failed
          else "全部一致。")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
