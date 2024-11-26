# Importar las clases desde sus respectivos archivos
from cactus import Cactus
from rosa import Rosa
from orquidea import OrquideaExotica

def main():
    # Crear y mostrar información del Cactus
    print("\n--- Información del Cactus ---")
    cactus = Cactus(
        nombre="Cactus",
        resistencia_sequia="Alta",
        almacenamiento_agua="Capaz de almacenar grandes cantidades de agua en sus tallos"
    )
    cactus.mostrar_info_completa()

    # Crear y mostrar información de la Rosa
    print("\n--- Información de la Rosa ---")
    rosa = Rosa(
        nombre="Rosa Roja",
        uso_cosmetico="Extracto utilizado en productos para el cuidado de la piel",
        uso_simbolico="Símbolo de amor y pasión"
    )
    rosa.mostrar_info_completa()

    # Crear y mostrar información de la Orquídea Exótica
    print("\n--- Información de la Orquídea Exótica ---")
    orquidea_exotica = OrquideaExotica(
        nombre="Orquídea Exótica Tropical",
        exotica="Con una apariencia única, generalmente simétrica.",  # Indicamos que es exótica
        raices_aereas="Muchas orquídeas tienen raíces que crecen fuera del suelo."  # Indicamos que tiene raíces aéreas
    )
    orquidea_exotica.mostrar_info_completa()

if __name__ == "__main__":
    main()
