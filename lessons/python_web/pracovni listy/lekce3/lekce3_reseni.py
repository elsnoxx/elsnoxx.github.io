# Pracovní list: Tuples, Sets, Dictionaries, Search a Sort

# ------------------------------------------------------------------------------
# 1. Tuples

# Úkol 1
# Vytvoř tuple, který obsahuje tři jména. Jak přistoupíš k druhému jménu?
tuple_names = ("Alice", "Bob", "Charlie")
second_name = tuple_names[1]
print(second_name)

# Úkol 2
# Vytvoř tuple obsahující názvy tří měst. Jak zjistíš, zda město "Praha" je v tomto tuple?
cities = ("Brno", "Praha", "Ostrava")
is_praha_in_tuple = "Praha" in cities
print(is_praha_in_tuple)

# Úkol 3: Rozbalení tuple
# Máš tuple obsahující tři hodnoty: ("Alice", 25, "Praha"). Jak rozbalíš tento tuple do tří proměnných?
person = ("Alice", 25, "Praha")
name, age, city = person  # Rozbalení tuple
print(f"Jméno: {name}, Věk: {age}, Město: {city}")

# Úkol 4: Výměna hodnot pomocí tuple
# Máš dvě proměnné a = 5 a b = 10. Jak prohodíš jejich hodnoty bez použití třetí proměnné?
a = 5
b = 10
a, b = b, a
print(f"a: {a}, b: {b}")

# Úkol 5: Iterace přes tuple
# Máš tuple obsahující názvy měst: ("Brno", "Praha", "Ostrava"). Jak vypíšeš každé město na nový řádek?
cities = ("Brno", "Praha", "Ostrava")
for city in cities:
    print(city)

# Úkol 6: Zanořené tuple
# Máš tuple obsahující informace o osobách: (("Alice", 25), ("Bob", 30), ("Charlie", 22)).
# Jak získáš věk osoby jménem "Bob"?
people = (("Alice", 25), ("Bob", 30), ("Charlie", 22))
for person in people:
    if person[0] == "Bob":
        print(f"Bobův věk je {person[1]}")

# Hra: Uhádni hlavní město.
# Hráč hádá hlavní město podle zadaného státu. Pokud uhodne správně, vyhraje.
# Pokud ne, ukáže se správné hlavní město.

import random

# Tuple obsahující dvojice (stát, hlavní město)
staty_a_mesta = (
    ("Česká republika", "Praha"),
    ("Slovensko", "Bratislava"),
    ("Německo", "Berlín"),
    ("Francie", "Paříž"),
    ("Španělsko", "Madrid"),
    ("Itálie", "Řím"),
    ("USA", "Washington"),
    ("Kanada", "Ottawa"),
    ("Japonsko", "Tokio"),
    ("Austrálie", "Canberra"),
    ("Rusko", "Moskva"),
    ("Čína", "Peking"),
    ("Indie", "Nové Dillí"),
    ("Brazílie", "Brasília"),
    ("Mexiko", "Mexiko"),
    ("Argentina", "Buenos Aires"),
    ("Jihoafrická republika", "Pretoria"),
    ("Egypt", "Káhira"),
    ("Turecko", "Ankara"),
    ("Řecko", "Atény"),
    ("Švédsko", "Stockholm"),
    ("Norsko", "Oslo"),
    ("Finsko", "Helsinky"),
    ("Dánsko", "Kodaň"),
    ("Polsko", "Varšava"),
    ("Rakousko", "Vídeň"),
    ("Maďarsko", "Budapešť"),
    ("Švýcarsko", "Bern"),
    ("Portugalsko", "Lisabon"),
    ("Nizozemsko", "Amsterdam"),
    ("Belgie", "Brusel"),
    ("Ukrajina", "Kyjev"),
    ("Vietnam", "Hanoj"),
    ("Thajsko", "Bangkok"),
    ("Indonésie", "Jakarta"),
    ("Nový Zéland", "Wellington"),
    ("Saúdská Arábie", "Rijád"),
    ("Izrael", "Jeruzalém"),
    ("Jižní Korea", "Soul"),
    ("Severní Korea", "Pchjongjang")
)


