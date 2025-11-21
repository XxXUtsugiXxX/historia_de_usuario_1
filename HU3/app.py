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
import archivos

#creamos una lista vacia donde se guardara todo
inventarioL = []

#mostramos el menu para que el usuario digite la opción que quiera
while True:
    print("\nMenu principal")
    print("1. Agregar producto: ")
    print("2. Mostrar inventario: ")
    print("3. Buscar producto: ")
    print("4. Actualizar producto: ")
    print("5. Eliminar producto: ")
    print("6. Calcular estadistica: ")
    print("7. Guardar en CSV: ")
    print("8. Cargar en CSV: ")
    print("9. salir\n")
    
#de acá para abajo solo se llaman las funciones y lo que se va a ejecutar de servicios
    opcion = int(input("digita una opcion de 1 a 9: "))
    if opcion < 1 or opcion > 9:
        opcion = int(input("digita una opcion  valida de 1 a 9: "))
        continue
    if opcion == 1:
        servicios.agregar(inventarioL)
    elif opcion == 2:
        servicios.Mostrar(inventarioL)
    elif opcion == 3:
        servicios.consultar(inventarioL)
    elif opcion == 4:
        servicios.actalizar(inventarioL)
    elif opcion == 5:
        servicios.eliminar(inventarioL)
    elif opcion == 6:
        servicios.calcular(inventarioL)        
    elif opcion == 7:
        archivos.exportar(inventarioL) 
    elif opcion == 8:
        inventarioL = archivos.cargar("inventario.csv")                                                 
    else:
        print("saliste del menu")
        break