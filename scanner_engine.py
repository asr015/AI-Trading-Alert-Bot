# ==========================================
# TradingASR AI Pro v2.0
# File : scanner_engine.py
# Part 1 / 2
# ==========================================

from config import *

from indicator_engine import calculate_indicators
from smart_money_engine import smart_money_score
from liquidity_engine import liquidity_score
from structure_engine import structure_score
from order_block_engine import order_block_score
from fvg_engine import fvg_score
from news_engine import news_score
from risk_engine import calculate_trade


def calculate_score(data):

    df = calculate_indicators(data)

    if df is None or len(df) < 25:

        return {
            "score": 0,
            "reasons": [
                "⚠️ Not enough historical data"
            ],
            "entry": 0,
            "sl": 0,
            "target1": 0,
            "target2": 0
        }

    last = df.iloc[-1]
    prev = df.iloc[-2]

    score = 0
    reasons = []

    # ==========================================
    # EMA
    # ==========================================

    if last["EMA20"] > last["EMA50"]:
        score += EMA_BULLISH
        reasons.append("✅ EMA20 > EMA50")
    else:
        score += EMA_BEARISH
        reasons.append("🔴 EMA20 < EMA50")

    if last["EMA50"] > last["EMA200"]:
        score += EMA200_BULLISH
        reasons.append("✅ Above EMA200")
    else:
        score += EMA200_BEARISH
        reasons.append("🔴 Below EMA200")

    # ==========================================
    # RSI
    # ==========================================

    if last["RSI"] >= 60:
        score += RSI_BULLISH
        reasons.append("✅ Strong RSI")

    elif last["RSI"] <= 40:
        score += RSI_BEARISH
        reasons.append("🔴 Weak RSI")

    # ==========================================
    # MACD
    # ==========================================

    if last["MACD"] > last["Signal"]:
        score += MACD_BULLISH
        reasons.append("✅ MACD Bullish")
    else:
        score += MACD_BEARISH
        reasons.append("🔴 MACD Bearish")

    # ==========================================
    # VWAP
    # ==========================================

    if last["Close"] > last["VWAP"]:
        score += VWAP_BULLISH
        reasons.append("✅ Above VWAP")
    else:
        score += VWAP_BEARISH
        reasons.append("🔴 Below VWAP")

    # ==========================================
    # Candle
    # ==========================================

    if last["Close"] > last["Open"]:
        score += CANDLE_BULLISH
        reasons.append("✅ Bullish Candle")
    else:
        score += CANDLE_BEARISH
        reasons.append("🔴 Bearish Candle")

    # ==========================================
    # Volume
    # ==========================================

    if last["Volume"] > prev["Volume"]:
        score += VOLUME_BULLISH
        reasons.append("✅ Volume Expansion")

    if last["RVOL"] >= 1.5:
        score += RVOL_BULLISH
        reasons.append("✅ High Relative Volume")

    # ==========================================
    # EMA Slope
    # ==========================================

    if last["EMA20"] > prev["EMA20"]:
        score += EMA_RISING
        reasons.append("✅ EMA Rising")
    else:
        score += EMA_FALLING
        reasons.append("🔴 EMA Falling")

    # ==========================================
    # Momentum Before Momentum
    # ==========================================

    if (
        last["EMA20"] > last["EMA50"]
        and last["RSI"] > 55
        and last["RVOL"] > 1.5
        and last["Volume"] > prev["Volume"]
    ):
        score += MOMENTUM
        reasons.append("🚀 Momentum Before Momentum")

    # ==========================================
    # Smart Money Engine
    # ==========================================

    sm_score, sm_reasons = smart_money_score(df)

    score += sm_score
    reasons.extend(sm_reasons)

    # ==========================================
    # Liquidity Engine
    # ==========================================

    liq_score, liq_reasons = liquidity_score(df)

    score += liq_score
    reasons.extend(liq_reasons)

    # ==========================================
    # Structure Engine
    # ==========================================

    st_score, st_reasons = structure_score(df)

    score += st_score
    reasons.extend(st_reasons)

    # ==========================================
    # Order Block Engine
    # ==========================================

    ob_score, ob_reasons = order_block_score(df)

    score += ob_score
    reasons.extend(ob_reasons)

    # ==========================================
    # Fair Value Gap Engine
    # ==========================================

    fvg_points, fvg_reasons = fvg_score(df)

    score += fvg_points
    reasons.extend(fvg_reasons)

    # ==========================================
    # News Engine
    # ==========================================

    news_points, news_reasons = news_score(data)

    score += news_points
    reasons.extend(news_reasons)

    # ==========================================
    # Risk Engine
    # ==========================================

    trade = calculate_trade(df, score)
        # ==========================================
    # SCORE LIMIT
    # ==========================================

    if score > 300:
        score = 300

    elif score < -300:
        score = -300

    # ==========================================
    # REMOVE DUPLICATE REASONS
    # ==========================================

    reasons = list(dict.fromkeys(reasons))

    # ==========================================
    # FINAL RESULT
    # ==========================================

    return {

        "score": score,

        "reasons": reasons,

        "entry": trade["entry"],

        "sl": trade["sl"],

        "target1": trade["target1"],

        "target2": trade["target2"]

    }
