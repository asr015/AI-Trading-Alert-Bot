import yfinance as yf
from datetime import datetime
from zoneinfo import ZoneInfo

def get_nifty_data():

    nifty = yf.Ticker("^NSEI")
    data = nifty.history(period="2d")

    last_price = round(data["Close"].iloc[-1], 2)
    prev_close = round(data["Close"].iloc[-2], 2)

    change = round(last_price - prev_close, 2)
    change_pct = round((change / prev_close) * 100, 2)

    ist = ZoneInfo("Asia/Kolkata")
    now = datetime.now(ist)

    market_open = (
        now.weekday() < 5 and
        ((now.hour > 9 or (now.hour == 9 and now.minute >= 15)) and
         (now.hour < 15 or (now.hour == 15 and now.minute <= 30)))
    )

    status = "🟢 OPEN" if market_open else "🔴 CLOSED"

    return {
        "price": last_price,
        "change": change,
        "change_pct": change_pct,
        "status": status,
        "time": now.strftime("%d-%m-%Y %I:%M %p")
    }
