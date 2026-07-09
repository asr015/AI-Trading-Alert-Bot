from indicator_engine import calculate_indicators
from smart_money_engine import smart_money_score
from liquidity_engine import liquidity_score
from structure_engine import structure_score
from order_block_engine import order_block_score


def calculate_score(data):

    df = calculate_indicators(data)

    if len(df) < 25:
        return {
            "score": 0,
            "reasons": ["⚠️ Not enough Data"]
        }

    last = df.iloc[-1]
    prev = df.iloc[-2]

    score = 0
    reasons = []

    # ===============================
    # BULLISH CONDITIONS
    # ===============================

    if last["EMA20"] > last["EMA50"]:
        score += 30
        reasons.append("✅ EMA20 > EMA50")

    if last["EMA50"] > last["EMA200"]:
        score += 20
        reasons.append("✅ Above EMA200")

    if last["RSI"] > 60:
        score += 30
        reasons.append("✅ Strong RSI")

    if last["MACD"] > last["Signal"]:
        score += 20
        reasons.append("✅ MACD Bullish")

    if last["Close"] > last["VWAP"]:
        score += 20
        reasons.append("✅ Above VWAP")

    if last["Close"] > last["Open"]:
        score += 20
        reasons.append("✅ Bullish Candle")

    if last["Volume"] > prev["Volume"]:
        score += 20
        reasons.append("✅ Volume Expansion")

    if last["RVOL"] > 1.5:
        score += 20
        reasons.append("✅ High RVOL")

    if last["EMA20"] > prev["EMA20"]:
        score += 20
        reasons.append("✅ EMA Rising")

    if (
        last["EMA20"] > last["EMA50"]
        and last["RSI"] > 55
        and last["Volume"] > prev["Volume"]
    ):
        score += 40
        reasons.append("🚀 Momentum Before Momentum")

    # ===============================
    # BEARISH CONDITIONS
    # ===============================

    if last["EMA20"] < last["EMA50"]:
        score -= 30
        reasons.append("🔴 EMA20 < EMA50")

    if last["EMA50"] < last["EMA200"]:
        score -= 20
        reasons.append("🔴 Below EMA200")

    if last["RSI"] < 40:
        score -= 30
        reasons.append("🔴 Weak RSI")

    if last["MACD"] < last["Signal"]:
        score -= 20
        reasons.append("🔴 MACD Bearish")

    if last["Close"] < last["VWAP"]:
        score -= 20
        reasons.append("🔴 Below VWAP")

    if last["Close"] < last["Open"]:
        score -= 20
        reasons.append("🔴 Bearish Candle")

    if (
        last["Volume"] > prev["Volume"]
        and last["Close"] < last["Open"]
    ):
        score -= 20
        reasons.append("🔴 Selling Pressure")

    if last["EMA20"] < prev["EMA20"]:
        score -= 20
        reasons.append("🔴 EMA Falling")

    if (
        last["EMA20"] < last["EMA50"]
        and last["RSI"] < 45
        and last["Volume"] > prev["Volume"]
    ):
        score -= 40
        reasons.append("💥 Bearish Momentum")

    # ===============================
    # SMART MONEY ENGINE
    # ===============================

    sm_score, sm_reasons = smart_money_score(df)
    score += sm_score
    reasons.extend(sm_reasons)

    # ===============================
    # LIQUIDITY ENGINE
    # ===============================

    liq_score, liq_reasons = liquidity_score(df)
    score += liq_score
    reasons.extend(liq_reasons)

    # ===============================
    # STRUCTURE ENGINE
    # ===============================

    structure_score_value, structure_reasons = structure_score(df)
    score += structure_score_value
    reasons.extend(structure_reasons)

    # ===============================
    # ORDER BLOCK ENGINE
    # ===============================

    ob_score, ob_reasons = order_block_score(df)
    score += ob_score
    reasons.extend(ob_reasons)

    # ===============================
    # FINAL RESULT
    # ===============================

    return {
        "score": score,
        "reasons": reasons
    }
