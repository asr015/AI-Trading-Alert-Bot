def structure_score(df):

    last = df.iloc[-1]

    score = 0
    reasons = []

    # Last 20 candles
    high20 = df["High"].rolling(20).max().shift(1).iloc[-1]
    low20 = df["Low"].rolling(20).min().shift(1).iloc[-1]

    # Break of Structure (Bullish)
    if last["Close"] > high20:
        score += 40
        reasons.append("🚀 BOS Bullish")

    # Break of Structure (Bearish)
    if last["Close"] < low20:
        score -= 40
        reasons.append("💥 BOS Bearish")

    # Higher High
    if last["High"] > df.iloc[-2]["High"]:
        score += 10
        reasons.append("📈 Higher High")

    # Higher Low
    if last["Low"] > df.iloc[-2]["Low"]:
        score += 10
        reasons.append("📈 Higher Low")

    # Lower High
    if last["High"] < df.iloc[-2]["High"]:
        score -= 10
        reasons.append("📉 Lower High")

    # Lower Low
    if last["Low"] < df.iloc[-2]["Low"]:
        score -= 10
        reasons.append("📉 Lower Low")

    # CHOCH Bullish
    if (
        last["Low"] > df.iloc[-2]["Low"]
        and last["Close"] > df.iloc[-2]["High"]
    ):
        score += 30
        reasons.append("🟢 CHOCH Bullish")

    # CHOCH Bearish
    if (
        last["High"] < df.iloc[-2]["High"]
        and last["Close"] < df.iloc[-2]["Low"]
    ):
        score -= 30
        reasons.append("🔴 CHOCH Bearish")

    return score, reasons
