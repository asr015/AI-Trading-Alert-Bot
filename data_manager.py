from nifty import get_nifty_data
from market_status import get_market_status

def get_market_data():

    data = get_nifty_data()

    return {
        "nifty": data,
        "market_status": get_market_status()
    }
