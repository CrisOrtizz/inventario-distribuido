import threading
import random
import time

class Bodega(threading.Thread):

    def __init__(self, nombre, inventario):
        super().__init__()
        self.nombre = nombre
        self.inventario = inventario
        self.daemon = True   # MUY IMPORTANTE para servidores como Render
        self.productos = ["martillo", "taladro", "destornillador"]

    def run(self):

        while True:

            producto = random.choice(self.productos)
            cantidad = random.randint(1, 2)

            self.inventario.vender(self.nombre, producto, cantidad)

            time.sleep(random.randint(4, 8))