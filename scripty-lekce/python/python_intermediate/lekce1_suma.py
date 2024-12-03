count = int(input("Zadej počet vstupů pro výpočet sumy... "))
total = 0
for index in range(count):
    entry_number = int(input("Zadej číslo do sumy... "))
    total = total + entry_number
print("Suma zadaných čísel je: " + str(total))