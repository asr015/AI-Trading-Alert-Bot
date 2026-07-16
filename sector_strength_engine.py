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
