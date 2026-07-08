from datetime import datetime
from zoneinfo import ZoneInfo

def get_market_status():

    ist = ZoneInfo("Asia/Kolkata")
    now = datetime.now(ist)

    weekday = now.weekday()

    if weekday >= 5:
        return "🔴 CLOSED (Weekend)"

    market_start = (9, 15)
    market_end = (15, 30)

    current = (now.hour, now.minute)

    if current < market_start:
        return "🟡 PRE-MARKET"

    elif current <= market_end:
        return "🟢 OPEN"

    else:
        return "🔴 CLOSED"
