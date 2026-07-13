# ==========================================
# TradingASR AI Pro v2.0
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

        df = pd.read_csv(StringIO(response.text))

        symbols = []

        for symbol in df.iloc[:, 1]:

            symbol = str(symbol).strip()

            if (
                symbol
                and symbol != "SYMBOL"
                and symbol.lower() != "nan"
            ):
                symbols.append(symbol + ".NS")

        return sorted(list(set(symbols)))

    except Exception as e:

        print("Dynamic Watchlist Error:", e)

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
