def generate_signal(score):

    if score >= 90:
        return {
            "signal": "🔥 HIGH MOMENTUM",
            "confidence": "90%"
        }

    elif score >= 80:
        return {
            "signal": "🟢 WATCHLIST",
            "confidence": "80%"
        }

    elif score >= 60:
        return {
            "signal": "🟡 WAIT",
            "confidence": "60%"
        }

    else:
        return {
            "signal": "🔴 NO TRADE",
            "confidence": "Low"
        }
