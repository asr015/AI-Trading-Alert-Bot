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
            # ==========================================
    # NO DATA
    # ==========================================

    if not sector_scores:

        return {

            "score": 0,

            "strongest": "N/A",

            "weakest": "N/A",

            "sectors": {},

            "reasons": [

                "No sector data"

            ]

        }

    # ==========================================
    # STRONGEST & WEAKEST SECTOR
    # ==========================================

    strongest = max(

        sector_scores,

        key=lambda x: sector_scores[x]["score"]

    )

    weakest = min(

        sector_scores,

        key=lambda x: sector_scores[x]["score"]

    )

    overall = sum(

        s["score"]

        for s in sector_scores.values()

    ) / len(sector_scores)

    overall = round(overall)

    # ==========================================
    # AI SCORE
    # ==========================================

    ai_score = 0

    if overall >= 70:

        ai_score = 30

        reasons.append(

            "🟢 Broad Sector Strength"

        )

    elif overall >= 55:

        ai_score = 20

        reasons.append(

            "🟢 Positive Sector Rotation"

        )

    elif overall <= 30:

        ai_score = -30

        reasons.append(

            "🔴 Broad Sector Weakness"

        )

    elif overall <= 45:

        ai_score = -20

        reasons.append(

            "🔴 Weak Sector Participation"

        )

    reasons.append(

        f"🏆 Strongest Sector : {strongest}"

    )

    reasons.append(

        f"⚠️ Weakest Sector : {weakest}"

    )

    return {

        "score": ai_score,

        "overall": overall,

        "strongest": strongest,

        "weakest": weakest,

        "sectors": sector_scores,

        "reasons": reasons

    }
