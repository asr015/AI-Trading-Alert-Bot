# ==========================================
# TradingASR AI Pro v2.2
# File : ai_decision_engine.py
# ==========================================

def analyze_setup(score, reasons):

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

    confidence = 60

    if abs(score) >= 280:
        confidence = 98
    elif abs(score) >= 250:
        confidence = 96
    elif abs(score) >= 220:
        confidence = 94
    elif abs(score) >= 190:
        confidence = 91
    elif abs(score) >= 160:
        confidence = 87
    elif abs(score) >= 130:
        confidence = 82
    elif abs(score) >= 100:
        confidence = 75

    # Extra confidence from multiple confirmations
    if bull >= 4 and score > 0:
        confidence = min(confidence + 2, 99)

    if bear >= 4 and score < 0:
        confidence = min(confidence + 2, 99)

    if score >= 250:
        verdict = "🚀 STRONG BUY"

    elif score >= 180:
        verdict = "🟢 BUY"

    elif score <= -250:
        verdict = "💥 STRONG SELL"

    elif score <= -180:
        verdict = "🔴 SELL"

    else:
        verdict = "🟡 WAIT"

    return {
        "verdict": verdict,
        "confidence": f"{confidence}%"
    }
