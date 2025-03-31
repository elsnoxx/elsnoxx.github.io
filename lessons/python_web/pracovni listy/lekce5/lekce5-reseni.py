# Pracovní list: Práce s JSON a HTTP požadavky

# ------------------------------------------------------------------------------ 
# Úkol 1: Čtení JSON souboru
# Máš JSON soubor s názvem "data.json", který obsahuje následující data:
# {
#     "name": "John Doe",
#     "age": 30,
#     "address": {
#         "street": "123 Main St",
#         "city": "New York"
#     }
# }
# Načti tento soubor pomocí modulu `json` a vypiš jméno a město.

import json

# Řešení:
with open('data.json', 'r') as file:
    data = json.load(file)

print(f"Jméno: {data['name']}")
print(f"Město: {data['address']['city']}")

# ------------------------------------------------------------------------------ 
# Úkol 2: Zápis do JSON souboru
# Vytvoř Python slovník s následujícími daty:
# {
#     "product": "Notebook",
#     "price": 1500,
#     "in_stock": True
# }
# Ulož tento slovník do souboru s názvem "product.json" ve formátu JSON.

# Řešení:
product_data = {
    "product": "Notebook",
    "price": 1500,
    "in_stock": True
}

with open('product.json', 'w') as file:
    json.dump(product_data, file, indent=4)

# ------------------------------------------------------------------------------ 
# Úkol 3: Základní GET požadavek
# Použij knihovnu `requests` a odešli GET požadavek na následující URL:
# https://jsonplaceholder.typicode.com/posts/1
# Získaná data vypiš ve formátu JSON a zobraz hodnoty klíčů "title" a "body".

import requests

# Řešení:
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
data = response.json()

print(f"Title: {data['title']}")
print(f"Body: {data['body']}")

# ------------------------------------------------------------------------------ 
# Úkol 4: Odeslání POST požadavku
# Odešli POST požadavek na URL https://jsonplaceholder.typicode.com/posts
# s následujícími daty:
# {
#     "title": "foo",
#     "body": "bar",
#     "userId": 1
# }
# Vypiš stavový kód odpovědi a data, která server vrátil.

# Řešení:
payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)

print(f"Status Code: {response.status_code}")
print(f"Response JSON: {response.json()}")

# ------------------------------------------------------------------------------ 
# Úkol 5: Práce s Weather API
# Použij Weather API (https://api.weatherapi.com/v1/current.json) a získej aktuální informace o počasí
# pro město Praha. Použij následující API klíč: 939716ed2d204c008ef151039252603
# Vypiš následující informace:
# - Název města
# - Aktuální teplotu v °C
# - Popis počasí (např. "Sunny", "Cloudy")

# URL API a parametry
url = 'https://api.weatherapi.com/v1/current.json'
params = {
    'key': '939716ed2d204c008ef151039252603',
    'q': 'Prague'
}

# Řešení:
response = requests.get(url, params=params)
data = response.json()

print(f"Město: {data['location']['name']}")
print(f"Teplota: {data['current']['temp_c']} °C")
print(f"Počasí: {data['current']['condition']['text']}")

# ------------------------------------------------------------------------------ 
# Úkol 6: Rozšíření - Uložení dat z Weather API do JSON souboru
# Rozšiř úkol 5 tak, aby získaná data o počasí byla uložena do souboru "weather.json".

# Řešení:
with open('weather.json', 'w') as file:
    json.dump(data, file, indent=4)

# ------------------------------------------------------------------------------ 
# Úkol 7: Generování HTML souboru s aktuálním počasím
# Použij Weather API (https://api.weatherapi.com/v1/current.json) a získej aktuální informace o počasí
# pro město Praha. Vygeneruj HTML soubor s názvem "weather.html", který zobrazí následující informace:
# - Název města
# - Aktuální teplotu v °C
# - Popis počasí (např. "Sunny", "Cloudy")
# - Ikonu počasí (URL ikony je dostupná v odpovědi API)

# URL API a parametry
url = 'https://api.weatherapi.com/v1/current.json'
params = {
    'key': '939716ed2d204c008ef151039252603',
    'q': 'Prague'
}

# Řešení:
import requests

# Získání dat z Weather API
response = requests.get(url, params=params)
data = response.json()

# Extrakce dat
city = data['location']['name']
temperature = data['current']['temp_c']
condition = data['current']['condition']['text']
icon_url = "https:" + data['current']['condition']['icon']

# Generování HTML obsahu
html_content = f"""
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Počasí - {city}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }}
        img {{
            width: 100px;
            height: 100px;
        }}
    </style>
</head>
<body>
    <h1>Aktuální počasí v {city}</h1>
    <p><strong>Teplota:</strong> {temperature} °C</p>
    <p><strong>Stav:</strong> {condition}</p>
    <img src="{icon_url}" alt="Ikona počasí">
</body>
</html>
"""

# Uložení HTML souboru
with open('weather.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("HTML soubor 'weather.html' byl úspěšně vygenerován.")