# Řešení úkolu 1
with open("test_soubor.txt", "w") as soubor:
    soubor.write("Toto je testovací soubor.")

with open("test_soubor.txt", "r") as soubor:
    obsah = soubor.read()
    print("Obsah souboru:", obsah)


# Řešení úkolu 2
from colorama import Fore, Style

print(Fore.GREEN + "Toto je zelený text." + Style.RESET_ALL)
print(Fore.RED + "Toto je červený text." + Style.RESET_ALL)


# Řešení úkolu 3
with open("suda_cisla.txt", "w") as soubor:
    for cislo in range(1, 51):
        if cislo % 2 == 0:
            soubor.write(f"{cislo}\n")
print("Sudá čísla byla zapsána do souboru 'suda_cisla.txt'.")


# Řešení úkolu 4: Porovnání dvou textů
text1 = input("Zadej první text: ")
text2 = input("Zadej druhý text: ")

if text1 == text2:
    print("Texty jsou stejné.")
else:
    print("Texty se liší.")



# Řešení úkolu 5
import random

seznam = [random.randint(1, 100) for _ in range(10)]
print("Generovaný seznam:", seznam)
print("Součet čísel:", sum(seznam))
