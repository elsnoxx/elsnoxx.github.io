import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Úkol: Vytvoř webovou aplikaci, která umožní uživateli zadat jméno Pokémona a zobrazí jeho informace.
# 1. Nastav route '/' pro GET i POST požadavky.
# 2. Pokud je metoda POST, získej jméno Pokémona z formuláře (request.form['name']).
# 3. Sestav URL pro PokeAPI podle zadaného jména.
# 4. Pošli GET požadavek na API a zpracuj odpověď:
#    - Pokud je status_code 200, zpracuj data a připrav je pro šablonu.
#    - Pokud není Pokémon nalezen, nastav chybovou hlášku.
# 5. Vrať render_template s daty nebo chybou do šablony index.html.

@app.route('/', methods=['GET', 'POST'])
def index():
    # url = f'https://pokeapi.co/api/v2/pokemon/{name}'

        # Získání jména Pokémona z formuláře, úprava na malá písmena a odstranění mezer

        # Sestavení URL pro API podle zadaného jména
        
        # Odeslání GET požadavku na API

            # Pokud je odpověď v pořádku, zpracuj data

            # Pokud Pokémon není nalezen, nastav chybovou hlášku

    # Vrať šablonu s daty nebo chybou
    return ""

if __name__ == '__main__':
    # Spusť aplikaci v debug režimu
    app.run(debug=True)