import pandas as pd

def calculate_indicators(data):

    if data.empty:
        return data

    df = data.copy()

    # EMA 20
    df["EMA20"] = df["Close"].ewm(span=20, adjust=False).mean()

    # EMA 50
    df["EMA50"] = df["Close"].ewm(span=50, adjust=False).mean()

    # RSI (14)
    delta = df["Close"].diff()

    gain = delta.where(delta > 0, 0).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()

    rs = gain / loss

    df["RSI"] = 100 - (100 / (1 + rs))

    # Fill NaN values
    df = df.fillna(0)

    return df
