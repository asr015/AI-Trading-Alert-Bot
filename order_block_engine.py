def order_block_score(df):

    last = df.iloc[-1]
    prev = df.iloc[-2]

    score = 0
    reasons = []

    # Bullish Order Block
    if (
        prev["Close"] < prev["Open"] and
        last["Close"] > prev["High"]
    ):
        score += 40
        reasons.append("🏦 Bullish Order Block")

    # Bearish Order Block
    if (
        prev["Close"] > prev["Open"] and
        last["Close"] < prev["Low"]
    ):
        score -= 40
        reasons.append("🏦 Bearish Order Block")

    # Demand Zone
    if (
        last["Close"] > last["VWAP"] and
        last["Low"] > prev["Low"]
    ):
        score += 20
        reasons.append("🟢 Demand Zone")

    # Supply Zone
    if (
        last["Close"] < last["VWAP"] and
        last["High"] < prev["High"]
    ):
        score -= 20
        reasons.append("🔴 Supply Zone")

    return score, reasons
