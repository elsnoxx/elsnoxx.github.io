from flask import Flask, request, render_template, redirect, url_for, abort, send_file
import io

app = Flask(__name__)

# 1. Základní routy (Routes)
@app.route('/')
def home():
    # Hlavní stránka – zde by se zobrazovala úvodní stránka aplikace
    pass

@app.route('/about')
def about():
    # Stránka "O nás" – informace o projektu nebo autorovi
    pass

# 2. Dynamické routy
@app.route('/user/<username>')
def show_user(username):
    # Dynamická stránka pro uživatele podle jména
    pass

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Dynamická stránka pro příspěvek podle ID (čísla)
    pass

@app.route('/category/<category>')
def show_category(category):
    # Dynamická stránka pro kategorii podle názvu
    pass

# 3. HTTP metody (GET, POST)
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Přihlašovací stránka – GET zobrazí formulář, POST zpracuje přihlášení
    pass

# 4. Templates (Šablony)
@app.route('/hello/<name>')
def hello(name):
    # Ukázka použití šablony s proměnnou (např. hello.html)
    pass

# 5. Zpracování formulářů
@app.route('/form', methods=['GET', 'POST'])
def form():
    # Stránka s formulářem – GET zobrazí, POST zpracuje data z formuláře
    pass

# 6. Redirecty a chyby
@app.route('/redirect')
def redirect_example():
    # Přesměrování na jinou stránku v aplikaci
    pass

@app.route('/error')
def error_example():
    # Vyvolání chyby 404 – stránka nenalezena
    pass

# Vlastní stránka pro chybu 404
@app.errorhandler(404)
def page_not_found(e):
    # Vlastní text nebo stránka pro chybu 404
    pass

# 7. Vrácení různých typů odpovědí

@app.route('/text')
def text_response():
    # Vrácení čistého textu
    pass

@app.route('/html')
def html_response():
    # Vrácení HTML kódu
    pass

@app.route('/json')
def json_response():
    # Vrácení JSON odpovědi (např. slovník)
    pass

@app.route('/tuple')
def tuple_response():
    # Vrácení odpovědi jako tuple (obsah, status kód, hlavičky)
    pass

# 8. Vrácení souboru ke stažení
@app.route('/download')
def download_file():
    # Vrácení souboru ke stažení (např. textový soubor)
    pass

# 9. Vrácení přesměrování na externí web
@app.route('/google')
def google_redirect():
    # Přesměrování na externí web (např. Google)
    pass

# 10. Vlastní HTTP status kód a hlavičky
@app.route('/custom')
def custom_response():
    # Vrácení odpovědi s vlastním status kódem a hlavičkami
    pass

@app.route('/styled')
def styled():
    # Vrácení HTML stránky s vloženým CSS stylem
    pass

@app.route('/plain')
def plain():
    # Vrácení čistého textu s nastaveným content-type
    pass

@app.route('/headers')
def headers():
    # Vrácení odpovědi s vlastními hlavičkami
    pass

@app.route('/xml')
def xml():
    # Vrácení XML odpovědi
    pass

@app.route('/csv')
def csv():
    # Vrácení CSV dat
    pass

@app.route('/set-cookie')
def set_cookie():
    # Nastavení cookie v odpovědi
    pass

@app.route('/get-cookie')
def get_cookie():
    # Získání hodnoty cookie z požadavku
    pass

@app.route('/status')
def status():
    # Vrácení pouze status kódu bez obsahu (např. 204)
    pass

@app.route('/json-list')
def json_list():
    # Vrácení JSON pole (seznam slovníků)
    pass

@app.route('/json-nested')
def json_nested():
    # Vrácení vnořeného JSON (slovník v slovníku)
    pass

@app.route('/html-table')
def html_table():
    # Vrácení HTML stránky s tabulkou
    pass

@app.route('/inline-js')
def inline_js():
    # Vrácení HTML stránky s JavaScriptem
    pass

@app.route('/inline-img')
def inline_img():
    # Vrácení HTML stránky s obrázkem
    pass

@app.route('/params')
def params():
    # Vrácení GET parametrů z URL
    pass

@app.route('/post-json', methods=['POST'])
def post_json():
    # Přijetí a vrácení JSON dat v POST požadavku
    pass

@app.route('/uppercase/<text>')
def uppercase(text):
    # Vrácení textu převedeného na velká písmena
    pass

@app.route('/repeat/<int:n>/<word>')
def repeat(n, word):
    # Vrácení slova opakovaného n-krát
    pass

if __name__ == '__main__':
    app.run(debug=True)