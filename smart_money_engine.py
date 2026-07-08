def smart_money_score(data):

    score = 0
    reasons = []

    if data.empty:
        return {
            "score": 0,
            "reasons": ["No Data"]
        }


    last = data.iloc[-1]

    avg_volume = data["Volume"].tail(20).mean()


    # Volume Expansion
    if last["Volume"] > avg_volume * 1.5:
        score += 30
        reasons.append("🟢 Smart Volume Entry")


    # Big Bullish Candle
    candle_size = abs(last["Close"] - last["Open"])

    avg_candle = (
        abs(data["Close"] - data["Open"])
        .tail(20)
        .mean()
    )


    if candle_size > avg_candle * 1.5 and last["Close"] > last["Open"]:
        score += 30
        reasons.append("🟢 Institutional Candle")


    # Breakout
    previous_high = data["High"].tail(20).max()

    if last["Close"] > previous_high:
        score += 40
        reasons.append("🚀 Breakout Detected")


    return {
        "score": score,
        "reasons": reasons
  }
