import pygame, sys, re, json, csv, os
from mensajes import texto_reglas
from biblioteca_pygame_ahorcado import *
from biblioteca_archivos import *
from configuraciones import *

# Inicio pygame
pygame.init()

# Configuraciones iniciales de entorno
reloj = pygame.time.Clock()

PANTALLA = pygame.display.set_mode((ANCHO_X, ALTO_Y))
pygame.display.set_caption("Juedo del ahorcado")

icono = pygame.image.load(r"imagenes\ahorcado.jpg")
pygame.display.set_icon(icono)


fuente = pygame.font.SysFont("Arial", 25)
otra_fuente = pygame.font.SysFont("Arial", 13)
fuente_mensaje = pygame.font.SysFont("Arial", 20)

texto_puntuacion = fuente.render(
    "Puntuación acumulada: ", True, GRIS, AZUL_CLARO)

datos, mensaje_error = cargar_datos_json(r"archivos\tematicas.json")

lista_matematica = datos["matematica"]
lista_programacion = datos["programacion"]
lista_deportes = datos["deportes"]
lista_tematicas = [lista_matematica, lista_programacion, lista_deportes]

# Selección de lista y palabra al azar
lista_palabras = obtener_lista_al_azar(lista_tematicas)
palabra_adivinar = obtener_palabra_al_azar(lista_palabras)
tematica = categorizar_palabra(palabra_adivinar)

# Uso de Regex
letras_ocultas = list(re.sub("[a-z]", "_", palabra_adivinar))

# Devuele valores iniciales
intentos_restantes, tiempo_restante, gano, puntaje, lista_letras_incorrectas, lista_letras_acertadas = inicializar_variables()

# Mensajes
mensaje_letras = "Haga click sobre una letra de la lista\n de abajo o seleccionela del teclado"
mensaje_letra_usada = fuente.render("", True, GRIS, AZUL_CLARO)
mensaje_letra_acertada = fuente.render("", True, GRIS, AZUL_CLARO)
mensaje_perdido = fuente.render("", True, GRIS, AZUL_CLARO)

# Boton inicio
dibujar_boton_inicio(PANTALLA, fuente, GRIS, AZUL_CLARO)

solicitar_inicio(PANTALLA, NEGRO, BLANCO, fuente, otra_fuente, texto_reglas)

resultados = {}
tiempo_inicial = pygame.time.get_ticks()

