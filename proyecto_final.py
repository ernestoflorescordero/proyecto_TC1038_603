import random

# Constantes a nivel de módulo
CARAS_DADO = 6
L = 2


def simular_tirada(puntaje_objetivo, nombre_jugador):
    """Simula el lanzamiento de dos dados y evalua si se alcanza la meta."""
    dado1 = random.randint(1, CARAS_DADO)
    dado2 = random.randint(1, CARAS_DADO)
    total = dado1 + dado2

    # Evaluacion de resultado
    if total >= puntaje_objetivo:
        print("Felicidades " + nombre_jugador + ", tus dados sumaron "
              + str(total) + " y alcanzaste la meta!")
    else:
        print("Mala suerte " + nombre_jugador + ", solo sumaste "
              + str(total) + " puntos.")

    return total


# Flujo principal interactivo
nombre = input("Ingrese el nombre del jugador: ")
meta = int(input("Cual es el numero meta que deseas alcanzar (2 al 12)?: "))
resultado = simular_tirada(meta, nombre)
print(resultado)