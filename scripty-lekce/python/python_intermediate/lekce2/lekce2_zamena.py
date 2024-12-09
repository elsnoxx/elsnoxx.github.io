first_number = int(input("Zadej první číslo..."))
second_number = int(input("Zadej druhé číslo..."))
temporary_number = second_number
second_number = first_number
first_number = temporary_number
print("Nyní vypíšeme čísla po jejich prohození.")
print(f"Toto je nyní první číslo: {first_number}")
print(f"Toto je nyní druhé číslo: {second_number}")