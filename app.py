# 2. Estructura de datos y modularización:
# Mantenga un inventario en memoria como lista de diccionarios , donde cada producto tenga:
# {"nombre": str, "precio": float, "cantidad": int}
# Crea un archivo principal app.py y un módulo servicios.py (o nombres equivalentes) con funciones:
# agregar_producto(inventario, nombre, precio, cantidad)
# mostrar_inventario(inventario)
# buscar_producto(inventario, nombre) → retorna el dict o Ninguno
# _producto(inventario, actualizar nombre, nuevo_precio=None, nueva_cantidad=None)
# eliminar_producto(inventario, nombre)
# calcular_estadisticas(inventario) → retorna tupla/dict con métricas
# Documenta cada función con docstring (qué hace, parámetros, retorno) y agrega comentarios breves.

import servicios

inventarioL = []

while True:
    print("Menu principal")
    print("1. Agregar producto: ")
    print("2. Mostrar inventario: ")
    print("3. Buscar producto: ")
    print("4. Actualizar producto: ")
    print("5. Eliminar producto: ")
    print("6. Calcular estadistica: ")
    print("7. salir")
    

    opcion = int(input("digita una opcion de 1 a 4: "))
    if opcion < 1 or opcion > 7:
        opcion = int(input("digita una opcion  valida de 1 a 4: "))
        continue
    if opcion == 1:
        servicios.agregar(inventarioL)
    elif opcion == 2:
        servicios.Mostrar(inventarioL)
    # elif opcion == 3:
    #     Calcular(inventario)
    # else:
    #     print("saliste del menu")
    #     break