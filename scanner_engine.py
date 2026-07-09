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
            "reasons": ["⚠️ Not enough Data"],
            "entry": 0,
            "sl": 0,
            "target1": 0,
            "target2": 0
        }

    last = df.iloc[-1]
    prev = df.iloc[-2]

    score = 0
    reasons = []

    # ==========================
    # BULLISH
    # ==========================

    if last["EMA20"] > last["EMA50"]:
        score += 30
        reasons.append("✅ EMA Bullish")

    if last["EMA50"] > last["EMA200"]:
        score += 20
        reasons.append("✅ Above EMA200")

    if last["RSI"] > 60:
        score += 30
        reasons.append("✅ RSI Strong")

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

    # ==========================
    # BEARISH
    # ==========================

    if last["EMA20"] < last["EMA50"]:
        score -= 30
        reasons.append("🔴 EMA Bearish")

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

    if last["Volume"] > prev["Volume"] and last["Close"] < last["Open"]:
        score -= 20
        reasons.append("🔴 Selling Pressure")

    if last["EMA20"] < prev["EMA20"]:
        score -= 20
        reasons.append("🔴 EMA Falling")

    # ==========================
    # SMART MONEY
    # ==========================

    sm_score, sm_reason = smart_money_score(df)

    score += sm_score
    reasons.extend(sm_reason)

    # ==========================
    # LIQUIDITY
    # ==========================

    liq_score, liq_reason = liquidity_score(df)

    score += liq_score
    reasons.extend(liq_reason)

    # ==========================
    # STRUCTURE
    # ==========================

    st_score, st_reason = structure_score(df)

    score += st_score
    reasons.extend(st_reason)

    # ==========================
    # ORDER BLOCK
    # ==========================

    ob_score, ob_reason = order_block_score(df)

    score += ob_score
    reasons.extend(ob_reason)

    # ==========================
    # ENTRY / SL / TARGET
    # ==========================

    if score >= 0:

        entry = round(last["High"] + 0.10, 2)

        sl = round(last["Low"], 2)

        risk = entry - sl

        target1 = round(entry + risk * 2, 2)

        target2 = round(entry + risk * 3, 2)

    else:

        entry = round(last["Low"] - 0.10, 2)

        sl = round(last["High"], 2)

        risk = sl - entry

        target1 = round(entry - risk * 2, 2)

        target2 = round(entry - risk * 3, 2)

    return {

        "score": score,

        "reasons": reasons,

        "entry": entry,

        "sl": sl,

        "target1": target1,

        "target2": target2

    }