pocet_kol = 5
body = 0

print("🌍 Vítej ve hře 'Najdi správné hlavní město'!\n")

for _ in range(pocet_kol):
    # Náhodně vyber stát z tuple
    stat, spravne_mesto = random.choice(staty_a_mesta)

    # Hráč zadává odpověď
    odpoved = input(f"👉 Jaké je hlavní město státu {stat}? ").strip()

    if odpoved.lower() == spravne_mesto.lower():
        print("✅ Správně! Získáváš bod! 🎉\n")
        body += 1
    else:
        print(f"❌ Špatně. Správná odpověď je: {spravne_mesto}.\n")

# Výsledek hry
print(f"🏆 Hra skončila! Získal jsi {body}/{pocet_kol} bodů.")



# ------------------------------------------------------------------------------
# 2. Sets

# Úkol 1
# Vytvoř set s několika čísly. Jak ověříš, zda číslo 5 je v tomto setu?
numbers_set = {1, 2, 3, 4, 5, 6}
is_five_in_set = 5 in numbers_set
print(is_five_in_set)

# Úkol 2
# Vytvoř set obsahující názvy zvířat. Přidej do tohoto setu nové zvíře "kočka".
animals = {"pes", "králík", "had"}
animals.add("kočka")
print(animals)

# Úkol 3: Operace na setech
# Máš dva sety: {1, 2, 3, 4} a {3, 4, 5, 6}. Jak zjistíš jejich průnik (společné prvky)?
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1 & set2
print(intersection)

# Úkol 4: Odstranění prvku ze setu
# Máš set {1, 2, 3, 4, 5}. Jak odstraníš číslo 3?
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)  # Změňte podle zadání
print(numbers)

# Úkol 5: Převod seznamu na set
# Máš seznam [1, 2, 2, 3, 4, 4, 5]. Jak vytvoříš set, který obsahuje pouze unikátní hodnoty?
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)  # Změňte podle zadání
print(unique_numbers)

# Úkol 6: Spojení dvou setů
# Máš dva sety: {1, 2, 3} a {4, 5, 6}. Jak vytvoříš nový set, který obsahuje všechny prvky z obou setů?
set_a = {1, 2, 3}
set_b = {4, 5, 6}
union_set = set_a | set_b  # Spojení setů
print(union_set)

# Úkol 7: Generování setu z řetězce
# Máš řetězec "abrakadabra". Jak vytvoříš set obsahující unikátní znaky z tohoto řetězce?
string = "abrakadabra"
unique_chars = set(string)  # Unikátní znaky
print(unique_chars)

# Úkol 8: Set z číselného rozsahu
# Jak vytvoříš set obsahující všechna sudá čísla od 1 do 10?
even_numbers = {x for x in range(1, 11) if x % 2 == 0}
print(even_numbers)

# Hra: Najdi unikátní slova!
# Najdi unikátní slova ve větě a zjisti, kolik jich je.
# Hráč hádá počet unikátních slov ve větě.
# Pokud uhodne správně, vyhraje. Pokud ne, ukáže se správný počet.
# Hra je založena na náhodně vybrané větě z předem definovaného seznamu vět.
# Hráč zadá svůj tip a program porovná s počtem unikátních slov ve větě.
import random
import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

vety = [
    "Python je skvělý a mocný programovací jazyk",
    "Hraní her v Pythonu je zábava",
    "Sety jsou užitečné pro odstranění duplicit",
    "Hledání unikátních slov je skvělý trénink",
    "Programování je dovednost, která se dá naučit",
    "Opakování je matka moudrosti",
    "Chyby jsou součástí učení, každý programátor je dělá",
    "Nejlepší způsob jak se naučit programovat je psát kód",
    "Python je interpretovaný jazyk s jednoduchou syntaxí",
    "Algoritmy a datové struktury jsou klíčem k efektivnímu kódu",
    "Verzování kódu pomocí GitHubu je užitečné pro spolupráci",
    "Každý programátor by měl znát alespoň jeden objektově orientovaný jazyk",
    "Čtení cizího kódu je stejně důležité jako jeho psaní",
    "Komentování kódu pomáhá ostatním i tobě v budoucnu",
    "Refaktoring kódu zlepšuje jeho čitelnost a efektivitu"
]


