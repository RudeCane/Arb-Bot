def calculate_arbitrage(binance_bid, pancake_price):
    profit_threshold = 0.5  # %
    spread = ((pancake_price - binance_bid) / binance_bid) * 100
    return spread >= profit_threshold, spread
