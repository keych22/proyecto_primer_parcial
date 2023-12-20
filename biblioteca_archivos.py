import json

def cargar_datos_json(ruta: str) -> dict | Exception:
    """
    Carga datos desde un archivo JSON.

    Argumento:
        ruta (str): La ruta del archivo JSON.

    Retorno:
        dict or None: Los datos cargados desde el archivo JSON, o None si ocurrió un error.
    """
    mensaje_error = None
    datos = None

    try:
        with open(ruta, 'r') as file:
            datos = json.load(file)
    except json.JSONDecodeError as e:
        mensaje_error = f"Error al cargar el archivo JSON: {e}"
    except FileNotFoundError as e:
        mensaje_error = f"El archivo no fue encontrado: {e}"
    except Exception as e:
        mensaje_error = f"Otro tipo de error: {e}"
    finally:
        file.close()

    return datos, mensaje_error