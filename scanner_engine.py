from indicator_engine import calculate_indicators

def calculate_score(data):

    df = calculate_indicators(data)

    score = 0

    last = df.iloc[-1]

    if last["EMA20"] > last["EMA50"]:
        score += 30

    if last["RSI"] > 60:
        score += 30

    return score
