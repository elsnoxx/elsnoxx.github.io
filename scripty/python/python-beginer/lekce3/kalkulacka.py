
while True:
    a = input("zadej prvni cislo: ")
    b = input("zadej druhe cislo: ")
    znak = input("Zadej operaci: ")
    if (a == "q" or b == "q" or znak == "q"):
        break
    

    a = int(a)
    b = int(b)

    if (znak == "+"):
        print(a + b)
    if (znak == "-"):
        print(a - b)
    if (znak == "*"):
        print(a * b)
    if (znak == "/"):
        print(float(a) / float(b))
    