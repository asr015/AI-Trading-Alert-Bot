# ==========================================
# TradingASR AI Pro v4.0
# File : scanner_engine.py
# Part 1 / 6
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


# ==========================================
# AI TECHNICAL SCORE
# ==========================================

def calculate_score(data):

    df = calculate_indicators(data)

    if df is None or len(df) < 30:

        return {

            "score": 0,

            "setup": "⭐ Ignore",

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

    confirmations = 0
        # ==========================================
    # EMA ALIGNMENT
    # ==========================================

    if last["EMA20"] > last["EMA50"]:

        score += EMA_BULLISH
        confirmations += 1
        reasons.append("✅ EMA20 > EMA50")

    else:

        score += EMA_BEARISH
        reasons.append("🔴 EMA20 < EMA50")

    if last["EMA50"] > last["EMA200"]:

        score += EMA200_BULLISH
        confirmations += 1
        reasons.append("✅ Above EMA200")

    else:

        score += EMA200_BEARISH
        reasons.append("🔴 Below EMA200")

    # ==========================================
    # EMA SLOPE
    # ==========================================

    if last["EMA20"] > prev["EMA20"]:

        score += EMA_RISING
        confirmations += 1
        reasons.append("📈 EMA Rising")

    else:

        score += EMA_FALLING
        reasons.append("📉 EMA Falling")

    # ==========================================
    # RSI
    # ==========================================

    if last["RSI"] >= 60:

        score += RSI_BULLISH
        confirmations += 1
        reasons.append("💪 Strong RSI")

    elif last["RSI"] <= 40:

        score += RSI_BEARISH
        reasons.append("⚠️ Weak RSI")

    # ==========================================
    # MACD
    # ==========================================

    if last["MACD"] > last["Signal"]:

        score += MACD_BULLISH
        confirmations += 1
        reasons.append("✅ MACD Bullish")

    else:

        score += MACD_BEARISH
        reasons.append("🔴 MACD Bearish")

    # ==========================================
    # VWAP
    # ==========================================

    if last["Close"] > last["VWAP"]:

        score += VWAP_BULLISH
        confirmations += 1
        reasons.append("📊 Above VWAP")

    else:

        score += VWAP_BEARISH
        reasons.append("📉 Below VWAP")
            # ==========================================
    # ATR FILTER
    # ==========================================

    atr_percent = (last["ATR"] / last["Close"]) * 100

    if 1 <= atr_percent <= 5:

        score += 15
        confirmations += 1
        reasons.append("📏 Healthy ATR")

    elif atr_percent > 5:

        score -= 10
        reasons.append("⚠️ High Volatility")

    # ==========================================
    # RELATIVE VOLUME
    # ==========================================

    if last["RVOL"] >= 1.50:

        score += RVOL_BULLISH
        confirmations += 1
        reasons.append("📈 High Relative Volume")

    elif last["RVOL"] >= 1.20:

        score += 15
        confirmations += 1
        reasons.append("📊 Good Relative Volume")

    # ==========================================
    # VOLUME EXPANSION
    # ==========================================

    if last["Volume"] > prev["Volume"]:

        score += VOLUME_BULLISH
        confirmations += 1
        reasons.append("💰 Volume Expansion")

    # ==========================================
    # MOMENTUM BEFORE MOMENTUM
    # ==========================================

    if (

        last["EMA20"] > last["EMA50"]

        and last["RSI"] > 55

        and last["RVOL"] > 1.50

        and last["MACD"] > last["Signal"]

        and last["Close"] > last["VWAP"]

    ):

        score += MOMENTUM
        confirmations += 2
        reasons.append("🚀 Momentum Before Momentum")

    # ==========================================
    # SMART MONEY ENGINE
    # ==========================================

    sm_score, sm_reasons = smart_money_score(df)

    score += sm_score

    if sm_score > 0:
        confirmations += 1

    reasons.extend(sm_reasons)
