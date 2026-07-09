def smart_money_score(df):

    last = df.iloc[-1]
    prev = df.iloc[-2]

    score = 0
    reasons = []

    # Smart Volume Entry
    if last["Volume"] > prev["Volume"] * 1.8:
        score += 30
        reasons.append("🟢 Smart Volume")

    # Bullish Institutional Candle
    body = abs(last["Close"] - last["Open"])

    if body > (last["High"] - last["Low"]) * 0.60:
        if last["Close"] > last["Open"]:
            score += 25
            reasons.append("🏦 Institutional Buying")

    # Bearish Institutional Candle
    if body > (last["High"] - last["Low"]) * 0.60:
        if last["Close"] < last["Open"]:
            score -= 25
            reasons.append("🏦 Institutional Selling")

    # Breakout
    if last["Close"] > df["High"].rolling(20).max().shift(1).iloc[-1]:
        score += 35
        reasons.append("🚀 Breakout")

    # Breakdown
    if last["Close"] < df["Low"].rolling(20).min().shift(1).iloc[-1]:
        score -= 35
        reasons.append("💥 Breakdown")

    return score, reasons
