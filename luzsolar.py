class Luz:
    def __init__(self, luz_solar="Alta"):
        # Atributos comunes para todas las plantas
        self.luz_solar = luz_solar  # Atributo específico para la luz solar

    # Método para mostrar la información común de las plantas
    def mostrar_info(self):
        print(f"Luz Solar: {self.luz_solar}")
