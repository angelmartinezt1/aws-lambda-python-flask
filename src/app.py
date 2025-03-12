from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas


@app.route("/")
def home():
    return jsonify({"message": "¡Hola, Flask está corriendo correctamente!"})


@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
