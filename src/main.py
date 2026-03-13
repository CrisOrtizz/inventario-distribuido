from servidor import ServidorCentral
from bodega import Bodega


def main():

    print("\n--- Simulación Sistema Distribuido de Inventario ---\n")

    servidor = ServidorCentral()

    bodega_norte = Bodega("Bodega Norte", servidor)
    bodega_centro = Bodega("Bodega Centro", servidor)
    bodega_industrial = Bodega("Bodega Industrial", servidor)

    bodega_norte.start()
    bodega_centro.start()
    bodega_industrial.start()

    bodega_norte.join()
    bodega_centro.join()
    bodega_industrial.join()

    print("\n--- Simulación finalizada ---")


if __name__ == "__main__":
    main()