# 1️⃣ Výpis textu
# Úkol: Vypiš na obrazovku text: "Ahoj světe!"
print("Ahoj světe!")  # ✅ Očekávaný výstup: Ahoj světe!

# ---------------------------------------------

# 2️⃣ Práce s proměnnými
# Úkol: Oprav chybu v tomto kódu:
x = "10"
y = 5
print(int(x) + y)  # ✅ Opraveno: Převedení x na číslo

# ---------------------------------------------

# 3️⃣ Podmínky (if-else)
# Úkol: Oprav chybu v podmínce, aby program správně fungoval:
cislo = int(input("Zadej číslo: "))

if cislo % 2 == 0:  # ✅ Opraveno: Použití "==" místo "="
    print("Číslo je sudé.")
else:
    print("Číslo je liché.")

# ---------------------------------------------

# 4️⃣ Cykly (for)
# Úkol: Napiš program, který vypíše čísla od 1 do 5 pomocí for cyklu.
for i in range(1, 6):
    print(i)  # ✅ Očekávaný výstup: 1 2 3 4 5 (každé číslo na novém řádku)

# ---------------------------------------------

# 5️⃣ Seznamy (list)
# Úkol: Opravit kód tak, aby správně vypsal třetí prvek seznamu:
ovoce = ["jablko", "banán", "třešeň", "hruška"]
print(ovoce[2])  # ✅ Opraveno: Index 2 odpovídá třetímu prvku

# ---------------------------------------------

# 6️⃣ Funkce
# Úkol: Napiš funkci, která přijme jméno a vypíše „Ahoj, [jméno]!“
def pozdrav(jmeno):
    print(f"Ahoj, {jmeno}!")  # ✅ Opraveno: Použití f-stringu

pozdrav("Petr")  # ✅ Očekávaný výstup: Ahoj, Petr!

# ---------------------------------------------

# 7️⃣ Slovníky (dictionary)
# Úkol: Opravit kód tak, aby správně vypsal věk „Tomáše“:
vek = {"Petr": 25, "Tomáš": 30, "Anna": 22}
print(vek["Tomáš"])  # ✅ Opraveno: Použití hranatých závorek

# ---------------------------------------------

# 8️⃣ Práce se stringy
# Úkol: Opravit kód, aby správně vypisoval první písmeno jména:
jmeno = "Eliška"
print(jmeno[0])  # ✅ Opraveno: Použití hranatých závorek místo kulatých
