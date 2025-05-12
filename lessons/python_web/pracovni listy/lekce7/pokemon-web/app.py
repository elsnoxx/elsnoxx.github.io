import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    error = None
    if request.method == 'POST':
        name = request.form['name'].strip().lower()
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        resp = requests.get(url)
        if resp.status_code == 200:
            poke = resp.json()
            data = {
                'name': poke['name'].capitalize(),
                'img': poke['sprites']['front_default'],
                'height': poke['height'],
                'weight': poke['weight'],
                'types': [t['type']['name'] for t in poke['types']],
                'abilities': [a['ability']['name'] for a in poke['abilities']],
                'id': poke['id'],
                'base_experience': poke['base_experience'],
                'stats': {s['stat']['name']: s['base_stat'] for s in poke['stats']}
            }
        else:
            error = "Pokémon nenalezen!"
    return render_template('index.html', data=data, error=error)

if __name__ == '__main__':
    app.run(debug=True)