# ==========================================
# TradingASR AI Pro v2.2
# File : scanner.py
# ==========================================

import pandas as pd
import yfinance as yf

from config import TIMEFRAME, PERIOD

_cache = {}


def get_stock_data(symbol):

    global _cache

    try:

        if symbol in _cache:
            return _cache[symbol]

        data = yf.download(
            symbol,
            period=PERIOD,
            interval=TIMEFRAME,
            auto_adjust=True,
            progress=False,
            threads=True
        )

        # ==========================================
        # FIX : yfinance MultiIndex Columns
        # ==========================================
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        if data is None or data.empty:
            return pd.DataFrame()

        _cache[symbol] = data

        return data

    except Exception as e:

        print(f"{symbol}: {e}")

        return pd.DataFrame()
