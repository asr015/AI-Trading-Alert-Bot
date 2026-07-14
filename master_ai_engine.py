# ==========================================
# TradingASR AI Pro v2.2
# File : master_ai_engine.py
# ==========================================

from market_bias_engine import market_bias_score

_option_cache = None


def set_option_chain(option_data):
    global _option_cache
    _option_cache = option_data


def final_ai_score(symbol, score):

    reasons = []

    # ======================================
    # Market Bias
    # ======================================

    bias_score, bias_reason = market_bias_score()

    score += bias_score
    reasons.extend(bias_reason)

    # ======================================
    # Option Chain (Optional Confirmation)
    # ======================================

    global _option_cache

    if _option_cache:

        pcr = _option_cache.get("PCR", "N/A")

        if isinstance(pcr, (int, float)):

            if pcr >= 1.20:
                score += 20
                reasons.append("🟢 Bullish PCR")

            elif pcr <= 0.80:
                score -= 20
                reasons.append("🔴 Bearish PCR")

    # ======================================
    # Confidence Calculation
    # ======================================

    abs_score = abs(score)

    if abs_score >= 280:
        confidence = "98%"

    elif abs_score >= 250:
        confidence = "96%"

    elif abs_score >= 220:
        confidence = "94%"

    elif abs_score >= 190:
        confidence = "91%"

    elif abs_score >= 160:
        confidence = "87%"

    elif abs_score >= 130:
        confidence = "82%"

    elif abs_score >= 100:
        confidence = "75%"

    else:
        confidence = "65%"

    # ======================================
    # Final Verdict
    # ======================================

    if score >= 250:
        verdict = "🚀 STRONG BUY"

    elif score >= 180:
        verdict = "🟢 BUY"

    elif score <= -250:
        verdict = "💥 STRONG SELL"

    elif score <= -180:
        verdict = "🔴 SELL"

    else:
        verdict = "🟡 WAIT"

    return {
        "score": score,
        "verdict": verdict,
        "confidence": confidence,
        "reasons": reasons
    }
