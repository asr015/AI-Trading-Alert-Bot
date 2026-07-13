# ==========================================
# TradingASR AI Pro v2.0
# File : scanner.py
# ==========================================

import pandas as pd
import yfinance as yf

from config import TIMEFRAME, PERIOD


def get_stock_data(symbol):

    try:

        stock = yf.Ticker(symbol)

        data = stock.history(
            period=PERIOD,
            interval=TIMEFRAME,
            auto_adjust=True
        )

        if data is None or data.empty:
            return pd.DataFrame()

        return data

    except Exception as e:

        print(f"{symbol}: {e}")

        return pd.DataFrame()
