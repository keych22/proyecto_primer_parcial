import csv, json, re, time
import os
from biblioteca_consola_ahorcado import *

# Lectura de datos desde el archivo JSON
with open(r"archivos\tematicas.json", 'r') as file:
    data = json.load(file)

lista_matematica = data["matematica"]
lista_programacion = data["programacion"]
lista_deportes = data["deportes"]
lista_tematicas = [lista_matematica, lista_programacion, lista_deportes]

# Selección de lista y palabra al azar
tematica = obtener_lista_al_azar(lista_tematicas)
palabra_adivinar = obtener_palabra_al_azar(tematica)

# Lectura de datos desde el archivo CSV
with open(r"archivos\configuraciones.csv", 'r') as file:
    # Leer el archivo CSV como un diccionario
    reader = csv.DictReader(file)
    # Iterar sobre las filas del CSV (en este caso solo hay una)
    for row in reader:
        # Obtener los valores de las variables
        intentos_restantes = int(row['intentos_restantes'])
        puntaje = int(row['puntaje'])
        tiempo_juego = int(row['tiempo_juego'])

# Usando Regex se crea una lista de guiones bajos, para representar cada letra de la palabra a adivinar
palabra_oculta = list(re.sub("[a-z]", "_" , palabra_adivinar))

resultados = {}
tiempo_inicio = time.time()

# Ciclo principal del juego
while intentos_restantes > 0:
    tiempo_actual = time.time()
    tiempo_transcurrido = int(tiempo_actual - tiempo_inicio)
    tiempo_restante = tiempo_juego - tiempo_transcurrido

    if tiempo_transcurrido >= tiempo_juego:
        print("Se ha agotado el tiempo.")
        perdio = True
        break

    print(f"\nTiempo restante: {tiempo_restante} segundos")

    print("\n")
    print(" ".join(palabra_oculta))
    try:
        letra = input("\nIngrese SÓLO una letra y presione la tecla enter: ").lower()
        if not letra.isalpha():
            raise ValueError("Por favor, ingrese solo letras del alfabeto.")
    except ValueError as e:
        print(e)
        continue

    if letra in palabra_adivinar:
        for i in range(len(palabra_adivinar)):
            if palabra_adivinar[i] == letra:
                palabra_oculta[i] = letra

        puntaje += 10

        if "_" not in palabra_oculta:
            puntaje += tiempo_restante
            print(" ".join(palabra_oculta))
            print(f"\nFelicitaciones, adivinaste la palabra secreta: {palabra_adivinar.upper()} --> Tu puntaje es {puntaje}")
            perdio = "no"
            break
        
    else:
        puntaje -= 5
        intentos_restantes -= 1
        dibujar_horca(intentos_restantes)
    
try:
    if perdio == "si":
        pass
except NameError:
        print(f"Lo siento, has perdido. La palabra era: {palabra_adivinar.upper()}")

# Para persistencia de datos con CSV

ruta_archivo = os.path.join("archivos", "resultados_consola.csv")

resultados["Tiempo_transcurrido"] = round(tiempo_transcurrido)
resultados["Tiempo_restante"] = round(tiempo_restante)
resultados["Score"] = puntaje 

# Abres el archivo CSV en modo escritura
with open(ruta_archivo, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames = resultados.keys())
    writer.writeheader()
    writer.writerow(resultados)
