from flask import Flask, render_template
from app.controllers.inventario_controller import inventario_bp, inventario
from simulacion.bodegas import Bodega
from flask import jsonify

app = Flask(__name__, template_folder="views", static_folder="static")

app.register_blueprint(inventario_bp)

# Simulación de nodos de bodegas

bodega_norte = Bodega("Bodega Norte", inventario)
bodega_centro = Bodega("Bodega Centro", inventario)
bodega_industrial = Bodega("Bodega Industrial", inventario)

bodega_norte.start()
bodega_centro.start()
bodega_industrial.start()


@app.route("/inventario")
def inventario_api():

    stock = inventario.obtener_stock()

    return jsonify(stock)

@app.route("/eventos")
def eventos():

    eventos = inventario.obtener_eventos()

    return jsonify(eventos)

@app.route("/")
def index():

    eventos = inventario.obtener_eventos()

    return render_template("index.html", eventos=eventos)


@app.route("/admin")
def admin():

    stock = inventario.obtener_stock()

    return render_template("admin.html", stock=stock)


if __name__ == "__main__":
    app.run(debug=True)