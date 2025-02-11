Solana Meme Coin Trading Bot
This bot scans for newly launched meme coins on Solana, filters them based on specific criteria, and executes trades using the Jupiter Swap API.
Features
Scans new meme coins launching on Solana via DEX Screener & alternative APIs.
Filters tokens based on liquidity (100k+), 24h buys (50+), and age (0-4 minutes).
Executes buy orders when age is between 0-4 minutes and sells at 4:30 minutes.
Stores trade history for analysis and reporting.
Generates a report with all executed trades in Google Sheets.
Automatically generates a Solana wallet if none is provided.
Prerequisites
Before you start, ensure you have the following installed:
Python 3.8+
pip (Python package manager)
PyCharm (Optional but recommended)
Solana Wallet (for transactions)
Installation
Clone the Repository:
git clone https://github.com/your-repo/solana-meme-bot.git
cd solana-meme-bot
Install Dependencies:
pip install -r requirements.txt
Set Up Environment Variables:


Running the Bot
Open PyCharm or any terminal and navigate to the project folder.
Run the bot using:
Python solana_bot.py
The bot will start scanning for new meme coins and executing trades based on the filters.
If no wallet is provided, it will generate one and display the public key.
Troubleshooting
No new tokens found? API might be down. Try restarting the bot later.
ImportError? Ensure you have installed dependencies using pip install -r requirements.txt.
Contributing
Feel free to fork the repo, make improvements, and submit pull requests!
License
MIT License
