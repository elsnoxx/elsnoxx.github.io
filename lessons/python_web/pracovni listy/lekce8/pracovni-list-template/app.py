from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

# Seznamy pro úkoly:
todos = []         # aktuální úkoly
todos_done = []    # splněné úkoly
todo_smazane = []  # smazané úkoly

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Hlavní stránka aplikace.
    - GET: zobrazí seznam aktuálních úkolů.
    - POST: přijme data z formuláře a přidá nový úkol do seznamu todos.
    Každý úkol může obsahovat např. text, poznámku, termín, předmět atd.
    """
    # Zde doplň logiku pro přidání úkolu z formuláře (POST)
    # a pro zobrazení seznamu úkolů (GET)
    return render_template('index.html', todos=todos, count=len(todos))

@app.route('/done/<int:idx>', methods=['POST'])
def done(idx):
    """
    Označí úkol jako splněný.
    - Najde úkol podle indexu v seznamu todos.
    - Přesune ho do seznamu splněných úkolů (todos_done).
    - Nastaví mu čas splnění.
    """
    # Zde doplň logiku pro přesun úkolu do splněných
    return redirect('/')

@app.route('/delete/<int:idx>')
def delete(idx):
    """
    Smaže úkol (přesune do seznamu smazaných).
    - Najde úkol podle indexu v seznamu todos.
    - Přesune ho do seznamu smazaných úkolů (todo_smazane).
    - Může nastavit čas smazání.
    """
    # Zde doplň logiku pro přesun úkolu do smazaných
    return redirect('/')

@app.route('/edit/<int:idx>', methods=['GET', 'POST'])
def edit(idx):
    """
    Editace úkolu.
    - GET: zobrazí formulář s předvyplněnými údaji úkolu.
    - POST: uloží změny do úkolu v seznamu todos.
    """
    # Zde doplň logiku pro úpravu úkolu (GET zobrazí formulář, POST uloží změny)
    return render_template('edit.html', todo=todos[idx], idx=idx)

@app.route('/history')
def history():
    """
    Zobrazení historie úkolů.
    - Zobrazí seznam splněných a smazaných úkolů.
    - U každého úkolu může být zobrazen čas splnění/smazání a další informace.
    """
    # Zde doplň logiku pro zobrazení splněných a smazaných úkolů
    return render_template('history.html', splnene=todos_done, smazane=todo_smazane)

@app.errorhandler(404)
def page_not_found(e):
    """
    Vlastní stránka pro chybu 404.
    - Zobrazí jednoduchou zprávu, že stránka nebyla nalezena.
    """
    return "Stránka nebyla nalezena", 404

if __name__ == '__main__':
    app.run(debug=True)