while True:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            salir_del_juego()

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if (420 <= evento.pos[0] <= 490 and 272 <= evento.pos[1] <= 312) and reiniciar:
                lista_palabras = obtener_lista_al_azar(lista_tematicas)
                palabra_adivinar = obtener_palabra_al_azar(lista_palabras)
                tematica = categorizar_palabra(palabra_adivinar)
                letras_ocultas = list(re.sub("[a-z]", "_", palabra_adivinar))
                letra_fue_usada, letra_acertada, juego_iniciado, juego_terminado, reiniciar, mensaje_excepcion = variables_estado()
                intentos_restantes, tiempo_restante, gano, puntaje, lista_letras_incorrectas, lista_letras_acertadas = inicializar_variables()
                tiempo_inicial = pygame.time.get_ticks()

            elif 512 <= evento.pos[0] <= 585 and 272 <= evento.pos[1] <= 312:
                salir_del_juego()

        if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
            letra = pygame.key.name(evento.key).lower(
            ) if evento.type == pygame.KEYDOWN else obtener_letra_por_mouse(evento)
            mensaje_excepcion = ""

            try:
                if letra is None:
                    raise TypeError("Haga click sobre la letra")

                if not letra.isalpha():
                    raise ValueError(
                        "Debe ingresar una letra, no un número ni otro caracter especial")

                if letra in lista_letras_incorrectas:
                    mensaje_letra_usada = fuente.render(
                        "Letra incorrecta, ya intentada", True, ROJO)
                    letra_fue_usada = True
                    letra_acertada = False

                elif letra in lista_letras_acertadas:
                    mensaje_letra_acertada = fuente.render(
                        "Letra correcta, ya la uso en la palabra", True, ROJO)
                    letra_acertada = True
                    letra_fue_usada = False

                elif letra not in lista_letras_incorrectas and letra not in palabra_adivinar:
                    if not juego_terminado:
                        puntaje -= 5
                        intentos_restantes -= 1
                        lista_letras_incorrectas.append(letra)
                        letra_fue_usada = False
                        letra_acertada = False
                else:
                    for i in range(len(palabra_adivinar)):
                        if palabra_adivinar[i] == letra and not juego_terminado:
                            letras_ocultas[i] = letra
                            lista_letras_acertadas.append(letra)
                            letra_fue_usada = False
                            letra_acertada = False
                            puntaje += 10

                    if "_" not in letras_ocultas:
                        puntaje += int(tiempo_restante)
                        mensaje_felicitaciones = fuente.render(
                            "¡Felicitaciones adivinaste la palabra secreta!", True, VERDE, AZUL_CLARO)
                        gano = True
                        juego_terminado = True

            except BaseException as e:
                mensaje_excepcion = str(e)

    PANTALLA.fill(AZUL_CLARO)

    dibujar_letras(abecedario, fuente, PANTALLA, NEGRO)

    mensaje_tematica = fuente.render(f"Temática: {tematica}", True, GRIS)
    PANTALLA.blit(mensaje_tematica, (410, 20))

    if not gano and intentos_restantes > 0 and tiempo_restante > 0:
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = (tiempo_actual - tiempo_inicial) * 0.001
        tiempo_restante = (60 - tiempo_transcurrido)

        mostrar_tiempo_restante = fuente.render(
            str(int(tiempo_restante)), False, GRIS, AZUL_CLARO)
        PANTALLA.blit(mostrar_tiempo_restante, (460, 190))

        PANTALLA.blit(fuente.render("Tiempo restante", True, GRIS), (390, 150))
        dibujo = dibujar_ahorcado(intentos_restantes)
        PANTALLA.blit(dibujo, (90, 150))

        lineas_mensajes = mensaje_letras.split('\n')
        y = 300  # Altura inicial para imprimir las líneas

        for linea in lineas_mensajes:
            PANTALLA.blit(fuente_mensaje.render(linea, True, ROJO), (350, y))
            y += fuente_mensaje.get_linesize()

    if tiempo_restante < 0:
        juego_terminado = True
        reiniciar = True

        mensaje_perdido = fuente.render(
            "¡Tiempo agotado, perdiste!", True, ROJO, AZUL_CLARO)
        PANTALLA.blit(mensaje_perdido, (340, 180))

        palabra_secreta = fuente.render(
            f"La palabra secreta era: {palabra_adivinar.upper()}", True, GRIS)
        PANTALLA.blit(palabra_secreta, (40, 400))

        ultimo_tiempo_restante = tiempo_restante
        mostrar_ultimo_tiempo = fuente.render(
            "Tiempo restante: " + str(int(ultimo_tiempo_restante)), True, GRIS)
        PANTALLA.blit(mostrar_ultimo_tiempo, (390, 150))

        dibujo = dibujar_ahorcado(0)
        PANTALLA.blit(dibujo, (90, 150))

        continuar_jugando(PANTALLA)

    if intentos_restantes == 0:
        juego_terminado = True
        reiniciar = True

        palabra_secreta = fuente.render(
            f"La palabra secreta era: {palabra_adivinar.upper()}", True, GRIS)
        PANTALLA.blit(palabra_secreta, (40, 100))

        perdiste = fuente.render(
            "Perdiste, agotaste los 7 intentos permitidos", True, ROJO)
        PANTALLA.blit(perdiste, (140, 405))

        ultimo_tiempo_restante = tiempo_restante
        mostrar_ultimo_tiempo = fuente.render(
            "Tiempo restante: " + str(int(ultimo_tiempo_restante)), True, GRIS)
        PANTALLA.blit(mostrar_ultimo_tiempo, (400, 150))

        dibujo = dibujar_ahorcado(0)
        PANTALLA.blit(dibujo, (90, 150))

        continuar_jugando(PANTALLA)

    if gano:
        reiniciar = True
        ultimo_tiempo_restante = tiempo_restante
        mostrar_ultimo_tiempo = fuente.render(
            "Tiempo restante: " + str(int(ultimo_tiempo_restante)), True, GRIS)
        PANTALLA.blit(mostrar_ultimo_tiempo, (390, 150))

        PANTALLA.blit(mensaje_felicitaciones, (130, 400))

        dibujo_ahorcado = pygame.image.load(r"imagenes\imagen_8.jpg")
        dibujo = pygame.transform.scale(dibujo_ahorcado, (200, 200))
        PANTALLA.blit(dibujo, (90, 150))

        continuar_jugando(PANTALLA)

    if mensaje_excepcion:
        PANTALLA.blit(fuente.render(mensaje_excepcion, True, NEGRO), (20, 435))
    elif mensaje_error:
        PANTALLA.blit(fuente.render(mensaje_error, True, NEGRO), (20, 435))

    PANTALLA.blit(texto_puntuacion, (40, 20))
    PANTALLA.blit(fuente.render(str(puntaje), True, GRIS), (325, 20))

    if letra_fue_usada and not juego_terminado:
        PANTALLA.blit(mensaje_letra_usada, (20, 400))

    if letra_acertada and not juego_terminado:
        PANTALLA.blit(mensaje_letra_acertada, (30, 410))

    palabra_mostrada = fuente.render("  ".join(letras_ocultas), True, GRIS,)
    PANTALLA.blit(palabra_mostrada, (90, 360))

    letras_usadas_texto = fuente.render(
        "Letras incorrectas usadas: " + ", ".join(lista_letras_incorrectas), True, GRIS)
    PANTALLA.blit(letras_usadas_texto, (40, 60))

    pygame.display.update()
    reloj.tick(FPS)

    # Para persistencia de datos con CSV
    ruta_archivo = os.path.join("archivos", "resultados_pygame.csv")

    resultados["Tiempo_transcurrido"] = round(tiempo_transcurrido)
    resultados["Tiempo_restante"] = round(tiempo_restante)
    resultados["Score"] = puntaje

    # Abres el archivo CSV en modo escritura
    with open(ruta_archivo, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=resultados.keys())
        writer.writeheader()
        writer.writerow(resultados)

