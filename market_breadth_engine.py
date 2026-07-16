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
