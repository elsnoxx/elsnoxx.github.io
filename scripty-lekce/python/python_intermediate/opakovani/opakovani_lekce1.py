# Úkol 1: Záměna dvou hodnot

a = 5
b = 10
print("Před záměnou:", a, b)
temp = a
a = b
b = temp
print("Po záměně:", a, b)

# Úkol 2: Kontrola sudého nebo lichého čísla

cislo = int(input("Zadejte číslo: "))
if cislo % 2 == 0:
    print("Číslo je sudé.")
else:
    print("Číslo je liché.")

# Úkol 3: Výpis prvků seznamu

fruits = ["jablko", "banán", "pomeranč"]
for item in fruits:
    print(item)

# Úkol 4: Trojúhelník hvězdiček

n = int(input("Zadejte počet řádků: "))
for i in range(1, n+1):
    print('*' * i)

# Úkol 5: Typ lístku podle věku

vek = int(input("Zadejte svůj věk: "))
if vek < 18:
    print("Dětský lístek")
else:
    print("Dospělý lístek")
