import random

print("Hra se načítá a generuje se náhodné číslo k hádání.")
hadane_cislo = random.randint(0, 10)
print("Hotovo. Hra začíná.")

pokusy = 0  # Počet pokusů hráče

while pokusy < 3:  # Hráč má tři pokusy
    vstup = int(input("Zadej číslo: "))
    
    if vstup == hadane_cislo:
        print("Vyhrál jsi! Hádané číslo je {0}".format(hadane_cislo))
        break
    else:
        pokusy += 1
        if vstup > hadane_cislo:
            print("Špatně, hádané číslo je menší.")
        else:
            print("Špatně, hádané číslo je větší.")

if pokusy == 3:
    print("Prohrál jsi! Hádané číslo bylo:", hadane_cislo)
