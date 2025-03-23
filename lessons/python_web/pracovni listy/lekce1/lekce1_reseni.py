# 1️⃣ Výpis textu
# Úkol: Vypiš na obrazovku text: "Ahoj světe!"
# ---------------------------------------------
# Tvůj kód sem:
print("Ahoj světe!")
# ---------------------------------------------

# 2️⃣ Práce s proměnnými
# Úkol: Oprav chybu v tomto kódu:
# x = "10"
# y = 5
# print(x + y)
# ---------------------------------------------
# Opravený kód:
x = 10
y = 5
print(x + y)
# ---------------------------------------------

# 3️⃣ Podmínky (if-else)
# Úkol: Oprav chybu v podmínce, aby program správně fungoval:
# age = 18
# ---------------------------------------------
# Opravený kód:
age = 18
if age >= 18:
    print("Jsi dospělý!")
else:
    print("Jsi dítě!")
# ---------------------------------------------

# 4️⃣ Cykly (for)
# Úkol: Napiš program, který vypíše čísla od 1 do 5 pomocí for cyklu.
# ---------------------------------------------
# Řešení:
for i in range(1, 6):
    print(i)
# ---------------------------------------------

# 5️⃣ Seznamy (list)
# Úkol: Opravit kód tak, aby správně vypsal třetí prvek seznamu:
# my_list = [10, 20, 30, 40, 50]
# ---------------------------------------------
# Opravený kód:
my_list = [10, 20, 30, 40, 50]
print(my_list[2])  # Třetí prvek (index 2)
# ---------------------------------------------

# 6️⃣ Funkce
# Úkol: Napiš funkci, která přijme jméno a vypíše „Ahoj, [jméno]!“
# ---------------------------------------------
# Řešení:
def pozdrav(jmeno):
    print(f"Ahoj, {jmeno}!")

pozdrav("Eliška")
# ---------------------------------------------

# 7️⃣ Slovníky (dictionary)
# Úkol: Opravit kód tak, aby správně vypsal věk „Tomáše“:
# ages = {"Petr": 25, "Tomáš": 30, "Eva": 22}
# ---------------------------------------------
# Opravený kód:
ages = {"Petr": 25, "Tomáš": 30, "Eva": 22}
print(ages["Tomáš"])
# ---------------------------------------------

# 8️⃣ Práce se stringy
# Úkol: Opravit kód, aby správně vypisoval první písmeno jména:
# jmeno = "Eliška"
# ---------------------------------------------
# Opravený kód:
jmeno = "Eliška"
print(jmeno[0])  # První písmeno
# ---------------------------------------------

# 9️⃣ Základní operátory
# Úkol: Napiš kód tak, aby správně spočítal rozdíl mezi dvěma čísly:
# a = 10
# b = 4
# ---------------------------------------------
# Řešení:
a = 10
b = 4
print(a - b)
# ---------------------------------------------

# 🔟 Zpracování vstupu od uživatele
# Úkol: Napiš program, který se zeptá uživatele na jeho jméno a pozdraví ho.
# ---------------------------------------------
# Řešení:
jmeno = input("Jak se jmenuješ? ")
print(f"Ahoj, {jmeno}!")
# ---------------------------------------------
