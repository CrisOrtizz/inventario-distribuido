from flask import Flask, render_template
from app.controllers.inventario_controller import inventario_bp, inventario

app = Flask(__name__, template_folder="views", static_folder="static")

app.register_blueprint(inventario_bp)


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