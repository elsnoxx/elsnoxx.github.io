import random

# Počet náhodných čísel
count = int(input("Kolik náhodných čísel chcete vygenerovat? "))

# Interval pro generování čísel
lower_limit = int(input("Zadejte dolní mez intervalu: "))
upper_limit = int(input("Zadejte horní mez intervalu: "))

# Název souboru
filename = input("Zadejte název souboru (včetně přípony, např. 'random_numbers.txt'): ")

# Generování náhodných čísel
random_numbers = []
for _ in range(count):
    random_number = random.randint(lower_limit, upper_limit)
    random_numbers.append(random_number)

# Otevření souboru pro zápis a uložení náhodných čísel
with open(filename, mode="w", encoding="utf-8") as file:
    for number in random_numbers:
        file.write(f"{number}\n")

print(f"Náhodná čísla byla zapsána do souboru {filename}.")
