# ==========================================
# TradingASR AI Pro v2.1
# File : config.py
# ==========================================

import os

# ==========================
# Telegram Secrets
# ==========================

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# ==========================
# Scanner Settings
# ==========================

TIMEFRAME = "1d"
PERIOD = "6mo"

# ---------- Trend ----------

EMA_BULLISH = 30
EMA200_BULLISH = 30
EMA_RISING = 25

EMA_BEARISH = -30
EMA200_BEARISH = -30
EMA_FALLING = -25

# ---------- Momentum ----------

RSI_BULLISH = 25
MACD_BULLISH = 25
VWAP_BULLISH = 20
CANDLE_BULLISH = 20
VOLUME_BULLISH = 25
RVOL_BULLISH = 25
MOMENTUM = 50

RSI_BEARISH = -25
MACD_BEARISH = -25
VWAP_BEARISH = -20
CANDLE_BEARISH = -20
SELLING = -25
BEARISH_MOMENTUM = -50

# ---------- Smart Money ----------

SMART_ENTRY = 60
SMART_EXIT = -60

# ---------- Liquidity ----------

LIQUIDITY = 40

# ---------- Structure ----------

BOS = 40
CHOCH = -40

# ---------- Order Block ----------

ORDER_BLOCK = 40

# ---------- Fair Value Gap ----------

FVG = 40
FVG_HOLD = 20

# ---------- News ----------

POSITIVE_NEWS = 20
NEGATIVE_NEWS = -20

# ---------- Market Bias ----------

BULLISH_BIAS = 30
BEARISH_BIAS = -30

# ---------- Option Chain ----------

PCR_BULLISH = 30
PCR_BEARISH = -30

# ---------- Final Score ----------

BUY_SCORE = 220
SELL_SCORE = -220

STRONG_BUY = 300
STRONG_SELL = -300

# ---------- Risk Reward ----------

RR1 = 2
RR2 = 3
