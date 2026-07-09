def analyze_setup(score, reasons):

    smart_money = any(
        "Smart" in r or
        "Momentum Before Momentum" in r or
        "Breakout" in r
        for r in reasons
    )

    # Confidence
    confidence = min(max(abs(score) // 2, 40), 95)

    # Final Decision

    if score >= 220:
        verdict = "🚀 STRONG BULLISH"

    elif score >= 150:
        verdict = "🟢 HIGH PROBABILITY BULLISH"

    elif score >= 80:
        verdict = "🟢 BULLISH"

    elif score <= -220:
        verdict = "💥 STRONG BEARISH"

    elif score <= -150:
        verdict = "🔴 HIGH PROBABILITY BEARISH"

    elif score <= -80:
        verdict = "🔴 BEARISH"

    else:
        verdict = "🟡 WAIT"

    # Upgrade if Smart Money is present
    if smart_money and score >= 150:
        verdict += "\n🧠 Smart Money Confirmed"

    if smart_money and score <= -150:
        verdict += "\n🧠 Smart Money Selling"

    return {
        "verdict": verdict,
        "confidence": f"{confidence}%"
    }
