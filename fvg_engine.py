def fvg_score(df):

    score = 0
    reasons = []

    if len(df) < 3:
        return score, reasons

    last = df.iloc[-1]
    prev = df.iloc[-2]
    prev2 = df.iloc[-3]

    # ==========================
    # Bullish Fair Value Gap
    # ==========================

    if prev["Low"] > prev2["High"]:

        score += 40
        reasons.append("🟢 Bullish FVG")

        if last["Close"] > prev["Low"]:
            score += 20
            reasons.append("✅ FVG Holding")

    # ==========================
    # Bearish Fair Value Gap
    # ==========================

    if prev["High"] < prev2["Low"]:

        score -= 40
        reasons.append("🔴 Bearish FVG")

        if last["Close"] < prev["High"]:
            score -= 20
            reasons.append("✅ Bearish FVG Holding")

    return score, reasons
