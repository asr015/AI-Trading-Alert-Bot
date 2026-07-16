# ==========================================
# TradingASR AI Pro v3.0
# File : nse_engine.py
# ==========================================

import time
import requests

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
    "Origin": "https://www.nseindia.com",
    "Connection": "keep-alive"
}

session = requests.Session()
session.headers.update(HEADERS)


def refresh_session():

    session.cookies.clear()

    response = session.get(
        BASE_URL,
        timeout=20
    )

    response.raise_for_status()

    time.sleep(1)


def get_option_chain():

    last_error = None

    for attempt in range(5):

        try:

            refresh_session()

            response = session.get(
                OPTION_CHAIN_URL,
                timeout=20
            )

            if response.status_code != 200:
                raise Exception(
                    f"HTTP {response.status_code}"
                )

            data = response.json()

            if (
                "records" not in data
                or "data" not in data["records"]
            ):
                raise Exception(
                    "Invalid NSE Response"
                )

            return data

        except Exception as e:

            last_error = str(e)

            print(
                f"NSE Retry {attempt+1}/5 : {last_error}"
            )

            time.sleep(2)

    raise Exception(
        f"NSE Option Chain Failed : {last_error}"
)
