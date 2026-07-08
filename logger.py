from datetime import datetime
from zoneinfo import ZoneInfo

def log(message):

    ist = ZoneInfo("Asia/Kolkata")

    now = datetime.now(ist).strftime("%d-%m-%Y %H:%M:%S")

    print(f"[{now}] {message}")
