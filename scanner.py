# ==========================================
# TradingASR AI Pro v2.4
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

    last_error = None

    for attempt in range(3):

        try:

            data = yf.download(
                symbol,
                period=PERIOD,
                interval=TIMEFRAME,
                auto_adjust=True,
                progress=False,
                threads=False,
                timeout=20
            )

            # MultiIndex Fix
            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.get_level_values(0)

            if data is None or data.empty:
                raise ValueError("No Data")

            # Required Columns
            required = ["Open", "High", "Low", "Close", "Volume"]

            missing = [c for c in required if c not in data.columns]

            if missing:
                raise ValueError(f"Missing Columns : {missing}")

            data = data.dropna()

            if data.empty:
                raise ValueError("Empty Data")

            data = data[~data.index.duplicated(keep="last")]

            data = data.sort_index()

            _cache[symbol] = data

            if len(_cache) > 300:
                _cache.clear()

            return data

        except Exception as e:

            last_error = str(e)

            if attempt < 2:
                time.sleep(1)

    print(f"{symbol}: {last_error}")

    return pd.DataFrame()
