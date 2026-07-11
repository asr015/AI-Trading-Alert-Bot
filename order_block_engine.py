def order_block_score(df):

    required_columns = [
        "Open",
        "High",
        "Low",
        "Close"
    ]

    # Safety checks
    if df is None or len(df) < 2:
        return 0, ["Not enough candle data"]

    for col in required_columns:
        if col not in df.columns:
            return 0, [f"Missing column: {col}"]

    data = df.copy()

    data = data.dropna(subset=required_columns)

    if len(data) < 2:
        return 0, ["Invalid candle data"]

    last = data.iloc[-1]
    prev = data.iloc[-2]

    score = 0
    reasons = []

    # Bullish Order Block
    if (
        prev["Close"] < prev["Open"]
        and last["Close"] > prev["High"]
    ):
        score += 40
        reasons.append("🏦 Bullish Order Block")


    # Bearish Order Block
    if (
        prev["Close"] > prev["Open"]
        and last["Close"] < prev["Low"]
    ):
        score -= 40
        reasons.append("🏦 Bearish Order Block")


    # VWAP based zones
    if "VWAP" in data.columns:

        # Demand Zone
        if (
            last["Close"] > last["VWAP"]
            and last["Low"] > prev["Low"]
        ):
            score += 20
            reasons.append("🟢 Demand Zone")


        # Supply Zone
        if (
            last["Close"] < last["VWAP"]
            and last["High"] < prev["High"]
        ):
            score -= 20
            reasons.append("🔴 Supply Zone")


    # Score limit
    score = max(min(score, 100), -100)

    return score, reasons
