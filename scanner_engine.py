# ==========================================
# TradingASR AI Pro v2.0
# File : scanner_engine.py
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

    if len(df) < 25:

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
    # CANDLE
    # ==========================================

    if last["Close"] > last["Open"]:

        score += CANDLE_BULLISH

        reasons.append("✅ Bullish Candle")

    else:

        score += CANDLE_BEARISH

        reasons.append("🔴 Bearish Candle")



    # ==========================================
    # VOLUME
    # ==========================================

    if last["Volume"] > prev["Volume"]:

        score += VOLUME_BULLISH

        reasons.append("✅ Volume Expansion")



    if last["RVOL"] >= 1.5:

        score += RVOL_BULLISH

        reasons.append("✅ High Relative Volume")



    # ==========================================
    # EMA SLOPE
    # ==========================================

    if last["EMA20"] > prev["EMA20"]:

        score += EMA_RISING

        reasons.append("✅ EMA Rising")

    else:

        score += EMA_FALLING

        reasons.append("🔴 EMA Falling")



    # ==========================================
    # MOMENTUM BEFORE MOMENTUM
    # ==========================================

    if (

        last["EMA20"] > last["EMA50"]

        and last["RSI"] > 55

        and last["RVOL"] > 1.5

        and last["Volume"] > prev["Volume"]

    ):

        score += MOMENTUM

        reasons.append("🚀 Momentum Before Momentum")
