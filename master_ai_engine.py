from market_bias_engine import market_bias_score

_option_cache = None


def set_option_chain(option_data):
    global _option_cache
    _option_cache = option_data


def final_ai_score(symbol, score):

    reasons = []

    # ==========================
    # Market Bias
    # ==========================

    bias_score, bias_reason = market_bias_score()

    score += bias_score
    reasons.extend(bias_reason)

    # ==========================
    # Cached Option Chain
    # ==========================

    global _option_cache

    if _option_cache:

        pcr = _option_cache.get("PCR", "N/A")

        if pcr != "N/A":

            if pcr >= 1.20:
                score += 20
                reasons.append("🟢 Bullish PCR")

            elif pcr <= 0.80:
                score -= 20
                reasons.append("🔴 Bearish PCR")

    # ==========================
    # Final Decision
    # ==========================

    if score >= 250:
        verdict = "🚀 STRONG BUY"
        confidence = "98%"

    elif score >= 180:
        verdict = "🟢 BUY"
        confidence = "90%"

    elif score <= -250:
        verdict = "💥 STRONG SELL"
        confidence = "98%"

    elif score <= -180:
        verdict = "🔴 SELL"
        confidence = "90%"

    else:
        verdict = "🟡 WAIT"
        confidence = "60%"

    return {
        "score": score,
        "verdict": verdict,
        "confidence": confidence,
        "reasons": reasons
    }
