import yfinance as yf

def get_scanner_data(symbol):

    stock = yf.Ticker(symbol)

    data = stock.history(period="5d", interval="15m")

    return data
