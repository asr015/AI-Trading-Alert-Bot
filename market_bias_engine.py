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
            # ==========================================
    # Market Breadth
    # ==========================================

    breadth = market_breadth()

    breadth_score = breadth.get("score", 0)

    score += breadth_score

    reasons.extend(
        breadth.get("reasons", [])
    )

    # ==========================================
    # Sector Strength
    # ==========================================

    sectors = sector_strength()

    sector_score = sectors.get("score", 0)

    score += sector_score

    reasons.extend(
        sectors.get("reasons", [])
    )

    # ==========================================
    # Index Trend
    # ==========================================

    index = get_index_signal()

    verdict = index.get(
        "signal",
        "WAIT"
    )

    confidence = index.get(
        "confidence",
        "0%"
    )

    if "BUY" in verdict:

        score += 35

        reasons.append(
            f"📈 Index Bullish ({confidence})"
        )

    elif "SELL" in verdict:

        score -= 35

        reasons.append(
            f"📉 Index Bearish ({confidence})"
        )

    else:

        reasons.append(
            "⚪ Index Neutral"
        )
            # ==========================================
    # SCORE LIMIT
    # ==========================================

    if score > 100:
        score = 100

    elif score < -100:
        score = -100

    # ==========================================
    # FINAL MARKET BIAS
    # ==========================================

    if score >= 70:

        market = "🟢 STRONG BULLISH"

    elif score >= 35:

        market = "🟢 BULLISH"

    elif score <= -70:

        market = "🔴 STRONG BEARISH"

    elif score <= -35:

        market = "🔴 BEARISH"

    else:

        market = "🟡 SIDEWAYS"

    # ==========================================
    # REMOVE DUPLICATE REASONS
    # ==========================================

    reasons = list(dict.fromkeys(reasons))

    # Keep only most important reasons
    reasons = reasons[:10]

    # ==========================================
    # FINAL RESULT
    # ==========================================

    return {

        "score": score,

        "market": market,

        "reasons": reasons,

        "option_chain": option,

        "breadth": breadth,

        "sector_strength": sectors,

        "index": index

        }
