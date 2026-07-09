import yfinance as yf
from config import TIMEFRAME, PERIOD


def get_stock_data(symbol):

    stock = yf.Ticker(symbol)

    data = stock.history(
        period=PERIOD,
        interval=TIMEFRAME,
        auto_adjust=True
    )

    return data
