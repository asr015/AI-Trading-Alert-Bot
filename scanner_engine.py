from indicator_engine import calculate_indicators

def calculate_score(data):

    if data.empty:
        return {
            "score": 0,
            "reasons": ["No Data"]
        }

    df = calculate_indicators(data)

    last = df.iloc[-1]
    prev = df.iloc[-2]

    score = 0
    reasons = []

    # EMA Trend
    if last["EMA20"] > last["EMA50"]:
        score += 30
        reasons.append("✅ EMA Bullish")

    # RSI
    if last["RSI"] > 60:
        score += 30
        reasons.append("✅ RSI Strong")

    # Price Above EMA20
    if last["Close"] > last["EMA20"]:
        score += 20
        reasons.append("✅ Above EMA20")

    # Bullish Candle
    if last["Close"] > last["Open"]:
        score += 20
        reasons.append("✅ Bullish Candle")

    # EMA Rising
    if last["EMA20"] > prev["EMA20"]:
        score += 30
        reasons.append("✅ EMA Rising")

    # Volume
    avg_volume = df["Volume"].tail(20).mean()

    if last["Volume"] > avg_volume:
        score += 40
        reasons.append("✅ Volume Expansion")

    return {
        "score": score,
        "reasons": reasons
    }
