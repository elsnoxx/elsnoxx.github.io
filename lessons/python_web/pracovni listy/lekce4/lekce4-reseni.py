# Úkol 1: Třída Pes
# Vytvoř třídu Pes, která má atributy jméno a barva. Přidej metodu info, která vypíše informace o psovi.
class Pes:
    def __init__(self, jmeno, barva):
        self.jmeno = jmeno
        self.barva = barva

    def info(self):
        print(f"Pes: {self.jmeno}, Barva: {self.barva}")


pes1 = Pes("Rex", "hnědá")
pes2 = Pes("Baryk", "černá")
pes1.info()
pes2.info()

# Úkol 2: Třída Osoba se zapouzdřením
# Vytvoř třídu Osoba, která má atributy jméno a věk. Věk nastav jako soukromý atribut.
# Přidej metody pro změnu věku (zmen_vek) a získání věku (get_vek).
class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.__vek = vek

    def zmen_vek(self, novy_vek):
        self.__vek = novy_vek

    def get_vek(self):
        return self.__vek
    
osoba1 = Osoba("Jan Novák", 30)
print(f"Věk osoby {osoba1.jmeno}: {osoba1.get_vek()} let")
osoba1.zmen_vek(35)
print(f"Nový věk osoby {osoba1.jmeno}: {osoba1.get_vek()} let")

# Úkol 3: Třída Auto
# Vytvoř třídu Auto, která má atributy značka a barva. Přidej metodu info, která vypíše informace o autě.
class Auto:
    def __init__(self, znacka, barva):
        self.znacka = znacka
        self.barva = barva

    def info(self):
        print(f"Auto: {self.znacka}, Barva: {self.barva}")

auto1 = Auto("Škoda", "modrá")
auto2 = Auto("Tesla", "červená")
auto1.info()
auto2.info()


# Úkol 4: Dědičnost - Třída ElektrickeAuto
# Vytvoř třídu ElektrickeAuto, která dědí od třídy Auto. Přidej atribut kapacita_baterie a metodu nabij,
# která vypíše, že auto je nabíjeno, a zobrazí kapacitu baterie.
class ElektrickeAuto(Auto):
    def __init__(self, znacka, barva, kapacita_baterie):
        super().__init__(znacka, barva)
        self.kapacita_baterie = kapacita_baterie

    def nabij(self):
        print(f"Auto je nyní nabíjeno. Kapacita baterie: {self.kapacita_baterie} kWh")

elektricke_auto = ElektrickeAuto("Tesla", "bílá", 75)
elektricke_auto.info()
elektricke_auto.nabij()
elektricke_auto.info()

# Úkol 5: Polymorfismus - Třída Zvire
# Vytvoř abstraktní třídu Zvire s metodou zvuk. Poté vytvoř dvě třídy Pes a Kocka,
# které dědí od třídy Zvire a implementují metodu zvuk.
class Zvire:
    def zvuk(self):
        pass

class Pes(Zvire):
    def zvuk(self):
        return "Haf!"

class Kocka(Zvire):
    def zvuk(self):
        return "Mňau!"
    
pes = Pes()
kocka = Kocka()
print(f"Zvuk psa: {pes.zvuk()}")
print(f"Zvuk kočky: {kocka.zvuk()}")

# Úkol 6: Hra - Evidence zvířat v zoo
# Vytvoř třídu Zvire, která má atributy jméno a druh. Přidej metodu info, která vypíše informace o zvířeti.
# Poté vytvoř třídu Zoo, která bude evidovat zvířata. Přidej metody pro přidání zvířete, zobrazení všech zvířat
# a hledání zvířete podle jména.

class Zvire:
    def __init__(self, jmeno, druh):
        self.jmeno = jmeno
        self.druh = druh

    def info(self):
        return f"Zvíře: {self.jmeno}, Druh: {self.druh}"

class Zoo:
    def __init__(self):
        self.zvirata = []

    def pridej_zvire(self, zvire):
        self.zvirata.append(zvire)
        print(f"Zvíře {zvire.jmeno} bylo přidáno do zoo.")

    def zobraz_vsechna_zvirata(self):
        if not self.zvirata:
            print("Zoo je prázdná.")
        else:
            print("Seznam zvířat v zoo:")
            for zvire in self.zvirata:
                print(zvire.info())

    def najdi_zvire(self, jmeno):
        for zvire in self.zvirata:
            if zvire.jmeno == jmeno:
                print(f"Nalezeno: {zvire.info()}")
                return
        print(f"Zvíře s jménem {jmeno} nebylo nalezeno.")

# Použití
zoo = Zoo()

# Přidání zvířat
zoo.pridej_zvire(Zvire("Lev", "Šelma"))
zoo.pridej_zvire(Zvire("Slon", "Savci"))
zoo.pridej_zvire(Zvire("Papoušek", "Ptáci"))

# Zobrazení všech zvířat
zoo.zobraz_vsechna_zvirata()

# Hledání zvířete podle jména
zoo.najdi_zvire("Slon")
zoo.najdi_zvire("Tygr")