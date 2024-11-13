# Importar las clases desde sus respectivos archivos
from cactus import Cactus
from rosa import Rosa
from fertilizante import OrquideaExotica

def main():
    # Crear y mostrar información del Cactus
    print("\n--- Información del Cactus ---")
    cactus = Cactus("Cactus Espinoso")
    cactus.mostrar_info_completa()

    # Crear y mostrar información de la Rosa
    print("\n--- Información de la Rosa ---")
    rosa = Rosa("Rosa Roja")
    rosa.mostrar_info_completa()

    # Crear y mostrar información de la Orquídea Exótica
    print("\n--- Información de la Orquídea Exótica ---")
    orquidea_exotica = OrquideaExotica("Orquídea Exótica Tropical")
    orquidea_exotica.mostrar_info_completa()

if __name__ == "__main__":
    main()
