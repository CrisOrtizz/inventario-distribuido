import threading

class Inventario:

    def __init__(self):
        self.stock = {
            "martillo": 10,
            "taladro": 5,
            "destornillador": 20
        }

        self.lock = threading.Lock()

    def vender(self, producto, cantidad):

        with self.lock:

            if self.stock.get(producto, 0) >= cantidad:
                self.stock[producto] -= cantidad
                return True, self.stock[producto]

            return False, self.stock.get(producto, 0)