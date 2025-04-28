from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hlavní stránka s výpisem filmů a her
@app.route('/')
def home():
    return render_template('index.html')

# Detailní stránka pro Avengers
@app.route('/avengers')
def avengers():
    return render_template('avengers.html')

# Detailní stránka pro Batmana
@app.route('/batman')
def batman():
    return render_template('batman.html')

# Detailní stránka pro Inception
@app.route('/inception')
def inception():
    return render_template('inception.html')

# Detailní stránka pro Age of Empires
@app.route('/ageofempires')
def ageofempires():
    return render_template('ageofempires.html')

# Detailní stránka pro Minecraft
@app.route('/minecraft')
def minecraft():
    return render_template('minecraft.html')

# Detailní stránka pro Call of Duty
@app.route('/callofduty')
def callofduty():
    return render_template('callofduty.html')

# Chybová stránka 404 - stránka nenalezena
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Stránka s formulářem
@app.route('/napsat', methods=['GET', 'POST'])
def napsat():
    if request.method == 'POST':
        oblibeny_film = request.form['film']
        print(f"Uživatel napsal: {oblibeny_film}")  # Vypsání do konzole
        return render_template('thankyou.html', film=oblibeny_film)
    return render_template('napsat.html')


# Spuštění aplikace v debug režimu
if __name__ == '__main__':
    app.run(debug=True)