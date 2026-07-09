def analyze_setup(score, reasons):

    confidence = 40

    if score >= 220:
        confidence = 98

    elif score >= 200:
        confidence = 95

    elif score >= 180:
        confidence = 90

    elif score >= 150:
        confidence = 82

    elif score >= 100:
        confidence = 65

    elif score <= -220:
        confidence = 98

    elif score <= -200:
        confidence = 95

    elif score <= -180:
        confidence = 90

    elif score <= -150:
        confidence = 82

    bullish = [
        "Smart Money",
        "Liquidity",
        "Order Block",
        "Breakout",
        "BOS",
        "FVG"
    ]

    bearish = [
        "Smart Money Exit",
        "Supply",
        "CHOCH",
        "Bearish Momentum",
        "Distribution"
    ]

    bull = sum(any(x in r for x in bullish) for r in reasons)
    bear = sum(any(x in r for x in bearish) for r in reasons)

    if score >= 180:
        verdict = "🔥 HIGH PROBABILITY BUY"

    elif score >= 150:
        verdict = "🟢 BUY"

    elif score <= -180:
        verdict = "🔥 HIGH PROBABILITY SELL"

    elif score <= -150:
        verdict = "🔴 SELL"

    else:
        verdict = "🟡 WAIT"

    return {
        "verdict": verdict,
        "confidence": f"{confidence}%"
    }
