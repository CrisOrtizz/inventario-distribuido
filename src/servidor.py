from inventario import Inventario

class ServidorCentral:

    def __init__(self):
        self.inventario = Inventario()

    def procesar_venta(self, bodega, producto, cantidad):

        aprobado, restante = self.inventario.vender(producto, cantidad)

        if aprobado:
            print(f"[SERVIDOR] Venta aprobada para {bodega}")
            print(f"[SERVIDOR] Stock restante {producto}: {restante}")
        else:
            print(f"[SERVIDOR] Stock insuficiente para {bodega}")

        return aprobado