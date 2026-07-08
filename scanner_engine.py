from indicator_engine import calculate_indicators
from smart_money_engine import smart_money_score


def calculate_score(data):

    if data.empty:
        return {
            "score": 0,
            "reasons": ["No Data"]
        }


    df = calculate_indicators(data)

    last = df.iloc[-1]
    prev = df.iloc[-2]


    technical_score = 0
    reasons = []


    # EMA Trend
    if last["EMA20"] > last["EMA50"]:
        technical_score += 30
        reasons.append("✅ EMA Bullish")


    # RSI Strength
    if last["RSI"] > 60:
        technical_score += 30
        reasons.append("✅ RSI Strong")


    # Price Above EMA20
    if last["Close"] > last["EMA20"]:
        technical_score += 20
        reasons.append("✅ Above EMA20")


    # Bullish Candle
    if last["Close"] > last["Open"]:
        technical_score += 20
        reasons.append("✅ Bullish Candle")


    # EMA Rising
    if last["EMA20"] > prev["EMA20"]:
        technical_score += 30
        reasons.append("✅ EMA Rising")


    # Volume
    avg_volume = df["Volume"].tail(20).mean()

    if last["Volume"] > avg_volume:
        technical_score += 40
        reasons.append("✅ Volume Expansion")


    # Smart Money Check
    smart_money = smart_money_score(data)

    final_score = technical_score + smart_money["score"]


    reasons.extend(
        smart_money["reasons"]
    )


    return {
        "score": final_score,
        "reasons": reasons
    }
