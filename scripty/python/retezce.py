a = "hallo"

# demontrace retezce
print(a)

print()

print(list(a))

print()

print(len(a))

print()

print(a[1])

print()

for i in a:
    print(i)

# metody

# metoda vyhledat
print(str(a.find("a")))
print(str(a.find("l")))

# metoda nahradit
a = "Ahoj, jmenuji se Richard a jsem lektorem v Itstep"
print(a)
a = a.replace("Richard","Tom")
print(a)

import datetime
now = []
now = datetime.datetime.now()

print(now)
print(now)