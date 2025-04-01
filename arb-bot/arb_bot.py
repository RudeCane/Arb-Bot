import time
from binance_client import get_binance_price
from pancake_client import get_pancake_price, buy_on_pancake
from utils import calculate_arbitrage
import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

TOKEN_ADDRESS = os.getenv("TOKEN_ADDRESS")

def run():
    while True:
        try:
            bin_bid, bin_ask = get_binance_price("BUSD/USDT")
            pancake_price = get_pancake_price(TOKEN_ADDRESS)

            arbitrage, spread = calculate_arbitrage(bin_bid, pancake_price)

            print(f"Binance: {bin_bid} | Pancake: {pancake_price} | Spread: {spread:.2f}%")

            if arbitrage:
                print("✅ Arbitrage opportunity detected!")
                tx_hash = buy_on_pancake(TOKEN_ADDRESS, Web3.to_wei(1, 'ether'))
                print(f"Trade sent: {tx_hash}")
            else:
                print("❌ No arb opportunity")

            time.sleep(10)

        except Exception as e:
            print("Error:", e)
            time.sleep(5)

if __name__ == "__main__":
    run()
