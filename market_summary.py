# ==========================================
# TradingASR AI Pro v2.2
# File : market_summary.py
# ==========================================

def create_summary(results):

    total = len(results)

    bullish = 0
    bearish = 0
    neutral = 0

    for stock in results:

        score = stock.get("score", 0)

        if score >= 180:
            bullish += 1

        elif score <= -180:
            bearish += 1

        else:
            neutral += 1

    return {
        "total": total,
        "bullish": bullish,
        "bearish": bearish,
        "neutral": neutral
    }
