import pandas as pd

def calculate_indicators(data):

    df = data.copy()

    # ========= EMA =========

    df["EMA20"] = df["Close"].ewm(span=20).mean()

    df["EMA50"] = df["Close"].ewm(span=50).mean()

    df["EMA200"] = df["Close"].ewm(span=200).mean()

    # ========= RSI =========

    delta = df["Close"].diff()

    gain = delta.clip(lower=0).rolling(14).mean()

    loss = (-delta.clip(upper=0)).rolling(14).mean()

    rs = gain / loss

    df["RSI"] = 100 - (100 / (1 + rs))

    # ========= MACD =========

    ema12 = df["Close"].ewm(span=12).mean()

    ema26 = df["Close"].ewm(span=26).mean()

    df["MACD"] = ema12 - ema26

    df["Signal"] = df["MACD"].ewm(span=9).mean()

    # ========= VWAP =========

    typical_price = (
        df["High"] +
        df["Low"] +
        df["Close"]
    ) / 3

    df["VWAP"] = (
        (typical_price * df["Volume"]).cumsum()
        /
        df["Volume"].cumsum()
    )

    # ========= ATR =========

    hl = df["High"] - df["Low"]

    hc = (df["High"] - df["Close"].shift()).abs()

    lc = (df["Low"] - df["Close"].shift()).abs()

    tr = pd.concat([hl, hc, lc], axis=1).max(axis=1)

    df["ATR"] = tr.rolling(14).mean()

    # ========= Relative Volume =========

    df["RVOL"] = (
        df["Volume"]
        /
        df["Volume"].rolling(20).mean()
    )

    return df
