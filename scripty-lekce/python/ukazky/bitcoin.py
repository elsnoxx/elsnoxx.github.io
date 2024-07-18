import requests
from datetime import datetime

# https://docs.coingecko.com/reference/introduction


def bitcoinData(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # zkontroluje, zda nedošlo k chybě
        data = response.json()  # převede odpověď na JSON

        # Výstup dat
        print(data["market_data"]["current_price"]["usd"])
        print(data["market_data"]["ath"]["usd"])
        print(data["market_data"]["ath_change_percentage"]["usd"])
        print(data["market_data"]["market_cap"]["usd"])
        print(data["market_data"]["high_24h"]["usd"])
        print(data["market_data"]["low_24h"]["usd"])
        print(data["market_data"]["price_change_percentage_24h"])

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

def trendingData(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # zkontroluje, zda nedošlo k chybě
        data = response.json()  # převede odpověď na JSON

        # Výstup dat
        for item in data["coins"]:
            print("{0} price is {1} 24h change is {2}% marketcap of coin is {3}".format(item["item"]["name"], item["item"]["data"]["price"], item["item"]["data"]["price_change_percentage_24h"]["usd"], item["item"]["data"]["market_cap"]))
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

def marketData(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # zkontroluje, zda nedošlo k chybě
        data = response.json()  # převede odpověď na JSON

        # Výstup dat
        for item in data["data"]["market_cap_percentage"]:
            print(item + " " + str(data["data"]["market_cap_percentage"][item]))
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


url = "https://api.coingecko.com/api/v3/coins/bitcoin"

# data about compenies and their holdings of BTC
url2 = "https://api.coingecko.com/api/v3/companies/public_treasury/bitcoin"

# This endpoint allows you query trending search coins, nfts and categories on CoinGecko in the last 24 hours.
url3 = "https://api.coingecko.com/api/v3/search/trending"

# This endpoint allows you query cryptocurrency global data including active cryptocurrencies, markets, total crypto market cap and etc.
url4 = "https://api.coingecko.com/api/v3/global"

# bitcoinData(url)

# trendingData(url3)

marketData(url4)