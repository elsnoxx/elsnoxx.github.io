
count = int(input("Zadej počet vstupů pro výpočet sumy... "))
total = 0
for index in range(count):
    entry_number = int(input("Zadej číslo do sumy... "))
    total = total + entry_number
    average = total / count
print("Suma zadaných čísel je: " + str(total))
print("Průměr zadaných čísel je: " + str(average))