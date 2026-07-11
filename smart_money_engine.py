def smart_money_score(df):

    if len(df) < 21:
        return 0, []

    last = df.iloc[-1]
    prev = df.iloc[-2]

    score = 0
    reasons = []

    # Smart Volume Entry
    if last["Volume"] > prev["Volume"] * 1.8:
        score += 30
        reasons.append("🟢 Smart Volume")

    # Candle Body
    body = abs(last["Close"] - last["Open"])
    candle_range = last["High"] - last["Low"]

    # Avoid division/comparison on zero range candle
    if candle_range > 0:

        # Bullish Institutional Candle
        if body > candle_range * 0.60 and last["Close"] > last["Open"]:
            score += 25
            reasons.append("🏦 Institutional Buying")

        # Bearish Institutional Candle
        elif body > candle_range * 0.60 and last["Close"] < last["Open"]:
            score -= 25
            reasons.append("🏦 Institutional Selling")

    # Breakout
    breakout = df["High"].rolling(20).max().shift(1).iloc[-1]

    if last["Close"] > breakout:
        score += 35
        reasons.append("🚀 Breakout")

    # Breakdown
    breakdown = df["Low"].rolling(20).min().shift(1).iloc[-1]

    if last["Close"] < breakdown:
        score -= 35
        reasons.append("💥 Breakdown")

    return score, reasons
