from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import random
import json
import os

# Vytvoření Flask aplikace
app = Flask(__name__)
app.secret_key = 'tajny_klic_pro_tvou_aplikaci'

# Domovská stránka
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['GET'] )
def start():
    try:
        with open('questions.json', 'r', encoding='utf-8') as f:
            questions = json.load(f)
        
        questions = questions['questions']
        print(questions)
        forms = []
        while len(forms) < 5:
            question = random.choice(questions)
            if question in forms:
                continue
            forms.append(question)
            


        return render_template('start.html', questions=forms)
    except Exception as e:
        return f"Chyba: {str(e)}", 500

@app.route('/submit_answers', methods=['POST'])
def submit_answers():
    # Inicializace skóre
    score = 0
    
    # Zjisti počet otázek
    question_count = 0
    while f'answer_{question_count}' in request.form:
        question_count += 1
    
    # Zpracování odpovědí
    for i in range(question_count):
        user_answer = request.form.get(f'answer_{i}')
        correct_answer = request.form.get(f'correct_{i}')
        
        if user_answer == correct_answer:
            score += 1
    
    # Výpočet procenta úspěšnosti
    percentage = (score / question_count) * 100 if question_count > 0 else 0
    
    # Vrácení výsledků
    return render_template('results.html', 
                          score=score, 
                          total=question_count, 
                          percentage=percentage)

@app.route('/results')
def results():
    # Získání výsledků ze session
    score = session.get('score', 0)
    total = session.get('total_questions', 0)
    
    # Výpočet procent
    percentage = (score / total) * 100 if total > 0 else 0
    
    return render_template('results.html', score=score, total=total, percentage=percentage)

if __name__ == '__main__':
    app.run(debug=True)