# ==========================================
# TradingASR AI Pro v4.0
# File : market_bias_engine.py
# Part 1 / 3
# ==========================================

from option_chain import analyze_option_chain
from market_breadth_engine import market_breadth
from sector_strength_engine import sector_strength
from index_engine import get_index_signal


def market_bias_score():

    score = 0

    reasons = []

    # ==========================================
    # Option Chain
    # ==========================================

    option = analyze_option_chain()

    pcr = option.get("PCR", "N/A")

    bias = option.get("MarketBias", "UNKNOWN")

    if isinstance(pcr, (int, float)):

        if pcr >= 1.20:

            score += 20

            reasons.append(
                f"🟢 PCR Bullish ({pcr})"
            )

        elif pcr <= 0.80:

            score -= 20

            reasons.append(
                f"🔴 PCR Bearish ({pcr})"
            )

    if bias == "BULLISH":

        score += 15

        reasons.append(
            "📈 Option Chain Bullish"
        )

    elif bias == "BEARISH":

        score -= 15

        reasons.append(
            "📉 Option Chain Bearish"
        )
