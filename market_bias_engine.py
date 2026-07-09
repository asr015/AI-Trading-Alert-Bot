def get_market_bias(bullish, bearish):

    total = bullish + bearish

    if total == 0:
        return {
            "bias": "🟡 Sideways",
            "strength": "0%"
        }

    bullish_pct = round((bullish / total) * 100)
    bearish_pct = 100 - bullish_pct

    if bullish_pct >= 60:
        return {
            "bias": "🟢 Bullish",
            "strength": f"{bullish_pct}%"
        }

    elif bearish_pct >= 60:
        return {
            "bias": "🔴 Bearish",
            "strength": f"{bearish_pct}%"
        }

    return {
        "bias": "🟡 Sideways",
        "strength": "50%"
    }
