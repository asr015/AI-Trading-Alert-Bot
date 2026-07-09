import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "application/json,text/html"
}

session = requests.Session()

def get_option_chain():

    # First request for cookies
    session.get(
        "https://www.nseindia.com",
        headers=HEADERS,
        timeout=10
    )

    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

    response = session.get(
        url,
        headers=HEADERS,
        timeout=10
    )

    response.raise_for_status()

    return response.json()
