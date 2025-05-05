from flask import Flask, request, render_template, redirect, url_for, abort, send_file
import io

app = Flask(__name__)

# 1. Základní routy (Routes)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'O nás'

# 2. Dynamické routy
@app.route('/user/<username>')
def show_user(username):
    # Dynamický segment v URL
    return f'Uživatel: {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Dynamický segment s typem int
    return f'Příspěvek číslo: {post_id}'

@app.route('/category/<category>')
def show_category(category):
    # Dynamický segment s typem string
    return f'Kategorie: {category}'

# 3. HTTP metody (GET, POST)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Zpracování přihlášení
        return 'Zpracování přihlášení'
    else:
        # Zobrazení přihlašovacího formuláře
        return 'Přihlašovací formulář'

# 4. Templates (Šablony)
@app.route('/hello/<name>')
def hello(name):
    # Vykreslení šablony hello.html s proměnnou name
    return render_template('hello.html', name=name)

# 5. Zpracování formulářů
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Zdravím, {name}!'
    return '''
        <form method="post">
            <input name="name">
            <button type="submit">Odeslat</button>
        </form>
    '''

# 6. Redirecty a chyby
@app.route('/redirect')
def redirect_example():
    # Přesměrování na jinou stránku
    return redirect(url_for('home'))

@app.route('/error')
def error_example():
    # Vyvolání chyby 404
    abort(404)

# Vlastní stránka pro chybu 404
@app.errorhandler(404)
def page_not_found(e):
    return "Stránka nebyla nalezena", 404

# 7. Vrácení různých typů odpovědí

@app.route('/text')
def text_response():
    # Vrací čistý text
    return "Toto je textová odpověď"

@app.route('/html')
def html_response():
    # Vrací HTML kód
    return "<h2>HTML odpověď</h2><p>Toto je odstavec v HTML.</p>"

@app.route('/json')
def json_response():
    # Vrací JSON odpověď (automaticky nastaví správný Content-Type)
    return {"status": "ok", "message": "Toto je JSON odpověď"}

@app.route('/tuple')
def tuple_response():
    # Vrací tuple (obsah, status kód, hlavičky)
    return ("Vlastní status a hlavička", 202, {"X-Custom-Header": "Hodnota"})

# 8. Vrácení souboru ke stažení
@app.route('/download')
def download_file():
    # Vytvoří soubor v paměti a nabídne ke stažení
    file_content = "Toto je obsah souboru."
    return send_file(
        io.BytesIO(file_content.encode()),
        mimetype='text/plain',
        as_attachment=True,
        download_name='soubor.txt'
    )

# 9. Vrácení přesměrování na externí web
@app.route('/google')
def google_redirect():
    return redirect("https://www.google.com")

# 10. Vlastní HTTP status kód a hlavičky
@app.route('/custom')
def custom_response():
    response = app.response_class(
        response="Vlastní odpověď",
        status=201,
        headers={"X-Example": "Test"}
    )
    return response

@app.route('/styled')
def styled():
    return '''
    <html>
      <head>
        <style>
          body { background: gray; }
          h1 { color: red; }
          p { color: blue; }
        </style>
      </head>
      <body>
        <h1>Stylovaná stránka</h1>
        <p>Toto je stránka s vloženým CSS.</p>
      </body>
    </html>
    '''

@app.route('/plain')
def plain():
    # Vrací čistý text s nastaveným content-type
    return "Čistý text s content-type", 200, {'Content-Type': 'text/plain'}

@app.route('/headers')
def headers():
    # Vrací odpověď s více vlastními hlavičkami
    return ("Odpověď s hlavičkami", 200, {
        "X-First": "Jedna",
        "X-Second": "Dva"
    })

@app.route('/xml')
def xml():
    # Vrací XML odpověď
    xml_data = "<note><to>User</to><body>Ahoj!</body></note>"
    return xml_data, 200, {'Content-Type': 'application/xml'}

@app.route('/csv')
def csv():
    # Vrací CSV data
    csv_data = "jmeno,vek\nPetr,30\nAnna,25"
    return csv_data, 200, {'Content-Type': 'text/csv'}

@app.route('/set-cookie')
def set_cookie():
    # Nastaví cookie v odpovědi
    resp = app.make_response("Cookie nastaveno")
    resp.set_cookie('moje_cookie', 'hodnota')
    return resp

@app.route('/get-cookie')
def get_cookie():
    # Získá hodnotu cookie
    value = request.cookies.get('moje_cookie', 'nenastaveno')
    return f'Hodnota cookie: {value}'

@app.route('/status')
def status():
    # Vrací pouze status kód bez obsahu
    return '', 204

@app.route('/json-list')
def json_list():
    # Vrací JSON pole
    return [{"id": 1, "jmeno": "Petr"}, {"id": 2, "jmeno": "Anna"}]

@app.route('/json-nested')
def json_nested():
    # Vrací vnořený JSON
    return {
        "status": "ok",
        "data": {
            "uzivatel": {"jmeno": "Petr", "vek": 30},
            "seznam": [1, 2, 3]
        }
    }

@app.route('/html-table')
def html_table():
    # Vrací HTML s tabulkou
    return '''
    <table border="1">
      <tr><th>Jméno</th><th>Věk</th></tr>
      <tr><td>Petr</td><td>30</td></tr>
      <tr><td>Anna</td><td>25</td></tr>
    </table>
    '''

@app.route('/inline-js')
def inline_js():
    # Vrací HTML s JavaScriptem
    return '''
    <html>
      <body>
        <h2>Ukázka JavaScriptu</h2>
        <button onclick="alert('Ahoj ze Flasku!')">Klikni mě</button>
      </body>
    </html>
    '''

@app.route('/inline-img')
def inline_img():
    # Vrací HTML s obrázkem (externí odkaz)
    return '''
    <html>
      <body>
        <h2>Obrázek</h2>
        <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python logo" width="200">
      </body>
    </html>
    '''

@app.route('/params')
def params():
    # Vrací GET parametry z URL
    args = dict(request.args)
    return f'Parametry v URL: {args}'

@app.route('/post-json', methods=['POST'])
def post_json():
    # Přijímá JSON v POST a vrací ho zpět
    data = request.get_json()
    return {"obdrzeno": data}

@app.route('/uppercase/<text>')
def uppercase(text):
    # Vrací text převedený na velká písmena
    return text.upper()

@app.route('/repeat/<int:n>/<word>')
def repeat(n, word):
    # Vrací slovo opakované n-krát
    return ' '.join([word] * n)

if __name__ == '__main__':
    app.run(debug=True)