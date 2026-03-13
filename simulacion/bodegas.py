import threading
import random
import time

class Bodega(threading.Thread):

    def __init__(self, nombre, inventario):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.inventario = inventario
        self.productos = ["martillo", "taladro", "destornillador"]

    def run(self):

        while True:

            producto = random.choice(self.productos)
            cantidad = random.randint(1,2)

            self.inventario.vender(self.nombre, producto, cantidad)

            time.sleep(random.randint(3,6))