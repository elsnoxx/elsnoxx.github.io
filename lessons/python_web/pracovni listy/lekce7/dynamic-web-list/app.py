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
    return ""

@app.route('/uzivatele')
def uzivatele():
    # Ukázka výpisu seznamu a podmínky
    # Do šablony uzivatele.html pošleme seznam uživatelů
    users = ["Anna", "Petr", "Jana"]
    return ""

@app.route('/tabulka')
def tabulka():
    # Ukázka generování tabulky z dat
    # Do šablony tabulka.html pošleme seznam slovníků (osoby)
    osoby = [{"jmeno": "Anna", "vek": 23}, {"jmeno": "Petr", "vek": 31}]
    return ""

@app.route('/dotaz', methods=['GET', 'POST'])
def dotaz():
    # Ukázka formuláře a zpracování dat
    # GET: zobrazí formulář (dotaz.html)
    # POST: zpracuje data z formuláře a zobrazí výsledek (vysledek.html)

    return ""

@app.route('/pozdrav/<jmeno>')
def pozdrav_param(jmeno):
    # Ukázka práce s parametrem v URL
    # Hodnota <jmeno> z adresy se pošle do šablony pozdrav.html
    return ""

if __name__ == '__main__':
    # Spuštění aplikace v režimu debug (vhodné pro vývoj)
    app.run(debug=True)