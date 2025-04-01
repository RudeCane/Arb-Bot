import ccxt
import os
from dotenv import load_dotenv

load_dotenv()

binance = ccxt.binance({
    'apiKey': os.getenv("BINANCE_API_KEY"),
    'secret': os.getenv("BINANCE_SECRET"),
    'enableRateLimit': True
})

def get_binance_price(symbol="BUSD/USDT"):
    ticker = binance.fetch_ticker(symbol)
    return ticker['bid'], ticker['ask']

def create_binance_order(symbol, side, amount, price):
    return binance.create_limit_order(symbol, side, amount, price)
