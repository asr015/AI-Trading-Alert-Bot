def create_summary(results):

    total = len(results)

    bullish = 0
    bearish = 0
    neutral = 0

    for stock in results:

        score = stock["score"]

        if score >= 120:
            bullish += 1

        elif score < 60:
            bearish += 1

        else:
            neutral += 1

    return {
        "total": total,
        "bullish": bullish,
        "bearish": bearish,
        "neutral": neutral
    }
