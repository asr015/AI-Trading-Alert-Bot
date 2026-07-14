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

        # Skip invalid header lines
        df = pd.read_csv(
            StringIO(response.text),
            skiprows=1,
            on_bad_lines="skip"
        )

        symbols = []

        for col in df.columns:

            if "symbol" in col.lower():

                for symbol in df[col]:

                    symbol = str(symbol).strip()

                    if (
                        symbol
                        and symbol.lower() != "nan"
                        and symbol.upper() != "SYMBOL"
                    ):
                        symbols.append(symbol + ".NS")

                break

        symbols = sorted(list(set(symbols)))

        if len(symbols) > 0:
            return symbols

    except Exception as e:

        print("Dynamic Watchlist Error:", e)

    # Fallback Watchlist
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
