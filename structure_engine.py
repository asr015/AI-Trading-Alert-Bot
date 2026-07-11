def structure_score(df):

    required_columns = ["High", "Low", "Close"]

    # Safety checks
    if df is None or len(df) < 21:
        return 0, ["Not enough structure data"]

    for col in required_columns:
        if col not in df.columns:
            return 0, [f"Missing column: {col}"]

    data = df.dropna(subset=required_columns)

    if len(data) < 21:
        return 0, ["Invalid candle data"]

    last = data.iloc[-1]
    prev = data.iloc[-2]

    score = 0
    reasons = []

    # Previous 20 candle structure
    high20 = (
        data["High"]
        .rolling(20)
        .max()
        .shift(1)
        .iloc[-1]
    )

    low20 = (
        data["Low"]
        .rolling(20)
        .min()
        .shift(1)
        .iloc[-1]
    )

    # BOS Bullish
    if last["Close"] > high20:
        score += 40
        reasons.append("🚀 BOS Bullish")

    # BOS Bearish
    if last["Close"] < low20:
        score -= 40
        reasons.append("💥 BOS Bearish")


    # Higher High
    if last["High"] > prev["High"]:
        score += 10
        reasons.append("📈 Higher High")


    # Higher Low
    if last["Low"] > prev["Low"]:
        score += 10
        reasons.append("📈 Higher Low")


    # Lower High
    if last["High"] < prev["High"]:
        score -= 10
        reasons.append("📉 Lower High")


    # Lower Low
    if last["Low"] < prev["Low"]:
        score -= 10
        reasons.append("📉 Lower Low")


    # CHOCH Bullish
    if (
        last["Low"] > prev["Low"]
        and last["Close"] > prev["High"]
    ):
        score += 30
        reasons.append("🟢 CHOCH Bullish")


    # CHOCH Bearish
    if (
        last["High"] < prev["High"]
        and last["Close"] < prev["Low"]
    ):
        score -= 30
        reasons.append("🔴 CHOCH Bearish")


    # Limit score
    score = max(min(score, 100), -100)

    return score, reasons
