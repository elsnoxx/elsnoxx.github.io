import random

# Seznam slov pro hádání
slova = ["python", "programování", "datová", "analýza", "umělá", "inteligence", "strojové", "učení"]

# Náhodný výběr slova
slovo = random.choice(slova)

# Seznam písmen, která byla uhodnuta
uhodnuta_pismena = []

# Seznam písmen, která byla chybně hádaná
chybna_pismena = []

# Počet chyb
pocet_chyb = 0

# Hlavní smyčka hry
while True:
    # Vytiskne slovo s uhodnutými písmeny
    hadane_slovo = ""
    for pismeno in slovo:
        if pismeno in uhodnuta_pismena:
            hadane_slovo += pismeno + " "
        else:
            hadane_slovo += "_ "
    print("Hádané slovo:", hadane_slovo)
    
    # Zkontroluje, zda hráč vyhrál
    if all(pismeno in uhodnuta_pismena for pismeno in slovo):
        print("Gratuluji, uhodl jsi slovo:", slovo)
        break
    
    # Zkontroluje, zda hráč prohrál
    if pocet_chyb >= len(slovo) * 2:
        print("Bohužel, prohrál jsi. Hledané slovo bylo:", slovo)
        break
    
    # Získání hádaného písmene od hráče
    hadane_pismeno = input("Zadej hádané písmeno: ").lower()
    
    # Kontrola, zda bylo písmeno již hádané
    if hadane_pismeno in uhodnuta_pismena or hadane_pismeno in chybna_pismena:
        print("Toto písmeno jsi již hádal.")
        continue
    
    # Kontrola, zda bylo hádané písmeno správně
    if hadane_pismeno in slovo:
        print("Správně!")
        uhodnuta_pismena.append(hadane_pismeno)
    else:
        print("Špatně!")
        chybna_pismena.append(hadane_pismeno)
        pocet_chyb += 1
