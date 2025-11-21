import csv
# Guarda el inventario en un archivo CSV. inventarioL: lista de diccionarios con:
#     - nombre (str)
#     - precio (float)
#     - cantidad (int)
def exportar(inventarioL, nombre_archivo="inventario.csv"):
    """
    Exporta el inventario a un archivo CSV.
    """
    try:
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            columnas = ["nombre", "precio", "cantidad"]
            writer = csv.DictWriter(archivo, fieldnames=columnas)
            writer.writeheader()
            writer.writerows(inventarioL)

        print("Inventario exportado correctamente.")

    except Exception as e:
        print("Error al exportar CSV:", e)

#  Carga un inventario desde un archivo CSV y lo devuelve como lista de diccionarios.

def cargar(nombre_archivo="inventario.csv"):
    """
    Carga datos desde un archivo CSV y devuelve una lista de diccionarios.
    """
    inventarioL = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)
            
            for fila in reader:
                inventarioL.append({
                    "nombre": fila["nombre"].lower(),
                    "precio": float(fila["precio"]),
                    "cantidad": int(fila["cantidad"])
                })

        print("Inventario cargado correctamente.")
        return inventarioL

    except FileNotFoundError:
        print("El archivo no existe, se creará cuando exportes.")
        return []

    except Exception as e:
        print("Error al cargar CSV:", e)
        return []