import json
import time

import requests
from solana.rpc.api import Client
from solders.keypair import Keypair

# Load Private Key Securely
with open("config.json'") as f:
    config = json.load(f)


wallet = Keypair.from_base58_string(config["private_key"])



# Solana RPC Client
SOLANA_RPC = "https://api.mainnet-beta.solana.com"
client = Client(SOLANA_RPC)

# DexScreener API
DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/pairs/solana"

# Trading Filters
MIN_LIQUIDITY = 100000  # Minimum $100K liquidity
MIN_BUYS = 50  # At least 50 buys in 24h
BUY_AGE_LIMIT = 4 * 60  # Buy coins younger than 4 minutes
SELL_AGE_LIMIT = 4.5 * 60  # Sell at 4 minutes 30 seconds


def fetch_new_meme_coins():
    """Fetches new meme coins from DexScreener API and filters them."""
    response = requests.get(DEXSCREENER_API)
    if response.status_code == 200:
        data = response.json()
        eligible_coins = []
        current_time = time.time()

        for pair in data.get("pairs", []):
            pair_age = (current_time - pair["pairCreatedAt"] / 1000)

            if (pair["liquidity"]["usd"] >= MIN_LIQUIDITY and
                    pair["txns"]["h24"]["buys"] >= MIN_BUYS and
                    0 < pair_age < BUY_AGE_LIMIT):
                eligible_coins.append(pair)

        return eligible_coins
    else:
        print("Failed to fetch data")
        return []


def execute_trade(pair_address, trade_type="buy"):
    """Executes buy/sell order on Solana DEX (Raydium or Jupiter)."""
    print(f"Executing {trade_type} order for {pair_address}")

    # Placeholder for DEX trade execution
    pass


def main():
    """Main loop to monitor and trade meme coins."""
    while True:
        meme_coins = fetch_new_meme_coins()
        for coin in meme_coins:
            execute_trade(coin["pairAddress"], trade_type="buy")
            time.sleep(SELL_AGE_LIMIT - BUY_AGE_LIMIT)  # Wait until sell time
            execute_trade(coin["pairAddress"], trade_type="sell")

        time.sleep(10)  # Wait before fetching new coins again


if __name__ == "__main__":
    main()
