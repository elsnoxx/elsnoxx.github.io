import requests
import json
import os
import time

def get_joke():
    """
    Získá náhodný vtip z API
    """
    # TODO: Odešli GET požadavek na API https://official-joke-api.appspot.com/random_joke
    # a vrať vtip ve formátu {"setup": "...", "punchline": "..."}
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        joke = {
            "setup": data["setup"],
            "punchline": data["punchline"]
        }
        return joke
    else:
        return {"error": "Vtip nenalezen"}
    # Doplň svůj kód

def get_fact():
    """
    Získá náhodný zajímavý fakt z API
    """
    # TODO: Odešli GET požadavek na API https://uselessfacts.jsph.pl/random.json?language=en
    # a vrať fakt ve formátu {"text": "..."}
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        fact = {
            "text": data["text"]
        }
        return fact
    else:
        return {"error": "Fakt nenalezen"}
    

def get_country_info(country_name):
    """
    Získá informace o zemi
    """
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()[0]  # Bereme první výsledek
        return {
            "name": data["name"]["common"],
            "capital": data.get("capital", ["Neznámé"])[0],
            "population": data["population"],
            "area": data.get("area", "Neznámé"),
            "region": data["region"],
            "flag": data["flags"]["png"]
        }
    else:
        return {"error": f"Země '{country_name}' nenalezena"}


# Hlavní menu
def main():
    print("==== GENERÁTOR VTIPŮ A ZAJÍMAVOSTÍ ====")
    print("Vítej v aplikaci, která ti ukáže vtipy a zajímavé fakty!")
    
    
    while True:
        print("\nCo chceš dělat?")
        print("1. Zobrazit náhodný vtip")
        print("2. Zobrazit náhodný zajímavý fakt")
        print("3. Vyhledat informace o zemi")
        print("4. Konec")
        
        choice = input("Tvoje volba (1-7): ")
        
        # TODO: Zpracuj volbu uživatele a zavolej příslušné funkce
        if choice == "1":
            joke = get_joke()
            if "error" in joke:
                print(joke["error"])
            else:
                print(f"{joke['setup']} - {joke['punchline']}")
        elif choice == "2":
            fact = get_fact()
            if "error" in fact:
                print(fact["error"])
            else:
                print(f"Zajímavý fakt: {fact['text']}")
        elif choice == "3":
            country_name = input("Zadej název země: ")
            country_info = get_country_info(country_name)
            if "error" in country_info:
                print(country_info["error"])
            else:
                print(f"Název: {country_info['name']}")
                print(f"Hlavní město: {country_info['capital']}")
                print(f"Populace: {country_info['population']}")
                print(f"Rozloha: {country_info['area']} km²")
                print(f"Region: {country_info['region']}")
                print(f"Vlajka: {country_info['flag']}")
        elif choice == "4":
            print("Děkujeme za použití aplikace!")
            break
        
        # Doplň svůj kód

# Spuštění hlavního programu
if __name__ == "__main__":
    main()