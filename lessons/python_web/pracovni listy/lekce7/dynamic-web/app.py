"""
Ukázková Flask aplikace – základy dynamického webu

Tento soubor ukazuje, jak:
- vytvořit různé stránky (routy) ve Flasku,
- předávat proměnné do šablon,
- pracovat s cykly a podmínkami v šablonách,
- zpracovávat formuláře,
- používat parametry v URL.

Každá route (funkce s @app.route) odpovídá jedné stránce webu.
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Úvodní stránka s odkazy na ukázky
    return render_template('index.html')

@app.route('/pozdrav')
def pozdrav():
    # Ukázka vkládání proměnné do šablony
    # Do šablony pozdrav.html pošleme proměnnou jmeno s hodnotou 'Anna'
    return render_template('pozdrav.html', jmeno='Anna')

@app.route('/uzivatele')
def uzivatele():
    # Ukázka výpisu seznamu a podmínky
    # Do šablony uzivatele.html pošleme seznam uživatelů
    users = ["Anna", "Petr", "Jana"]
    return render_template('uzivatele.html', users=users)

@app.route('/tabulka')
def tabulka():
    # Ukázka generování tabulky z dat
    # Do šablony tabulka.html pošleme seznam slovníků (osoby)
    osoby = [{"jmeno": "Anna", "vek": 23}, {"jmeno": "Petr", "vek": 31}]
    return render_template('tabulka.html', osoby=osoby)

@app.route('/dotaz', methods=['GET', 'POST'])
def dotaz():
    # Ukázka formuláře a zpracování dat
    # GET: zobrazí formulář (dotaz.html)
    # POST: zpracuje data z formuláře a zobrazí výsledek (vysledek.html)
    if request.method == 'POST':
        odpoved = request.form['odpoved']
        return render_template('vysledek.html', odpoved=odpoved)
    return render_template('dotaz.html')

@app.route('/pozdrav/<jmeno>')
def pozdrav_param(jmeno):
    # Ukázka práce s parametrem v URL
    # Hodnota <jmeno> z adresy se pošle do šablony pozdrav.html
    return render_template('pozdrav.html', jmeno=jmeno)

@app.route("/about")
def about():
    # Samostatná práce s proměnnými v šabloně
    # Do šablony about.html pošleme proměnné jmeno, prijmeni a vek
    # Zde můžeš změnit hodnoty proměnných podle sebe
    # (např. jméno, příjmení a věk)
    # Vytvoř si vlastní šablonu about.html
    # a přidej do ní proměnné jmeno, prijmeni a vek
    # a jejich hodnoty
    jmeno = "TvojeJmeno"         # Změň na své jméno
    prijmeni = "TvojePrijmeni"   # Změň na své příjmení
    vek = 20                     # Změň na svůj věk
    return render_template("about.html", jmeno=jmeno, prijmeni=prijmeni, vek=vek)

if __name__ == '__main__':
    # Spuštění aplikace v režimu debug (vhodné pro vývoj)
    app.run(debug=True)