# Importujeme potřebné nástroje z knihovny Flask
# Flask - hlavní nástroj pro vytvoření webové aplikace
# render_template - umožňuje zobrazit HTML stránky
# request - umožňuje pracovat s daty z formulářů
# redirect a url_for - umožňují přesměrování na jiné stránky
from flask import Flask, render_template, request, redirect, url_for

# Vytvoříme novou webovou aplikaci
# __name__ je speciální proměnná v Pythonu, která obsahuje jméno aktuálního souboru
app = Flask(__name__)

# Vytvoříme seznam našich citátů
# Každý citát má text a autora
# V reálné aplikaci bychom citáty ukládali do databáze, ale pro jednoduchost
# je máme přímo v kódu
nase_citaty = [
    {
        'text': 'Život je to, co se děje, když jste zaneprázdněni plánováním něčeho jiného.',
        'author': 'John Lennon'
    },
    {
        'text': 'Štěstí není něco hotového. Přichází z vašich vlastních činů.',
        'author': 'Dalajláma'
    }
]

# Nastavíme, co se má stát, když někdo navštíví hlavní stránku (adresa "/")
@app.route('/')
def hlavni_stranka():
    # Zobrazíme stránku index.html a předáme jí seznam citátů
    return render_template('index.html', quotes=nase_citaty)

# Nastavíme, co se má stát, když někdo navštíví stránku pro přidání citátu (adresa "/add")
# methods=['GET', 'POST'] znamená, že stránka umí přijímat formuláře (POST) i normálně zobrazovat (GET)
@app.route('/add', methods=['GET', 'POST'])
def pridat_citat():
    # Pokud uživatel odeslal formulář (metoda POST)
    if request.method == 'POST':
        novy_citat = {
            'text': request.form['text'],
            'author': request.form['author']
        }
        
        # Přidáme nový citát do našeho seznamu
        nase_citaty.append(novy_citat)
        
        # Přesměrujeme uživatele zpět na hlavní stránku
        return redirect(url_for('hlavni_stranka'))
    
    # Pokud uživatel jen navštívil stránku (metoda GET), zobrazíme formulář
    return render_template('add.html')

# Nastavíme, co se má stát, když někdo hledá citáty podle autora
# <author_name> je proměnná část adresy - např. /author/Einstein
@app.route('/author/<author_name>')
def citaty_od_autora(author_name):
    # Najdeme všechny citáty od zadaného autora
    # Pro každý citát v našem seznamu: Přidej ho do nového seznamu, pokud je od hledaného autora
    citaty_autora = []
    for citat in nase_citaty:
        # Porovnáváme jména bez ohledu na velká/malá písmena (.lower())
        if citat['author'].lower() == author_name.lower():
            citaty_autora.append(citat)
    
    # Zobrazíme stránku s citáty od vybraného autora
    return render_template('author.html', quotes=citaty_autora, author=author_name)

# Pokud je tento soubor spuštěn přímo (ne importován), spustíme webový server
if __name__ == '__main__':
    # debug=True znamená, že server se automaticky restartuje při změnách kódu
    # a zobrazuje chybové hlášky - v reálném provozu by to bylo vypnuté!
    print("Spouštím webový server! Navštiv adresu http://127.0.0.1:5000 ve svém prohlížeči")
    app.run(debug=True)