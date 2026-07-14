# ==========================================
# TradingASR AI Pro v2.2
# File : dynamic_watchlist.py
# ==========================================

import requests
import pandas as pd
from io import StringIO


def get_watchlist():

    try:

        url = "https://archives.nseindia.com/content/fo/fo_mktlots.csv"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        response.raise_for_status()

        df = pd.read_csv(
            StringIO(response.text),
            skiprows=1,
            on_bad_lines="skip"
        )

        symbols = []

        # Second column normally contains the symbol
        if len(df.columns) > 1:

            for symbol in df.iloc[:, 1]:

                symbol = str(symbol).strip().upper()

                if (
                    symbol
                    and symbol != "SYMBOL"
                    and symbol != "NAN"
                ):
                    symbols.append(symbol + ".NS")

        symbols = sorted(set(symbols))

        if symbols:
            print(f"Loaded {len(symbols)} F&O Stocks")
            return symbols

    except Exception as e:

        print("Dynamic Watchlist Error:", e)

    print("Using fallback watchlist...")

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
