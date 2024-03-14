cislo1 = int(input("Zadej první číslo: "))
cislo2 = int(input("Zadej druhé číslo: "))
print("Mo+zn0 operace jsou: +, - , *, /, //, % ")
operace = input("Zadej operaci, kterou chceš vypočítat: ")



if operace == "+":
    soucet = cislo1 + cislo2
    print("Součet: ",soucet)
elif operace == "-":
    rozdil = cislo1 - cislo2
    print("Rozdíl: ",rozdil)
elif operace == "*":
    nasobeni = cislo1 * cislo2
    print("Násobení: ",nasobeni)
elif operace == "/":
    deleni = cislo1 / cislo2
    print("Dělení: ",deleni)
elif operace == "//":
    celo_deleni = cislo1 // cislo2
    print("Celočíselné dělení: ",celo_deleni)
elif operace == "%":
    modulo = cislo1 % cislo2
    print("Modulo: ",modulo)












