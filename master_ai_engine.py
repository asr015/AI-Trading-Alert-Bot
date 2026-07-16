# ==========================================
# TradingASR AI Pro v4.0
# File : master_ai_engine.py
# Part 1 / 5
# ==========================================

from market_bias_engine import market_bias_score

# Future Ready
try:
    from news_engine import news_score
except ImportError:

    def news_score(symbol):
        return 0, []

# ==========================================
# OPTION CHAIN CACHE
# ==========================================

_option_cache = None


def set_option_chain(option_data):

    global _option_cache

    _option_cache = option_data


# ==========================================
# CONFIDENCE ENGINE
# ==========================================

def calculate_confidence(score, reasons):

    confidence = 50

    # Score contribution
    confidence += min(abs(score) // 10, 30)

    # Confirmation contribution
    confidence += min(len(reasons) * 2, 20)

    confidence = max(50, min(99, int(confidence)))

    return f"{confidence}%"
    # ==========================================
# SCORE NORMALIZATION
# ==========================================

def normalize_score(score):

    if score > 500:
        return 500

    elif score < -500:
        return -500

    return int(score)


# ==========================================
# AI VERDICT ENGINE
# ==========================================

def generate_verdict(score):

    if score >= 420:

        return {
            "verdict": "🔥 ELITE BUY",
            "signal": "BUY"
        }

    elif score >= 300:

        return {
            "verdict": "🚀 STRONG BUY",
            "signal": "BUY"
        }

    elif score >= 180:

        return {
            "verdict": "🟢 BUY",
            "signal": "BUY"
        }

    elif score <= -420:

        return {
            "verdict": "💥 ELITE SELL",
            "signal": "SELL"
        }

    elif score <= -300:

        return {
            "verdict": "🔴 STRONG SELL",
            "signal": "SELL"
        }

    elif score <= -180:

        return {
            "verdict": "🟥 SELL",
            "signal": "SELL"
        }

    else:

        return {
            "verdict": "🟡 WAIT",
            "signal": "WAIT"
        }


# ==========================================
# REMOVE DUPLICATE REASONS
# ==========================================

def clean_reasons(reasons):

    cleaned = []

    for reason in reasons:

        if reason not in cleaned:
            cleaned.append(reason)

    return cleaned[:12]
