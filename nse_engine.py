import requests
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/option-chain",
    "Origin": "https://www.nseindia.com",
    "Connection": "keep-alive"
}

session = requests.Session()

def get_option_chain():

    # Get fresh cookies
    session.get(
        "https://www.nseindia.com/option-chain",
        headers=HEADERS,
        timeout=10
    )

    time.sleep(1)

    response = session.get(
        "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY",
        headers=HEADERS,
        timeout=10
    )

    response.raise_for_status()

    return response.json()
