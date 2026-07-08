import requests

BASE_URL = "https://www.nseindia.com"
OPTION_CHAIN_URL = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/option-chain"
}

def get_option_chain():

    session = requests.Session()

    # Get cookies first
    session.get(BASE_URL, headers=HEADERS, timeout=10)

    # Fetch option chain
    response = session.get(
        OPTION_CHAIN_URL,
        headers=HEADERS,
        timeout=10
    )

    response.raise_for_status()

    return response.json()
