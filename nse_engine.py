# ==========================================
# TradingASR AI Pro v2.1
# File : nse_engine.py
# ==========================================

import requests
import time

BASE_URL = "https://www.nseindia.com"

OPTION_CHAIN_URL = (
    "https://www.nseindia.com/api/"
    "option-chain-indices?symbol=NIFTY"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json,text/plain,*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/option-chain",
    "Connection": "keep-alive"
}

session = requests.Session()
session.headers.update(HEADERS)


def get_option_chain():

    last_error = None

    for attempt in range(3):

        try:

            # Refresh cookies
            session.get(
                BASE_URL,
                timeout=15
            )

            time.sleep(1)

            response = session.get(
                OPTION_CHAIN_URL,
                timeout=20
            )

            response.raise_for_status()

            data = response.json()

            if (
                "records" in data
                and "data" in data["records"]
            ):
                return data

            raise Exception("Invalid NSE response")

        except Exception as e:

            last_error = e

            time.sleep(2)

    raise Exception(
        f"NSE Option Chain Error : {last_error}"
    )
