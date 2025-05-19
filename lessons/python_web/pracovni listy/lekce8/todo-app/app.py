from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

todos = []
todos_done = []
todo_smazane = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ukol = request.form.get('ukol')
        poznamka = request.form.get('poznamka')
        ocekavane = request.form.get('ocekavane')
        predmet = request.form.get('predmet')
        if ukol:
            todos.append({
                'text': ukol,
                'poznamka': poznamka,
                'ocekavane': ocekavane,
                'predmet': predmet,
                'done': False,
                'created': datetime.now().strftime('%d.%m.%Y %H:%M'),
                'completed': None
            })
        return redirect('/')
    return render_template('index.html', todos=todos, count=len(todos))

@app.route('/done/<int:idx>', methods=['POST'])
def done(idx):
    if 0 <= idx < len(todos):
        todo = todos.pop(idx)
        todo['done'] = True
        todo['completed'] = datetime.now().strftime('%d.%m.%Y %H:%M')
        todos_done.append(todo)
    return redirect('/')

@app.route('/delete/<int:idx>')
def delete(idx):
    if 0 <= idx < len(todos):
        todo_smazane.append(todos[idx])
        todos.pop(idx)
        
    return redirect('/')

@app.route('/edit/<int:idx>', methods=['GET', 'POST'])
def edit(idx):
    if 0 <= idx < len(todos):
        if request.method == 'POST':
            new_text = request.form.get('ukol')
            new_poznamka = request.form.get('poznamka')
            new_ocekavane = request.form.get('ocekavane')
            new_predmet = request.form.get('predmet')
            
            todos[idx]['text'] = new_text
            todos[idx]['poznamka'] = new_poznamka
            todos[idx]['ocekavane'] = new_ocekavane
            todos[idx]['predmet'] = new_predmet

            return redirect('/')
        return render_template('edit.html', todo=todos[idx], idx=idx)
    return redirect('/')

@app.route('/history')
def history():
    return render_template('history.html', splnene=todos_done, smazane=todo_smazane)

# Vlastní stránka pro chybu 404
@app.errorhandler(404)
def page_not_found(e):
    return "Stránka nebyla nalezena", 404

if __name__ == '__main__':
    app.run(debug=True)