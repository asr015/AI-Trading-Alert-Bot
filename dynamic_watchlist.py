# ==========================================
# TradingASR AI Pro v2.0
# File : dynamic_watchlist.py
# ==========================================

import pandas as pd


def get_watchlist():

    try:

        url = (
            "https://archives.nseindia.com/content/fo/"
            "fo_mktlots.csv"
        )

        df = pd.read_csv(url)

        symbols = []

        for symbol in df.iloc[:, 1]:

            symbol = str(symbol).strip()

            if (
                symbol
                and symbol != "SYMBOL"
                and symbol != "nan"
            ):
                symbols.append(symbol + ".NS")

        symbols = sorted(list(set(symbols)))

        return symbols

    except Exception as e:

        print(f"Dynamic Watchlist Error: {e}")

        return [
            "RELIANCE.NS",
            "HDFCBANK.NS",
            "ICICIBANK.NS",
            "SBIN.NS",
            "TCS.NS",
            "INFY.NS",
            "HCLTECH.NS",
            "LT.NS",
            "BHARTIARTL.NS",
            "TATAMOTORS.NS"
        ]
