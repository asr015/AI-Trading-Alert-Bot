def generate_signal(score):

    # Safety check
    if score is None:
        return {
            "signal": "🔴 NO TRADE",
            "confidence": "Low"
        }

    try:
        score = float(score)

    except (ValueError, TypeError):
        return {
            "signal": "🔴 INVALID SCORE",
            "confidence": "Low"
        }


    # Bullish signals
    if score >= 90:
        return {
            "signal": "🔥 HIGH MOMENTUM BUY",
            "confidence": "90%"
        }


    elif score >= 80:
        return {
            "signal": "🟢 WATCHLIST BUY",
            "confidence": "80%"
        }


    elif score >= 60:
        return {
            "signal": "🟡 WAIT",
            "confidence": "60%"
        }


    # Bearish signals
    elif score <= -90:
        return {
            "signal": "🔥 HIGH MOMENTUM SELL",
            "confidence": "90%"
        }


    elif score <= -80:
        return {
            "signal": "🔴 WATCHLIST SELL",
            "confidence": "80%"
        }


    elif score <= -60:
        return {
            "signal": "🟠 WAIT SELL",
            "confidence": "60%"
        }


    else:
        return {
            "signal": "⚪ NO TRADE",
            "confidence": "Low"
        }
