import threading
import random
import time
from app.models.inventario import Inventario

inventario = Inventario()

class Bodega(threading.Thread):

    def __init__(self, nombre):
        threading.Thread.__init__(self)
        self.nombre = nombre

    def run(self):

        productos = ["martillo", "taladro", "destornillador"]

        for _ in range(3):

            producto = random.choice(productos)
            cantidad = random.randint(1,2)

            print(f"{self.nombre} intenta vender {producto}")

            inventario.vender(producto, cantidad)

            time.sleep(1)