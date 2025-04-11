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
    
    # Doplň svůj kód zde:
    # 1. Vytvoř URL pro API
    # 2. Použij requests.get() pro odeslání požadavku
    # 3. Převeď odpověď na JSON pomocí response.json()
    # 4. Zkontroluj, zda byl požadavek úspěšný (status_code == 200)
    # 5. Vrať slovník s klíči "setup" a "punchline"
    # 6. Pokud dojde k chybě, vrať slovník {"error": "Vtip nenalezen"}

def get_fact():
    """
    Získá náhodný zajímavý fakt z API
    """
    # TODO: Odešli GET požadavek na API https://uselessfacts.jsph.pl/random.json?language=en
    # a vrať fakt ve formátu {"text": "..."}
    
    # Doplň svůj kód zde:
    # 1. Vytvoř URL pro API
    # 2. Použij requests.get() pro odeslání požadavku
    # 3. Převeď odpověď na JSON
    # 4. Zkontroluj, zda byl požadavek úspěšný
    # 5. Vrať slovník s klíčem "text" obsahujícím zajímavý fakt
    # 6. Pokud dojde k chybě, vrať slovník {"error": "Fakt nenalezen"}

def get_country_info(country_name):
    """
    Získá informace o zemi
    """
    # TODO: Odešli GET požadavek na API https://restcountries.com/v3.1/name/{country_name}
    # a vrať informace o zemi
    
    # Doplň svůj kód zde:
    # 1. Vytvoř URL pro API s použitím zadaného názvu země
    # 2. Použij requests.get() pro odeslání požadavku
    # 3. Zkontroluj, zda byl požadavek úspěšný
    # 4. Z odpovědi získej následující informace:
    #    - name: data["name"]["common"]
    #    - capital: data.get("capital", ["Neznámé"])[0]
    #    - population: data["population"]
    #    - area: data.get("area", "Neznámé")
    #    - region: data["region"]
    #    - flag: data["flags"]["png"]
    # 5. Vrať tyto informace jako slovník
    # 6. Pokud dojde k chybě, vrať slovník {"error": "Země '{country_name}' nenalezena"}

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
        
        choice = input("Tvoje volba (1-4): ")
        
        # TODO: Zpracuj volbu uživatele a zavolej příslušné funkce
        # Doplň svůj kód zde:
        # - Pro volbu "1": Zavolej funkci get_joke() a zobraz vtip
        # - Pro volbu "2": Zavolej funkci get_fact() a zobraz zajímavý fakt
        # - Pro volbu "3": Zeptej se uživatele na název země, zavolej funkci get_country_info() a zobraz informace
        # - Pro volbu "4": Ukonči program (break)
        # - Pro jiné volby: Informuj uživatele o neplatné volbě

# Spuštění hlavního programu
if __name__ == "__main__":
    main()