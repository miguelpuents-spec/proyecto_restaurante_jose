import json
import os

# Nombre del archivo físico donde se guardará la información
ARCHIVO = "reservas_restaurante.json"

def cargar_datos():
    """Carga las reservas desde el disco duro al iniciar el programa."""
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []  # Si el archivo no existe, devuelve una lista vacía

def guardar_datos(reservas):
    """Escribe la lista de reservas en el archivo para que sea persistente.
    Se llama automáticamente después de cada operación para evitar pérdida de datos."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(reservas, f, indent=4, ensure_ascii=False)
