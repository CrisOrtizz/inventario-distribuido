from flask import Flask, render_template, jsonify
from app.controllers.inventario_controller import inventario_bp, inventario
from simulacion.bodegas import Bodega
import os

app = Flask(__name__, template_folder="views", static_folder="static")

app.register_blueprint(inventario_bp)

# -----------------------------
# Control para iniciar bodegas
# -----------------------------

bodegas_iniciadas = False


def iniciar_bodegas():

    global bodegas_iniciadas

    if not bodegas_iniciadas:

        print("Iniciando simulación de bodegas...")

        bodega_norte = Bodega("Bodega Norte", inventario)
        bodega_centro = Bodega("Bodega Centro", inventario)
        bodega_industrial = Bodega("Bodega Industrial", inventario)

        bodega_norte.start()
        bodega_centro.start()
        bodega_industrial.start()

        bodegas_iniciadas = True


# Se ejecuta cuando llega la primera petición
@app.before_request
def arrancar_simulacion():
    iniciar_bodegas()


# -----------------------------
# API del sistema
# -----------------------------

@app.route("/inventario")
def inventario_api():

    stock = inventario.obtener_stock()

    return jsonify(stock)


@app.route("/eventos")
def eventos():

    eventos = inventario.obtener_eventos()

    return jsonify(eventos)


# -----------------------------
# Vistas
# -----------------------------

@app.route("/")
def index():

    eventos = inventario.obtener_eventos()

    return render_template("index.html", eventos=eventos)


@app.route("/admin")
def admin():

    stock = inventario.obtener_stock()

    return render_template("admin.html", stock=stock)


# -----------------------------
# Ejecución local
# -----------------------------

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 10000))

    app.run(host="0.0.0.0", port=port)