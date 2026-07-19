# ==========================================
# TradingASR AI Pro v4.0
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

_cookie_ready = False


def refresh_session(force=False):
    global _cookie_ready

    if _cookie_ready and not force:
        return True

    try:
        session.cookies.clear()

        r = session.get(
            BASE_URL,
            timeout=15
        )

        r.raise_for_status()

        _cookie_ready = True
        return True

    except Exception as e:
        print(f"NSE Session Error : {e}")
        return False


def get_option_chain():

    if not refresh_session():
        return None

    last_error = None

    for attempt in range(2):

        try:

            response = session.get(
                OPTION_CHAIN_URL,
                timeout=15
            )

            response.raise_for_status()

            data = response.json()

            if (
                "records" not in data
                or "data" not in data["records"]
            ):
                raise ValueError("Invalid NSE Response")

            return data

        except Exception as e:

            last_error = str(e)

            print(
                f"NSE Retry {attempt+1}/2 : {last_error}"
            )

            refresh_session(force=True)

            time.sleep(1)

    print(
        f"NSE Option Chain Failed : {last_error}"
    )

    return None
