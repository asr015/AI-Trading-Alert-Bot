# ==========================================
# TradingASR AI Pro v2.0
# File : market_bias_engine.py
# ==========================================

from config import BULLISH_BIAS, BEARISH_BIAS


def get_market_bias(bullish, bearish):

    total = bullish + bearish

    if total == 0:
        return {
            "bias": "🟡 Sideways",
            "strength": "0%"
        }

    bullish_pct = round((bullish / total) * 100)
    bearish_pct = 100 - bullish_pct

    if bullish_pct >= 60:
        return {
            "bias": "🟢 Bullish",
            "strength": f"{bullish_pct}%"
        }

    elif bearish_pct >= 60:
        return {
            "bias": "🔴 Bearish",
            "strength": f"{bearish_pct}%"
        }

    return {
        "bias": "🟡 Sideways",
        "strength": "50%"
    }


def market_bias_score():

    """
    Placeholder function for AI Master Engine.

    Future:
    This function can calculate market bias using
    NIFTY, BANKNIFTY, Advance/Decline,
    Sector Strength, VIX, etc.
    """

    return 0, []
