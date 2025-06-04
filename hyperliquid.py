import ccxt
from config import HYPERLIQUID_ADRESS, HYPERLIQUID_KEY

def get_funding(ticker: str):
    dex = ccxt.hyperliquid({
    "walletAddress": HYPERLIQUID_ADRESS,
    "privateKey": HYPERLIQUID_KEY,
    'enableRateLimit': True
})
    ticker = ticker.upper() + '/USDC:USDC'
    funding_rate = dex.fetch_funding_rates([ticker])
    funding = float(funding_rate[ticker]['fundingRate'])*100

    return funding



if __name__ == "__main__":
    print(get_funding('zora'))


	
