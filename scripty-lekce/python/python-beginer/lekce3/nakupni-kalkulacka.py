import math


print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

cenaBanany = 60.8
cenaJablka = 40.9

print("Menu ovoce")
print("1 - pro výběr JABLKA")
print("2 - pro výběr BANÁNŮ")
ovoce = int(input("Vyber ovoce z menu zadej jeho cislo: "))
gramm = int(input("Zadejte hmotnost (v gr.): "))
kg = gramm / 1000
print("Navážené množství je: {0} kg".format(kg))

if ovoce == 1:
    total = kg * cenaJablka
    total = math.ceil(total)
    print("K platbe za jablka: {0} Kč".format(total))
if ovoce == 2:
    total = kg * cenaBanany
    total = math.ceil(total)
    print("K platbe za banány: {0} Kč".format(total))

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")