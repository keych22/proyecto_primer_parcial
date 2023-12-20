import pygame, sys, random

def obtener_lista_al_azar(lista_tematicas: list[list]) -> list:
    """
    Obtiene una lista al azar de una lista de listas.\n
    Argumento:
        lista_de_listas: Lista de listas.\n
    Retorno:
        Una lista al azar de la lista de listas.
    """
    return random.choice(lista_tematicas)

def obtener_palabra_al_azar(lista_palabras: list[str]) -> str:
    """
    Obtiene una palabra al azar de una lista.\n
    Argumento:
        lista_palabras: Lista de string.\n
    Retorno:
        Una palabra al azar de la lista.
    """
    return random.choice(lista_palabras)

def categorizar_palabra(palabra: str) -> str:
    """
    Clasifica una palabra en función de la lista o categoria a la que pertenece.\n
    Argumento:
        una_palabra: Un string.\n
    Retorno:
        Un string que indica la categoria de la palabra ingresada.
    """
    matematicas = ["exponente", "raiz", "logaritmo", "pitagoras"]
    programacion = ["burbujeo", "excepcion", "bucle", "archivo"]

    if palabra in matematicas:
        return "matematicas"
    elif palabra in programacion:
        return "programacion"
    else:
        return "deportes"

def dibujar_ahorcado(intentos: int) -> pygame.Surface:
    """
    Mostrar la fase del ahorcado dependiendo del número de errores cometidos.\n
    Argumento:
        un_número: Un entero.\n
    Retorno:
        Una imagen que representa la cantidad de desaciertos en dicho momento.
    """
    if intentos == 7:
        dibujo_ahorcado = pygame.image.load(r"imagenes\imagen_0.jpg")
        dibujo_ahorcado = pygame.transform.scale(dibujo_ahorcado, (200, 200))
        return dibujo_ahorcado
    elif intentos == 6:
        dibujo_ahorcado = pygame.image.load(r"imagenes\imagen_1.jpg")
        dibujo_ahorcado = pygame.transform.scale(dibujo_ahorcado, (200, 200))
        return dibujo_ahorcado
    elif intentos == 5:
        dibujo_ahorcado = pygame.image.load(r"imagenes\imagen_2.jpg")
        dibujo_ahorcado = pygame.transform.scale(dibujo_ahorcado, (200, 200))
        return dibujo_ahorcado
    elif intentos == 4:
        dibujo_ahorcado = pygame.image.load(r"imagenes\imagen_3.jpg")
        dibujo_ahorcado = pygame.transform.scale(dibujo_ahorcado, (200, 200))
        return dibujo_ahorcado
    elif intentos == 3:
        dibujo_ahorcado = pygame.image.load(r"imagenes\imagen_4.jpg")
        dibujo_ahorcado = pygame.transform.scale(dibujo_ahorcado, (200, 200))
        return dibujo_ahorcado
    elif intentos == 2:
        dibujo_ahorcado = pygame.image.load(r"imagenes\imagen_5.jpg")
        dibujo_ahorcado = pygame.transform.scale(dibujo_ahorcado, (200, 200))
        return dibujo_ahorcado
    elif intentos == 1:
        dibujo_ahorcado = pygame.image.load(r"imagenes\imagen_6.jpg")
        dibujo_ahorcado = pygame.transform.scale(dibujo_ahorcado, (200, 200))
        return dibujo_ahorcado
    else:
        dibujo_ahorcado = pygame.image.load(r"imagenes\imagen_7.jpg")
        dibujo_ahorcado = pygame.transform.scale(dibujo_ahorcado, (200, 200))
        return dibujo_ahorcado
    
def solicitar_inicio(ventana, color_uno, color_dos, fuente_uno, fuente_dos, texto_reglas):
    while True:
        ventana.fill(color_uno)
        evento = pygame.event.wait()
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
                if 310 <= evento.pos[0] <= 430 and 452 <= evento.pos[1] <= 500:
                    break 
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                break

        imagen_fondo = pygame.image.load(r"imagenes\imagen_9.jpg")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (750, 250))
        ventana.blit(imagen_fondo, (0, 0))

        boton_jugar = pygame.image.load(r"imagenes\imagen_10.jpg")
        boton_jugar = pygame.transform.scale(boton_jugar, (120, 50))
        ventana.blit(boton_jugar, (310, 450))

        mensaje_inicio = fuente_uno.render("Presiona enter o haz click para jugar", True, color_dos)
        ventana.blit(mensaje_inicio, (170, 510) )
    
        lineas_reglas = texto_reglas.split('\n')
        y = 250  # Altura inicial para imprimir las líneas

        for linea in lineas_reglas:
            ventana.blit(fuente_dos.render(linea, True, color_dos), (10, y))
            y += fuente_dos.get_linesize()

        pygame.display.update()

