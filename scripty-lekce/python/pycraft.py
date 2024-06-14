import time

# Spustíme stopky
start = time.time()

# Cyklus, který chceme měřit
for i in range(100000):
    print(i)

# Zastavíme stopky
konec = time.time()

# Spočítáme, jak dlouho cyklus běžel
vysledny_cas = konec - start

# Převod času na sekundy
print("Cyklus běžel:", vysledny_cas, "sekund")