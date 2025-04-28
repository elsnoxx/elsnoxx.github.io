import requests
from datetime import datetime

def get_iss_position():
    url = "http://api.open-notify.org/iss-now.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["message"] == "success":
            timestamp = data["timestamp"]
            dt = datetime.fromtimestamp(timestamp)
            latitude = data["iss_position"]["latitude"]
            longitude = data["iss_position"]["longitude"]
            print(f"\nAktuální poloha ISS:")
            print(f"Čas: {dt.strftime('%d.%m.%Y %H:%M:%S')}")
            print(f"Zeměpisná šířka: {latitude}")
            print(f"Zeměpisná délka: {longitude}\n")
        else:
            print("Chyba při získávání dat o ISS.")
    except Exception as e:
        print(f"Chyba: {e}")

def get_people_in_space():
    url = "http://api.open-notify.org/astros.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["message"] == "success":
            print(f"\nLidé aktuálně ve vesmíru ({data['number']}):")
            for person in data["people"]:
                print(f"- {person['name']} ({person['craft']})")
            print()
        else:
            print("Chyba při získávání seznamu osob ve vesmíru.")
    except Exception as e:
        print(f"Chyba: {e}")

def main():
    while True:
        print("Vyber možnost:")
        print("1. Zobrazit aktuální polohu ISS")
        print("2. Vypsat osoby ve vesmíru")
        print("3. Konec")
        choice = input("Zadej volbu (1-3): ").strip()
        if choice == "1":
            get_iss_position()
        elif choice == "2":
            get_people_in_space()
        elif choice == "3":
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba, zkus to znovu.\n")

if __name__ == "__main__":
    main()