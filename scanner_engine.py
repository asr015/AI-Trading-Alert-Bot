from smart_money_engine import smart_money_score
from indicator_engine import calculate_indicators

def calculate_score(data):

    df = calculate_indicators(data)

    last = df.iloc[-1]
    prev = df.iloc[-2]

    score = 0
    reasons = []

    # ==========================
    # BULLISH CONDITIONS
    # ==========================

    if last["EMA20"] > last["EMA50"]:
        score += 30
        reasons.append("✅ Above EMA20")

    if last["RSI"] > 60:
        score += 30
        reasons.append("✅ Strong RSI")

    if last["Close"] > last["Open"]:
        score += 20
        reasons.append("✅ Bullish Candle")

    if last["Volume"] > prev["Volume"]:
        score += 20
        reasons.append("✅ Volume Expansion")

    if last["EMA20"] > prev["EMA20"]:
        score += 20
        reasons.append("✅ EMA Rising")

    # Smart Volume Entry
    if (
        last["Volume"] > prev["Volume"] * 1.5
        and last["Close"] > last["Open"]
    ):
        score += 50
        reasons.append("🟢 Smart Volume Entry")

    # Momentum Before Momentum
    if (
        last["EMA20"] > last["EMA50"]
        and last["RSI"] > 55
        and last["Volume"] > prev["Volume"]
    ):
        score += 40
        reasons.append("🚀 Momentum Before Momentum")

    # ==========================
    # BEARISH CONDITIONS
    # ==========================

    if last["EMA20"] < last["EMA50"]:
        score -= 30
        reasons.append("🔴 Below EMA50")

    if last["RSI"] < 40:
        score -= 30
        reasons.append("🔴 Weak RSI")

    if last["Close"] < last["Open"]:
        score -= 20
        reasons.append("🔴 Bearish Candle")

    if last["Volume"] > prev["Volume"] and last["Close"] < last["Open"]:
        score -= 20
        reasons.append("🔴 Selling Pressure")

    if last["EMA20"] < prev["EMA20"]:
        score -= 20
        reasons.append("🔴 EMA Falling")

    # Smart Money Exit
    if (
        last["Volume"] > prev["Volume"] * 1.5
        and last["Close"] < last["Open"]
    ):
        score -= 50
        reasons.append("🔴 Smart Money Exit")

    # Bearish Momentum
    if (
        last["EMA20"] < last["EMA50"]
        and last["RSI"] < 45
        and last["Volume"] > prev["Volume"]
    ):
        score -= 40
        reasons.append("💥 Bearish Momentum")

   sm_score, sm_reason = smart_money_score(df)

score += sm_score

reasons.extend(sm_reason) 
    return {
        "score": score,
        "reasons": reasons
    }
