import random

def obtener_palabra_al_azar(lista_palabras: list[str]) -> str:
    """
    Obtiene una palabra al azar de una lista.\n
    Argumento:
        lista_palabras: Lista de string.\n
    Retorno:
        Una palabra al azar de la lista.
    """
    return random.choice(lista_palabras)

def obtener_lista_al_azar(lista_de_listas: list[list]) -> list:
    """
    Obtiene una lista al azar de una lista de listas.\n
    Argumento:
        lista_de_listas: Lista de listas.\n
    Retorno:
        Una lista al azar de la lista de listas.
    """
    return random.choice(lista_de_listas)

def dibujar_horca(intentos: int) -> None:
    """
    Dibuja una estructura.\n 
    Argumento:
        intentos: Los intentos para acertar las letras de la palabra\n
    Retorno:
        La imagen de la estructura de la horca a medida que se desacierta.
    """
    # Esqueleto
    if intentos == 5:
        print(" ___________")
        print("|           |")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|_          ")

    # Partes de la cabeza
    if intentos == 4:
        print(" __________")
        print("|       |  ")
        print("|       |  ")
        print("|     (__)|")
        print("|_         ")

    # Partes del cuerpo
    if intentos == 3:
        print(" ___________ ")
        print("|       |   ")
        print("|       |   ")
        print("|     (__)|")
        print("|       |  ")
        print("|_         ")

    # Partes de los brazos
    if intentos == 2:
        print(" ___________ ")
        print("|       |   ")
        print("|       |   ")
        print("|     (__)|")
        print("|       |  ")
        print("|       0  ")
        print("|_         ")

    # Partes de las piernas
    if intentos == 1:
        print(" ___________ ")
        print("|       |   ")
        print("|       |   ")
        print("|     (__)|")
        print("|       |  ")
        print("|       0  ")
        print("|      /   ")
        print("|_         ")

    # Partes de los pies
    if intentos == 0:
        print(" ___________ ")
        print("|       |   ")
        print("|       |   ")
        print("|     (__)|")
        print("|       |  ")
        print("|       0  ")
        print("|      / \ ")
        print("|_         ")





