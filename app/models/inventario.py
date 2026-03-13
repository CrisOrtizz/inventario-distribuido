import threading

class Inventario:

    def __init__(self):

        self.stock = {
            "martillo": 10,
            "taladro": 5,
            "destornillador": 20
        }

        self.lock = threading.Lock()

        self.eventos = []

    def vender(self, bodega, producto, cantidad):

        with self.lock:

            if self.stock.get(producto, 0) >= cantidad:

                self.stock[producto] -= cantidad

                evento = f"{bodega} vendió {cantidad} {producto}"

                self.eventos.insert(0, evento)

                return True

            return False

    def obtener_stock(self):

        return self.stock

    def obtener_eventos(self):

        return self.eventos[:10]