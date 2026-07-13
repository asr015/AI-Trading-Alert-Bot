# ==========================================
# TradingASR AI Pro v2.1
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

        if data is None or data.empty:
            return pd.DataFrame()

        _cache[symbol] = data

        print(data.columns)
print(type(data.columns))

        return data

    except Exception as e:

        print(f"{symbol}: {e}")

        return pd.DataFrame()
