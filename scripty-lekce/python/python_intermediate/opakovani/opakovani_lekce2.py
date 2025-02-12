# 1. Sečtení všech čísel v seznamu
seznam = [1, 2, 3, 4, 5]
soucet = sum(seznam)
print(f"Součet čísel v seznamu je: {soucet}")

# 2. Načti jméno uživatele a pozdrav ho
jmeno = input("Zadej své jméno: ")
print(f"Ahoj, {jmeno}!")

# 3. Převod stupňů Celsia na Fahrenheity
c = float(input("Zadej teplotu ve stupních Celsia: "))
f = c * 9/5 + 32
print(f"{c}°C je {f}°F")

# 4. Rozhodni, zda číslo je kladné, záporné nebo nula
cislo = float(input("Zadej číslo: "))
if cislo > 0:
    print("Číslo je kladné.")
elif cislo < 0:
    print("Číslo je záporné.")
else:
    print("Číslo je nula.")

# 5. Nakresli obdélník ze znaků hvězdiček
sirka = int(input("Zadej šířku obdélníku: "))
vyska = int(input("Zadej výšku obdélníku: "))

for i in range(vyska):
    print("*" * sirka)
