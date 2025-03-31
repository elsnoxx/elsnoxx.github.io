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

# Tvůj kód zde:


# ------------------------------------------------------------------------------ 
# Úkol 2: Zápis do JSON souboru
# Vytvoř Python slovník s následujícími daty:
# {
#     "product": "Notebook",
#     "price": 1500,
#     "in_stock": True
# }
# Ulož tento slovník do souboru s názvem "product.json" ve formátu JSON.

# Tvůj kód zde:


# ------------------------------------------------------------------------------ 
# Úkol 3: Základní GET požadavek
# Použij knihovnu `requests` a odešli GET požadavek na následující URL:
# https://jsonplaceholder.typicode.com/posts/1
# Získaná data vypiš ve formátu JSON a zobraz hodnoty klíčů "title" a "body".

import requests

# Tvůj kód zde:


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

# Tvůj kód zde:


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

# Tvůj kód zde:


# ------------------------------------------------------------------------------ 
# Úkol 6: Rozšíření - Uložení dat z Weather API do JSON souboru
# Rozšiř úkol 5 tak, aby získaná data o počasí byla uložena do souboru "weather.json".

# Tvůj kód zde:



# ------------------------------------------------------------------------------ 
# Úkol 7: Generování HTML souboru s aktuálním počasím
# Použij Weather API (https://api.weatherapi.com/v1/current.json) a získej aktuální informace o počasí
# pro město Praha. Vygeneruj HTML soubor s názvem "weather.html", který zobrazí následující informace:
# - Název města
# - Aktuální teplotu v °C
# - Popis počasí (např. "Sunny", "Cloudy")
# - Ikonu počasí (URL ikony je dostupná v odpovědi API)