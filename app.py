from flask import Flask, render_template, request, jsonify
from turnero import Turnero

app = Flask(__name__)
turnero = Turnero()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generar_turno", methods=["POST"])
def generar_turno():
    data = request.get_json()
    tipo = data.get("tipo")
    try:
        turno = turnero.generar_turno(tipo)
        return jsonify({
            "turno": turno,
            "estado": turnero.contadores  # devolvemos el estado actual
        })
    except ValueError:
        return jsonify({"ERROR": "Tipo inválido"}), 400

@app.route("/estado")
def estado():
    return jsonify(turnero.contadores)

if __name__ == "__main__":
    app.run(debug=True)