def dibujar_letras(lista_letras, fuente, ventana, color):
    posicion_x = 170
    posicion_y = 470

    for i in range(len(lista_letras)):
        boton_letra = fuente.render(lista_letras[i], True, color)
        ventana.blit(boton_letra, (posicion_x, posicion_y))

        # Actualiza las posiciones para la siguiente letra
        posicion_x += 35
        if i == 12:  # Cambia de fila después de mostrar las primeras 13 letras
            posicion_x = 130
            posicion_y += 40
            posicion_x += 40

def inicializar_variables():
    intentos_restantes = 7
    tiempo_restante = 60
    gano = False
    puntaje = 0
    lista_letras_incorrectas = []
    lista_letras_acertadas = []     
    return intentos_restantes, tiempo_restante, gano, puntaje, lista_letras_incorrectas, lista_letras_acertadas

def variables_estado():
    letra_fue_usada = False
    letra_acertada = False
    juego_iniciado = False
    juego_terminado = False
    reiniciar = False
    mensaje_excepcion = ""
    return letra_fue_usada, letra_acertada, juego_iniciado, juego_terminado, reiniciar, mensaje_excepcion

def continuar_jugando(ventana: pygame.Surface) -> pygame.Surface:
    continuar_juego = pygame.image.load(r"imagenes\imagen_11.jpg")
    ventana.blit(continuar_juego, (400, 230))

def dibujar_boton_inicio(ventana, fuente, color_uno, color_dos):
    boton_iniciar = fuente.render("Presione para iniciar juego", True, color_uno, color_dos)
    ventana.blit(boton_iniciar, (250, 250))

def obtener_letra_por_mouse(evento):
    """Devuelve la letra seleccionada por el usuario, o None si el usuario no seleccionó ninguna letra.\n
    Args:
        evento: El evento pygame.MOUSEBUTTONDOWN.
    Retorno:
        str: La letra seleccionada, o None.
    """
    letra = None
    if 171 <= evento.pos[0] <= 190 and 474 <= evento.pos[1] <= 498:
            letra = "a"
    if 208 <= evento.pos[0] <= 222 and 474 <= evento.pos[1] <= 498:
        letra = "b"
    if 240 <= evento.pos[0] <= 259 and 474 <= evento.pos[1] <= 498:
        letra = "c"
    if 277 <= evento.pos[0] <= 295 and 474 <= evento.pos[1] <= 498:
        letra = "d"
    if 313 <= evento.pos[0] <= 331 and 474 <= evento.pos[1] <= 498:
        letra = "e"
    if 349 <= evento.pos[0] <= 367 and 474 <= evento.pos[1] <= 498:
        letra = "f"
    if 385 <= evento.pos[0] <= 403 and 474 <= evento.pos[1] <= 498:
        letra = "g"
    if 421 <= evento.pos[0] <= 439 and 474 <= evento.pos[1] <= 498:
        letra = "h"
    if 448 <= evento.pos[0] <= 461 and 474 <= evento.pos[1] <= 498:
        letra = "i"
    if 486 <= evento.pos[0] <= 500 and 474 <= evento.pos[1] <= 498:
        letra = "j"
    if 522 <= evento.pos[0] <= 539 and 474 <= evento.pos[1] <= 498:
        letra = "k"
    if 558 <= evento.pos[0] <= 570 and 474 <= evento.pos[1] <= 498:
        letra = "l"
    if 591 <= evento.pos[0] <= 614 and 474 <= evento.pos[1] <= 498:
        letra = "m"
    if 173 <= evento.pos[0] <= 190 and 514 <= evento.pos[1] <= 537:
        letra = "n"
    if 205 <= evento.pos[0] <= 229 and 514 <= evento.pos[1] <= 537:
        letra = "o"
    if 241 <= evento.pos[0] <= 259 and 514 <= evento.pos[1] <= 537:
        letra = "p"
    if 275 <= evento.pos[0] <= 299 and 514 <= evento.pos[1] <= 537:
        letra = "q"
    if 313 <= evento.pos[0] <= 329 and 514 <= evento.pos[1] <= 537:
        letra = "r"
    if 346 <= evento.pos[0] <= 363 and 514 <= evento.pos[1] <= 537:
        letra = "s"
    if 382 <= evento.pos[0] <= 396 and 514 <= evento.pos[1] <= 537:
        letra = "t"
    if 415 <= evento.pos[0] <= 435 and 514 <= evento.pos[1] <= 537:
        letra = "u"
    if 449 <= evento.pos[0] <= 469 and 514 <= evento.pos[1] <= 537:
        letra = "v"
    if 485 <= evento.pos[0] <= 512 and 514 <= evento.pos[1] <= 537:
        letra = "w"
    if 521 <= evento.pos[0] <= 539 and 514 <= evento.pos[1] <= 537:
        letra = "x"
    if 555 <= evento.pos[0] <= 574 and 514 <= evento.pos[1] <= 537:
        letra = "y"
    if 591 <= evento.pos[0] <= 608 and 514 <= evento.pos[1] <= 537:
        letra = "z"
    return letra

def salir_del_juego():
    pygame.quit()
    sys.exit()

        
