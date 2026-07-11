import pandas as pd


def calculate_indicators(data):

    df = data.copy()

    # ========= EMA =========

    df["EMA20"] = df["Close"].ewm(span=20, adjust=False).mean()

    df["EMA50"] = df["Close"].ewm(span=50, adjust=False).mean()

    df["EMA200"] = df["Close"].ewm(span=200, adjust=False).mean()

    # ========= RSI =========

    delta = df["Close"].diff()

    gain = delta.clip(lower=0).rolling(window=14).mean()

    loss = (-delta.clip(upper=0)).rolling(window=14).mean()

    rs = gain / loss

    df["RSI"] = 100 - (100 / (1 + rs))

    # ========= MACD =========

    ema12 = df["Close"].ewm(span=12, adjust=False).mean()

    ema26 = df["Close"].ewm(span=26, adjust=False).mean()

    df["MACD"] = ema12 - ema26

    df["Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()

    # ========= VWAP =========

    typical_price = (
        df["High"] +
        df["Low"] +
        df["Close"]
    ) / 3

    cumulative_volume = df["Volume"].cumsum()

    df["VWAP"] = (
        (typical_price * df["Volume"]).cumsum()
        /
        cumulative_volume
    )

    # ========= ATR =========

    hl = df["High"] - df["Low"]

    hc = (df["High"] - df["Close"].shift()).abs()

    lc = (df["Low"] - df["Close"].shift()).abs()

    tr = pd.concat([hl, hc, lc], axis=1).max(axis=1)

    df["ATR"] = tr.rolling(window=14).mean()

    # ========= Relative Volume =========

    volume_average = df["Volume"].rolling(window=20).mean()

    df["RVOL"] = df["Volume"] / volume_average

    # ========= CLEANUP =========

    df.replace([float("inf"), float("-inf")], pd.NA, inplace=True)

    return df
