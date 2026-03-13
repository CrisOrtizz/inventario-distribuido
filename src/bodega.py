import threading
import random
import time

class Bodega(threading.Thread):

    def __init__(self, nombre, servidor):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.servidor = servidor

    def run(self):

        productos = ["martillo", "taladro", "destornillador"]

        for _ in range(3):

            producto = random.choice(productos)
            cantidad = random.randint(1,3)

            print(f"\n[{self.nombre}] solicita venta de {cantidad} {producto}")

            self.servidor.procesar_venta(self.nombre, producto, cantidad)

            time.sleep(random.uniform(0.5,2))