def liquidity_score(df):

    # Safety checks
    required_columns = ["High", "Low", "Open", "Close"]

    if df is None or len(df) < 2:
        return 0, ["Not enough data"]

    for col in required_columns:
        if col not in df.columns:
            return 0, [f"Missing column: {col}"]

    # Remove incomplete rows
    data = df.dropna(subset=required_columns)

    if len(data) < 2:
        return 0, ["Invalid candle data"]

    last = data.iloc[-1]
    prev = data.iloc[-2]

    score = 0
    reasons = []

    # Previous High Liquidity Sweep
    if (
        last["High"] > prev["High"]
        and last["Close"] < prev["High"]
    ):
        score -= 35
        reasons.append("🎯 Liquidity Grab High")

    # Previous Low Liquidity Sweep
    if (
        last["Low"] < prev["Low"]
        and last["Close"] > prev["Low"]
    ):
        score += 35
        reasons.append("🎯 Liquidity Grab Low")

    # Fake Breakout Detection
    if (
        last["High"] > prev["High"]
        and last["Close"] < last["Open"]
    ):
        score -= 20
        reasons.append("❌ Fake Breakout")

    # Fake Breakdown Detection
    if (
        last["Low"] < prev["Low"]
        and last["Close"] > last["Open"]
    ):
        score += 20
        reasons.append("✅ Fake Breakdown")

    # Keep score within limits
    score = max(min(score, 100), -100)

    return score, reasons
