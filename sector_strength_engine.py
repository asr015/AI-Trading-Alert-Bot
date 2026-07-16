# ==========================================
# TradingASR AI Pro v3.0
# File : sector_strength_engine.py
# Part 1 / 3
# ==========================================

from scanner import get_stock_data
from indicator_engine import calculate_indicators


# ==========================================
# SECTOR WATCHLIST
# ==========================================

SECTORS = {

    "BANKING": [
        "HDFCBANK.NS",
        "ICICIBANK.NS",
        "SBIN.NS",
        "AXISBANK.NS",
        "KOTAKBANK.NS"
    ],

    "IT": [
        "TCS.NS",
        "INFY.NS",
        "HCLTECH.NS",
        "TECHM.NS",
        "WIPRO.NS"
    ],

    "PHARMA": [
        "SUNPHARMA.NS",
        "DRREDDY.NS",
        "CIPLA.NS",
        "APOLLOHOSP.NS"
    ],

    "AUTO": [
        "MARUTI.NS",
        "M&M.NS",
        "TATAMOTORS.NS",
        "HEROMOTOCO.NS",
        "EICHERMOT.NS"
    ],

    "METAL": [
        "TATASTEEL.NS",
        "JSWSTEEL.NS",
        "HINDALCO.NS",
        "SAIL.NS",
        "NMDC.NS"
    ],

    "ENERGY": [
        "RELIANCE.NS",
        "ONGC.NS",
        "BPCL.NS",
        "IOC.NS",
        "GAIL.NS"
    ],

    "DEFENCE": [
        "HAL.NS",
        "BEL.NS",
        "BHEL.NS"
    ],

    "REALTY": [
        "DLF.NS",
        "LODHA.NS"
    ]

}


# ==========================================
# SECTOR STRENGTH
# ==========================================

def sector_strength():

    sector_scores = {}

    reasons = []
        # ==========================================
    # CALCULATE EACH SECTOR
    # ==========================================

    for sector, stocks in SECTORS.items():

        score = 0
        bullish = 0
        total = 0

        for symbol in stocks:

            data = get_stock_data(symbol)

            if data.empty:
                continue

            df = calculate_indicators(data)

            if len(df) < 30:
                continue

            last = df.iloc[-1]

            total += 1

            # EMA Trend
            if (
                last["EMA20"] > last["EMA50"]
                and last["EMA50"] > last["EMA200"]
            ):
                score += 20
                bullish += 1

            # RSI
            if last["RSI"] >= 60:
                score += 15

            # MACD
            if last["MACD"] > last["Signal"]:
                score += 15

            # VWAP
            if last["Close"] > last["VWAP"]:
                score += 10

            # Relative Volume
            if last["RVOL"] >= 1.20:
                score += 10

        if total == 0:
            continue

        score = round(score / total)

        sector_scores[sector] = {
            "score": score,
            "bullish": bullish,
            "total": total
            }
