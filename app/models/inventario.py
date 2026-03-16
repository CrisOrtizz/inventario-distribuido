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

                # reposición automática si el stock es bajo
                if self.stock[producto] < 5:

                    self.stock[producto] += 50

                    evento_reposicion = f"Sistema repuso inventario de {producto}"

                    self.eventos.insert(0, evento_reposicion)

                return True

            return False

    def obtener_stock(self):

        return self.stock

    def obtener_eventos(self):

        return self.eventos[:10]