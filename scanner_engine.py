from indicator_engine import calculate_indicators

def calculate_score(data):

    if data.empty:
        return 0

    df = calculate_indicators(data)

    last = df.iloc[-1]

    score = 0

    # Trend
    if last["EMA20"] > last["EMA50"]:
        score += 30

    # RSI
    if last["RSI"] > 60:
        score += 30

    # Price Above EMA20
    if last["Close"] > last["EMA20"]:
        score += 20

    # Bullish Candle
    if last["Close"] > last["Open"]:
        score += 20

    return score
