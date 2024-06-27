import requests
from datetime import datetime


url = "https://api.coingecko.com/api/v3/coins/bitcoin"
# Definujeme datum genesis blocku
genesis_block_date = datetime(2009, 1, 3)
# Zjistíme aktuální datum
current_date = datetime.now()

# Vypočítáme počet dní od genesis blocku
days_since_genesis_block = (current_date - genesis_block_date).days

# Koeficient a exponent podle daného vzorce
coefficient = 1.0117e-17
exponent = 5.82

# Vypočítáme fair price
fair_price = coefficient * (days_since_genesis_block ** exponent)

# Vypočítáme bottom price jako 42% z fair price
bottom_price = fair_price * 0.42
print(fair_price)

try:
    response = requests.get(url)
    response.raise_for_status()  # zkontroluje, zda nedošlo k chybě
    data = response.json()  # převede odpověď na JSON

    # Výstup dat
    print(data["market_data"]["current_price"]["usd"])

except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"Other error occurred: {err}")
