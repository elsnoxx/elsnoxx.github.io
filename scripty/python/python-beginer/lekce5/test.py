import random
import string

list = []
for i in range(20):
    list.append(random.randint(0,10))
print("Vygenerované random čísla - {}".format(list))

list[1] = 100
list[5] = 200
list[10] = 300
list[15] = 400

print("Úkol [1] - {}".format(list))


list.remove(100)
list.remove(200)
list.remove(300)
list.remove(400)
print("Úkol [2] - {}".format(list))

novy = list[5:15]
print("Úkol [3] - {}".format(novy))

text = []
for i in range(10):
    nahodne_pismeno = random.choice(string.ascii_lowercase)
    text.append(nahodne_pismeno)
print("Vygenerované random písmena - {}".format(text))
text.sort()
print("Úkol [4] - {}".format(text))