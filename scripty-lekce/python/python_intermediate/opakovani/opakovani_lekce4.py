# 1. Úkol: Vytvoř náhodné číslo a zjisti, jestli je sudé nebo liché.
# Použij knihovnu random pro generování čísla.

import random

number = random.randint(1, 100)
if number % 2 == 0:
    print(f"{number} je sudé.")
else:
    print(f"{number} je liché.")


# 2. Úkol: Pomocí knihovny colorama zbarvi text do jedné z barev podle náhody.
# Použij funkci random pro výběr barvy.

from colorama import Fore
import random

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
random_color = random.choice(colors)
print(random_color + "Toto je náhodně zbarvený text!")


# 3. Úkol: Změř čas, jak dlouho trvá generování náhodného čísla (použij time).
# Vyzkoušej generování náhodného čísla 10 000krát.

import time

start_time = time.time()
for i in range(10000):
    i = random.randint(1, 100)
end_time = time.time()

print(f"Generování náhodných čísel trvalo {end_time - start_time} sekund.")


# 4. Úkol: Napiš program, který bude generovat náhodná písmena (od A do Z) po dobu 5 sekund.
# Použij knihovnu random pro výběr písmen a time pro zajištění časového omezení.

import random
import time

start_time = time.time()
while time.time() - start_time < 5:
    letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print(letter, end=" ", flush=True)

print("\nKonec generování písmen.")


# 5. Úkol: Vytvoř program, který náhodně zvolí, jestli uživatel vyhraje nebo prohraje.
# Použij random pro výběr výsledku a colorama pro barevné zobrazení.

import random
from colorama import Fore

result = random.choice(["win", "lose"])
if result == "win":
    print(Fore.GREEN + "Vyhráls!")
else:
    print(Fore.RED + "Prohrál jsi!")
