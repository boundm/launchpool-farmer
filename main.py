import requests
from src.exchanges_api import gate



def bybit():
    response = requests.get("https://api.bybit.com/v5/market/tickers?category=linear")
    print(response.json())



def main():
    print(gate('ZORA'))

if __name__ == "__main__":
    main()