veta = random.choice(vety)

slova = veta.lower().replace(",", "").replace(".", "").split()
unikatni_slova = set(slova)

print("📝 Věta:", veta)
spravny_pocet = len(unikatni_slova)
time.sleep(1)
clear_console()

while True:
    try:
        tip = int(input("👉 Kolik unikátních slov obsahuje tato věta? "))
        if tip == spravny_pocet:
            print("🎉 Skvělé! Uhodl jsi správně!")
            break
        elif tip < spravny_pocet:
            print("❌ Ne, zkus to znovu. Zkus větší číslo.")
        elif tip > spravny_pocet:
            print("❌ Ne, zkus to znovu. Zkus menší číslo.")
    except ValueError:
        print("❌ Prosím zadejte platné číslo.")
        clear_console()


print("🔍 Unikátní slova:", unikatni_slova)


# ------------------------------------------------------------------------------
# 3. Dictionaries

# Úkol 1
# Vytvoř slovník, kde klíčem bude jméno a hodnotou věk. Jak získáš věk osoby jménem "Petr"?
people_ages = {"Anna": 22, "Petr": 30, "Eva": 19}
petr_age = people_ages.get("Petr")
print(petr_age)

# Úkol 2
# Vytvoř set obsahující názvy zvířat. Přidej do tohoto setu nové zvíře "kočka".
animals = {"pes", "králík", "had"}
animals.add("kočka")
print(animals)

# Úkol 3: Práce s hodnotami v dictionary
# Máš slovník {"jablko": 10, "banán": 5, "pomeranč": 8}. Jak zvýšíš počet jablek o 3?
fruits = {"jablko": 10, "banán": 5, "pomeranč": 8}
fruits["jablko"] += 3
print(fruits)

# Úkol 4: Iterace přes dictionary
# Máš slovník {"Anna": 22, "Petr": 30, "Eva": 19}. Jak vypíšeš všechny klíče a hodnoty?
people_ages = {"Anna": 22, "Petr": 30, "Eva": 19}
for name, age in people_ages.items():
    print(f"{name} má {age} let")

# Úkol 5: Získání hodnoty z dictionary s výchozí hodnotou
# Máš slovník {"auto": "BMW", "barva": "červená"}. Jak získáš hodnotu pro klíč "model", pokud neexistuje?
car = {"auto": "BMW", "barva": "červená"}
model = car.get("model", "neznámý")  # Změňte podle zadání
print(model)

# Úkol 6: Zanořené dictionaries
# Vytvoř slovník, kde klíčem bude jméno a hodnotou další slovník obsahující věk a město.
# Jak získáš město osoby jménem "Eva"?
nested_dict = {
    "Anna": {"věk": 22, "město": "Praha"},
    "Petr": {"věk": 30, "město": "Brno"},
    "Eva": {"věk": 19, "město": "Ostrava"}
}
eva_city = nested_dict["Eva"]["město"]
print(eva_city)

# Hra: Duolingo
#  Program vypíše náhodné české slovo a hráč musí napsat jeho anglický překlad.
# Pokud hráč odpoví správně, získá bod. Pokud ne, program mu ukáže správný překlad.
# Hráč může kdykoliv napsat "konec" a hra se ukončí.

