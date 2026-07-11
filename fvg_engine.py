def fvg_score(df):

    required_columns = [
        "High",
        "Low",
        "Close"
    ]

    score = 0
    reasons = []

    # Safety checks
    if df is None or len(df) < 3:
        return score, ["Not enough FVG data"]

    for col in required_columns:
        if col not in df.columns:
            return 0, [f"Missing column: {col}"]

    data = df.dropna(subset=required_columns)

    if len(data) < 3:
        return 0, ["Invalid candle data"]


    last = data.iloc[-1]
    prev = data.iloc[-2]
    prev2 = data.iloc[-3]


    # ==========================
    # Bullish Fair Value Gap
    # ==========================

    if prev["Low"] > prev2["High"]:

        score += 40
        reasons.append("🟢 Bullish FVG")

        # FVG remains supported
        if last["Close"] > prev["Low"]:
            score += 20
            reasons.append("✅ FVG Holding")


    # ==========================
    # Bearish Fair Value Gap
    # ==========================

    if prev["High"] < prev2["Low"]:

        score -= 40
        reasons.append("🔴 Bearish FVG")

        # FVG remains active
        if last["Close"] < prev["High"]:
            score -= 20
            reasons.append("✅ Bearish FVG Holding")


    # Score limit
    score = max(min(score, 100), -100)

    return score, reasons
