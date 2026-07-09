def liquidity_score(df):

    last = df.iloc[-1]
    prev = df.iloc[-2]

    score = 0
    reasons = []

    # Previous High Sweep
    if (
        last["High"] > prev["High"]
        and last["Close"] < prev["High"]
    ):
        score -= 35
        reasons.append("🎯 Liquidity Grab High")

    # Previous Low Sweep
    if (
        last["Low"] < prev["Low"]
        and last["Close"] > prev["Low"]
    ):
        score += 35
        reasons.append("🎯 Liquidity Grab Low")

    # Fake Breakout
    if (
        last["High"] > prev["High"]
        and last["Close"] < last["Open"]
    ):
        score -= 20
        reasons.append("❌ Fake Breakout")

    # Fake Breakdown
    if (
        last["Low"] < prev["Low"]
        and last["Close"] > last["Open"]
    ):
        score += 20
        reasons.append("✅ Fake Breakdown")

    return score, reasons
