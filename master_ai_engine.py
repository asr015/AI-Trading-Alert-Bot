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
