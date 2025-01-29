hour = int(input("Zadej počet hodin: "))
min =  int(input("Zadej počet minut: "))
sec =  int(input("Zadej počet sekund: "))

result = sec + hour * 60 * 60 + min * 60

print(f"Stanovený čas v sekundách je: {result}")

input()