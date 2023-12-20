import pygame

FPS = 5
ANCHO_X = 750
ALTO_Y = 550

AZUL_CLARO = (0, 180, 255)
BLANCO = (255, 255, 255)
GRIS = (67, 75, 77)
VERDE = (0, 150, 20)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Variables de estado
letra_fue_usada = False
letra_acertada = False
juego_iniciado = False
juego_terminado = False
reiniciar = False
mensaje_excepcion = ""
