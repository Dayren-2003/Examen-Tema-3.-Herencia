class Planta:
    def __init__(self, nombre, tipo):
        # Atributos que definen la planta
        self.nombre = nombre
        self.tipo = tipo

    def mostrar_info(self):
        # Método para mostrar la información de la planta
        print(f"\nPlanta: {self.nombre}")
        print(f"Tipo: {self.tipo}")
