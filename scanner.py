# ==========================================
# TradingASR AI Pro v2.3
# File : scanner.py
# ==========================================

import time
import pandas as pd
import yfinance as yf

from config import TIMEFRAME, PERIOD

_cache = {}


def get_stock_data(symbol):

    global _cache

    if symbol in _cache:
        return _cache[symbol]

    for attempt in range(2):

        try:

            data = yf.download(
                symbol,
                period=PERIOD,
                interval=TIMEFRAME,
                auto_adjust=True,
                progress=False,
                threads=False,
                timeout=30
            )

            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.get_level_values(0)

            if data is None or data.empty:
                raise Exception("No Data")

            data = data.dropna()

            if data.empty:
                raise Exception("Empty Data")

            _cache[symbol] = data

            # Prevent unlimited cache growth
            if len(_cache) > 300:
                _cache.clear()

            return data

        except Exception as e:

            if attempt == 1:
                print(f"{symbol}: {e}")

            time.sleep(1)

    return pd.DataFrame()
