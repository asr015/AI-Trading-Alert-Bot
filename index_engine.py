# ==========================================
# TradingASR AI Pro v3.0
# File : index_engine.py
# Part 1 / 3
# ==========================================

import pandas as pd
import yfinance as yf

from indicator_engine import calculate_indicators
from risk_engine import calculate_trade


# ==========================================
# INDEX SYMBOLS
# ==========================================

INDEXES = {
    "NIFTY": "^NSEI",
    "BANKNIFTY": "^NSEBANK"
}


# ==========================================
# DOWNLOAD INDEX DATA
# ==========================================

def get_index_data(symbol):

    try:

        df = yf.download(
            symbol,
            period="6mo",
            interval="1d",
            auto_adjust=True,
            progress=False,
            threads=False,
            timeout=30
        )

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        if df is None or df.empty:
            return pd.DataFrame()

        df = df.dropna()

        return df

    except Exception as e:

        print(f"{symbol} : {e}")

        return pd.DataFrame()


# ==========================================
# ANALYZE SINGLE INDEX
# ==========================================

def analyze_index(name, symbol):

    data = get_index_data(symbol)

    if data.empty:

        return {
            "index": name,
            "signal": "NO DATA",
            "score": 0,
            "confidence": "0%",
            "reasons": [
                "Unable to download index data"
            ]
        }

    df = calculate_indicators(data)

    if len(df) < 30:

        return {
            "index": name,
            "signal": "NO DATA",
            "score": 0,
            "confidence": "0%",
            "reasons": [
                "Not enough historical candles"
            ]
        }

    last = df.iloc[-1]
    prev = df.iloc[-2]

    score = 0
    reasons = []
