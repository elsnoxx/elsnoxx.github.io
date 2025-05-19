from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

seznam = []

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", seznam=seznam)

@app.route("/pridat", methods=["POST"])
def pridat():
    polozka = request.form.get("polozka")
    if polozka:
        seznam.append(polozka)
    return redirect(url_for("index"))

@app.route("/odebrat/<int:index>", methods=["POST"])
def odebrat(index):
    try:
        seznam.pop(index)
    except IndexError:
        pass
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)