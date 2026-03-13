from flask import Blueprint, request, redirect
from app.models.inventario import Inventario

inventario_bp = Blueprint("inventario", __name__)

inventario = Inventario()


@inventario_bp.route("/vender", methods=["POST"])
def vender():

    producto = request.form["producto"]
    cantidad = int(request.form["cantidad"])
    bodega = request.form["bodega"]

    inventario.vender(bodega, producto, cantidad)

    return redirect("/")