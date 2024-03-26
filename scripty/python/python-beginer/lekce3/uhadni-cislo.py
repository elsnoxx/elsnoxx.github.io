import random

print("Hra se načítá a generuje se nahodne číslo, k hádání.")
hadaneCislo = random.randint(0, 10)
print("Hotovo. Hra začíná.")
while True:
    vstup = int(input("Zadej číslo: "))
    if vstup == hadaneCislo:
        print("Vyhrál jsi hádané číslo je {0}".format(hadaneCislo))
    else:
        if vstup > hadaneCislo:
            print("Špatně hádané číslo je menší.")

        else:
            print("Špatně hádané číslo je větší.")