# Slovník českých slov a jejich anglických překladů
prekladac = {
    "pes": "dog",
    "kočka": "cat",
    "dům": "house",
    "auto": "car",
    "škola": "school",
    "učitel": "teacher",
    "stůl": "table",
    "židle": "chair",
    "slunce": "sun",
    "měsíc": "moon",
    "voda": "water",
    "jídlo": "food",
    "přítel": "friend",
    "rodina": "family",
    "práce": "work",
    "kniha": "book",
    "telefon": "phone",
    "počítač": "computer",
    "okno": "window",
    "dveře": "door",
    "čas": "time",
    "den": "day",
    "noc": "night",
    "město": "city",
    "vesnice": "village",
    "cesta": "road",
    "letadlo": "plane",
    "vlak": "train",
    "loď": "ship",
    "ruka": "hand",
    "oko": "eye",
    "hlava": "head",
    "srdce": "heart",
    "moře": "sea",
    "hora": "mountain",
    "strom": "tree",
    "květina": "flower",
    "jablko": "apple",
    "banán": "banana",
    "chléb": "bread",
    "mléko": "milk",
    "sýr": "cheese",
    "cukr": "sugar",
    "sůl": "salt",
    "vítr": "wind",
    "déšť": "rain",
    "sníh": "snow",
    "led": "ice",
    "oheň": "fire",
    "země": "earth",
    "vzduch": "air"
}


print("📝 Vítej ve hře Překladač CZ → EN!")
print("🔠 Napiš anglický překlad zobrazeného českého slova.")
print("✏️ Pokud chceš hru ukončit, napiš 'konec'.\n")

while True:
    ceske_slovo = random.choice(list(prekladac.keys()))  # Náhodné české slovo
    spravny_preklad = prekladac[ceske_slovo]  # Správný anglický překlad

    odpoved = input(f"👉 Jak se přeloží '{ceske_slovo}' do angličtiny? ").strip().lower()

    if odpoved == "konec":
        print("👋 Děkujeme za hraní! Měj hezký den!")
        break

    if odpoved == spravny_preklad:
        print("🎉 Správně!\n")
    else:
        print(f"❌ Špatně. Správná odpověď je: {spravny_preklad}\n")


# ------------------------------------------------------------------------------ 
# 4. Hledání (Search)

# Úkol 1: Základní hledání
# V seznamu [3, 7, 2, 9, 4] najdi, zda obsahuje číslo 9. Jaký způsob použiješ?
numbers_list = [3, 7, 2, 9, 4]
is_nine_present = 9 in numbers_list  # Použití operátoru "in"
print(f"Obsahuje seznam číslo 9? {is_nine_present}")

# Úkol 2: Najdi index čísla
# Jak zjistíš index čísla 9 v seznamu?
if is_nine_present:
    index_of_nine = numbers_list.index(9)  # Získání indexu
    print(f"Číslo 9 je na indexu {index_of_nine}")

# Úkol 3: Hledání více čísel
# Jak zjistíš, zda seznam obsahuje všechna čísla z [2, 9]?
search_numbers = [2, 9]
contains_all = all(num in numbers_list for num in search_numbers)  # Použití "all"
print(f"Obsahuje seznam všechna čísla {search_numbers}? {contains_all}")

# Úkol 4: Hledání prvního sudého čísla
# Najdi první sudé číslo v seznamu [3, 7, 2, 9, 4].
first_even = next((num for num in numbers_list if num % 2 == 0), None)  # Použití "next"
print(f"První sudé číslo v seznamu je: {first_even}")

# ------------------------------------------------------------------------------ 
# 7. Třídění (Sort)

# Úkol 1: Seřaď seznam čísel vzestupně
unsorted_numbers = [8, 3, 1, 5, 2]
unsorted_numbers.sort()  # Třídění na místě
print(f"Seřazený seznam (vzestupně): {unsorted_numbers}")

# Úkol 2: Seřaď seznam čísel sestupně
unsorted_numbers = [8, 3, 1, 5, 2]
sorted_desc = sorted(unsorted_numbers, reverse=True)  # Třídění do nového seznamu
print(f"Seřazený seznam (sestupně): {sorted_desc}")

# Úkol 3: Třídění seznamu řetězců podle délky
words = ["Python", "je", "skvělý", "jazyk"]
words.sort(key=len)  # Třídění podle délky řetězců
print(f"Seřazený seznam podle délky: {words}")