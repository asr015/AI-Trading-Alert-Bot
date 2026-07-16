# ==========================================
# TradingASR AI Pro v3.0
# File : market_breadth_engine.py
# Part 1 / 3
# ==========================================

import pandas as pd

from scanner import get_stock_data
from indicator_engine import calculate_indicators


# ==========================================
# NIFTY 50 STOCKS
# ==========================================

NIFTY50 = [

    "RELIANCE.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "SBIN.NS",
    "TCS.NS",
    "INFY.NS",
    "HCLTECH.NS",
    "LT.NS",
    "BHARTIARTL.NS",
    "AXISBANK.NS",
    "KOTAKBANK.NS",
    "ASIANPAINT.NS",
    "MARUTI.NS",
    "ULTRACEMCO.NS",
    "SUNPHARMA.NS",
    "BAJFINANCE.NS",
    "BAJAJFINSV.NS",
    "TITAN.NS",
    "NTPC.NS",
    "POWERGRID.NS",
    "ONGC.NS",
    "COALINDIA.NS",
    "ADANIPORTS.NS",
    "ADANIENT.NS",
    "HINDALCO.NS",
    "TATASTEEL.NS",
    "JSWSTEEL.NS",
    "GRASIM.NS",
    "EICHERMOT.NS",
    "HEROMOTOCO.NS",
    "CIPLA.NS",
    "DRREDDY.NS",
    "APOLLOHOSP.NS",
    "TECHM.NS",
    "WIPRO.NS",
    "INDUSINDBK.NS",
    "BEL.NS",
    "HAL.NS",
    "IRFC.NS",
    "RVNL.NS",
    "DLF.NS",
    "LODHA.NS",
    "GAIL.NS",
    "BPCL.NS",
    "IOC.NS",
    "CANBK.NS",
    "PNB.NS",
    "BANKBARODA.NS",
    "SAIL.NS",
    "NMDC.NS"

]


# ==========================================
# MARKET BREADTH
# ==========================================

def market_breadth():

    bullish = 0
    bearish = 0

    ema20 = 0
    ema50 = 0
    ema200 = 0

    rsi = 0
    volume = 0

    reasons = []

    total = 0

    for symbol in NIFTY50:

        data = get_stock_data(symbol)

        if data.empty:
            continue

        df = calculate_indicators(data)

        if len(df) < 30:
            continue

        last = df.iloc[-1]

        total += 1
                # ==========================================
        # EMA BREADTH
        # ==========================================

        if last["Close"] > last["EMA20"]:
            ema20 += 1

        if last["Close"] > last["EMA50"]:
            ema50 += 1

        if last["Close"] > last["EMA200"]:
            ema200 += 1

        # ==========================================
        # RSI BREADTH
        # ==========================================

        if last["RSI"] >= 60:
            rsi += 1

        # ==========================================
        # VOLUME BREADTH
        # ==========================================

        if last["RVOL"] >= 1.20:
            volume += 1

        # ==========================================
        # ADVANCE / DECLINE
        # ==========================================

        if last["Close"] > last["Open"]:
            bullish += 1
        else:
            bearish += 1

    # ==========================================
    # NO DATA
    # ==========================================

    if total == 0:

        return {
            "score": 0,
            "bullish": 0,
            "bearish": 0,
            "breadth": 0,
            "reasons": [
                "No market data"
            ]
        }

    # ==========================================
    # PERCENTAGES
    # ==========================================

    bull_percent = round((bullish / total) * 100, 1)

    bear_percent = round((bearish / total) * 100, 1)

    ema20_percent = round((ema20 / total) * 100, 1)

    ema50_percent = round((ema50 / total) * 100, 1)

    ema200_percent = round((ema200 / total) * 100, 1)

    rsi_percent = round((rsi / total) * 100, 1)

    volume_percent = round((volume / total) * 100, 1)

    score = 0
        # ==========================================
    # AI MARKET BREADTH SCORE
    # ==========================================

    if bull_percent >= 70:
        score += 30
        reasons.append("🟢 Strong Bullish Breadth")

    elif bull_percent >= 60:
        score += 20
        reasons.append("🟢 Bullish Breadth")

    elif bull_percent <= 30:
        score -= 30
        reasons.append("🔴 Strong Bearish Breadth")

    elif bull_percent <= 40:
        score -= 20
        reasons.append("🔴 Bearish Breadth")

    # EMA20
    if ema20_percent >= 70:
        score += 15
        reasons.append(f"✅ {ema20}/{total} Above EMA20")

    elif ema20_percent <= 30:
        score -= 15
        reasons.append(f"🔴 Only {ema20}/{total} Above EMA20")

    # EMA50
    if ema50_percent >= 70:
        score += 15
        reasons.append(f"✅ {ema50}/{total} Above EMA50")

    elif ema50_percent <= 30:
        score -= 15
        reasons.append(f"🔴 Only {ema50}/{total} Above EMA50")

    # EMA200
    if ema200_percent >= 70:
        score += 20
        reasons.append(f"✅ {ema200}/{total} Above EMA200")

    elif ema200_percent <= 30:
        score -= 20
        reasons.append(f"🔴 Only {ema200}/{total} Above EMA200")

    # RSI
    if rsi_percent >= 60:
        score += 10
        reasons.append("📈 Strong Market Momentum")

    elif rsi_percent <= 40:
        score -= 10
        reasons.append("📉 Weak Market Momentum")

    # Volume
    if volume_percent >= 50:
        score += 10
        reasons.append("💰 Broad Market Volume Expansion")

    # Score Limit
    score = max(min(score, 100), -100)

    return {

        "score": score,

        "bullish": bullish,

        "bearish": bearish,

        "breadth": bull_percent,

        "ema20": ema20_percent,

        "ema50": ema50_percent,

        "ema200": ema200_percent,

        "rsi": rsi_percent,

        "volume": volume_percent,

        "reasons": reasons

    }
