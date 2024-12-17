# Úkol 1:
# Načti celé číslo od uživatele.
# 1. Zkontroluj, zda je číslo kladné, záporné nebo rovno nule a vypiš odpovídající zprávu.
# 2. Pokud je číslo kladné, zjisti, zda je sudé nebo liché.
# Použij podmínky if...else a operátory ==, <, >, %.

# Řešení:
cislo = int(input("Zadej celé číslo: "))

if cislo > 0:
    print("Číslo je kladné.")
    if cislo % 2 == 0:
        print("Číslo je sudé.")
    else:
        print("Číslo je liché.")
elif cislo < 0:
    print("Číslo je záporné.")
else:
    print("Číslo je rovno nule.")


# Úkol 2:
# Načti věk uživatele a podle věku vypiš typ lístku:
# - Věk < 6: dětský lístek zdarma
# - Věk 6–18: studentský lístek
# - Věk 19–65: standardní lístek
# - Věk > 65: seniorská sleva

# Řešení:
vek = int(input("Zadej svůj věk: "))

if vek < 6:
    print("Máš dětský lístek zdarma.")
elif 6 <= vek <= 18:
    print("Máš studentský lístek.")
elif 19 <= vek <= 65:
    print("Máš standardní lístek.")
else:
    print("Máš seniorskou slevu.")


# Úkol 3:
# Načti věk uživatele a informaci o zdravotním omezení ("ano" nebo "ne").
# Vstup do zábavního parku je povolen, pokud:
# - Věk je mezi 10 a 60 lety.
# - Zdravotní omezení je "ne".
# Vypiš, zda má uživatel povolený vstup.

# Řešení:
vek = int(input("Zadej svůj věk: "))
zdravotni_omezeni = input("Máš zdravotní omezení? (ano/ne): ").lower()

if 10 <= vek <= 60 and zdravotni_omezeni == "ne":
    print("Vstup do zábavního parku je povolen.")
else:
    print("Vstup do zábavního parku není povolen.")


# Úkol 4:
# Načti kladné číslo od uživatele.
# Pomocí cyklu while spočítej součet všech čísel od 1 do tohoto čísla včetně.
# Na závěr vypiš výsledek.

# Řešení:
cislo = int(input("Zadej kladné číslo: "))
součet = 0
i = 1

while i <= cislo:
    součet += i
    i += 1

print(f"Součet čísel od 1 do {cislo} je {součet}.")


# Úkol 5:
# Načti číslo n od uživatele.
# Pomocí cyklu for vypiš čísla od 1 do n.
# Na konci cyklu vypiš zprávu: "Všechna čísla byla vypsána!"

# Řešení:
n = int(input("Zadej číslo: "))

for i in range(1, n + 1):
    print(i)
else:
    print("Všechna čísla byla vypsána!")


# Úkol 6:
# Vypiš čísla od 1 do 20.
# - Pokud je číslo násobkem 5, přeskoč ho (continue).
# - Pokud je číslo větší než 15, ukonči cyklus (break).

# Řešení:
for i in range(1, 21):
    if i > 15:
        break
    if i % 5 == 0:
        continue
    print(i)



# Úkol 7:
# Načti číslo n od uživatele.
# Vytvoř trojúhelník hvězdiček s n řádky:
# *
# **
# ***
# ****
# *****

# Řešení:
n = int(input("Zadej počet řádků: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# Úkol 8:
# Načti tři čísla od uživatele.
# Pomocí vnořených podmínek zjisti, které z čísel je největší.
# Vypiš výsledek.

# Řešení:
a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))
c = int(input("Zadej třetí číslo: "))

if a >= b:
    if a >= c:
        print(f"Největší číslo je {a}.")
    else:
        print(f"Největší číslo je {c}.")
else:
    if b >= c:
        print(f"Největší číslo je {b}.")
    else:
        print(f"Největší číslo je {c}.")
