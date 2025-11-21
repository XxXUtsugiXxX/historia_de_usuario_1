#en esta función agregamos los productos al inventario, 

def agregar (inventarioL):
    try:
        while True:
            nombre = input("Digita el nombre del producto: ").lower()

            if nombre.isalpha():  # nos ayuda a que solo sean letras 
                break
            else:
                print(" Error: solo letras, sin espacios ni símbolos.")

            #No ayuda a saber si un producto ya esciste, que solo se sume la cantidad que vamos a meter
        for producto in inventarioL:
            if producto["nombre"] == nombre:
                print("Producto ya existe, solo se sumara catidad")

                while True:
                    try:
                        cantidad = int(input("Digita la cantidad a sumar"))
                        if cantidad <= 0:
                            cantidad = int(input("Digita cantidad valida"))
                            continue
                        break
                    except ValueError:
                        print("ingrese un numero entero valido")

                producto["cantidad"] += cantidad
                print("producto actualizado")
                return
    except Exception as e:
        print("error inesperado", e)

    while True:
        precio = input("Digita el precio: ")

        if precio.isdigit():       #nos ayuda a que solo sean números
            precio = float(precio)
            break
        else:
            print("Ingresa solo números sin espacios ni símbolos.")
    
    while True:
        cantidad = input("Digita el precio: ")

        if cantidad.isdigit():       
            cantidad = int(cantidad)
            break
        else:
            print("Ingresa solo números sin espacios ni símbolos.")
        
    inventarioD = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventarioL.append(inventarioD)

#la función se encarga de mostrarnos todxo lo que hay en la lista

def Mostrar (inventarioL):
    try:
        if not inventarioL:
            print("inventario vacio")
            return
        for inventarioD in inventarioL:      
            print(f"nombre: {inventarioD ["nombre"]}, precio:{inventarioD["precio"]}, cantidad:{inventarioD["cantidad"]} ")
    except Exception as e:
        print("error inesperado: ", e)

#nos muestra algun producto en especifico

def consultar(inventarioL):
    try:    
        while True:
            producto_buscar = input("Digita el nombre del producto: ").lower()

            if producto_buscar.isalpha():  
                break
            else:
                print(" Error: solo letras, sin espacios ni símbolos.")
            return
        for producto in inventarioL:
            if producto["nombre"] == producto_buscar:
                print(f"nombre: {producto ["nombre"]}, precio:{producto["precio"]}, cantidad:{producto["cantidad"]} ")
                return
            else:
                print("Este producto no esta en la lista")
    except Exception as e:
        print("error inesperado: ", e)            

#la función nos ayuda a cambair ya sea la cantidad o el valor del precio

def actalizar(inventarioL):

    if not inventarioL:
        print("Lista vacia")
        return
    try:
        while True:
            producto_actualizar = input("Digita el nombre del producto: ").lower()

            if producto_actualizar.isalpha():  
                break
            else:
                print(" Error: solo letras, sin espacios ni símbolos.")
            return
        
        for producto in inventarioL:

            if producto["nombre"] == producto_actualizar:
                print(f"nombre: {producto ["nombre"]}, precio:{producto["precio"]}, cantidad:{producto["cantidad"]} ")
                opcion = int(input("digita 1 para cambiar cantidad\n 2 para cambiar precio\n para cambiar ambos pulsa 3: "))

                while opcion <= 0 or opcion > 3:
                    opcion = int(input("digita un numero solo de 1 a 3: "))

                if opcion == 1:
                    cantidadnew = int(input("ingresa cantidad nueva: "))
                    producto["cantidad"] = cantidadnew
                elif opcion == 2:
                    precionew = float(input("ingresa el precio nuevo: "))
                    producto["precio"] = precionew
                else:
                    precionew = float(input("ingresa el precio nuevo: "))
                    producto["precio"] = precionew
                    cantidadnew = int(input("ingresa cantidad nueva: "))
                    producto["cantidad"] = cantidadnew                    
                    
        
    except Exception as e:
        print("error inesperado: ", e)

#esta es la función que nos ayuda a eliminar cualquier producto del inventario

def eliminar(inventarioL):
    P_eliminar = input("ingresa el nombre del producto que quieres eliminar: ")

    for producto in inventarioL:

        if producto["nombre"] == P_eliminar:
            opcion = int(input(" 1. para eliminar\n 2. para mantener el producto\n "))

            while opcion < 1 or opcion > 2:
                opcion = int(input(" 1. para eliminar\n 2. para mantener el producto\n "))

            if opcion == 1:
                inventarioL.remove(producto)
                print(f"nombre: {producto ["nombre"]}, precio:{producto["precio"]}, cantidad:{producto["cantidad"]}, se ha eliminado exitosamente ")
            else:
                print("saliste al menu")
                break
        else:
            print("Producto no existe")

# en esta función hacemos todo el calculo de las estadisticas del inventario

def calcular(inventarioL):
    try:
        if not inventarioL:
            print("inventario vacio")
            return
        total_productos = len(inventarioL) #cauntos productos diferentes hay en la lista
        total_unidades = sum(p["cantidad"] for p in inventarioL) #sacamos todas las unidades del inventario
        valor_total = sum(p["precio"] * p["cantidad"] for p in inventarioL) #se usa para sacar el valor total del inventario
        mas_caro = max(inventarioL, key=lambda p: p["precio"]) #se usa para sacar el producto mas caro del inventario
        mas_barato = min(inventarioL, key=lambda p: p["precio"])#se usa para sacar el producto mas barato del inventario
        mas_stock = max(inventarioL, key=lambda p: p["cantidad"]) #se busca el producto con mayo stock

        print(f"\nTotal de productos diferentes: {total_productos}\n") #esto imprime todos los productos 
        print(f"Total de unidades: {total_unidades}\n") #imprimimos la cantidad total de todos los productos
        print(f"Valor total del inventario: {valor_total}\n") #esto imprime el valor total del inventario
        print(f"Producto más caro: {mas_caro['nombre']} (${mas_caro['precio']})\n") #aca imprimimos el producto mas caro
        print(f"Producto más barato: {mas_barato['nombre']} (${mas_barato['precio']})\n") # imprimimos el producto mas barato
        print(f"Producto con más stock: {mas_stock['nombre']} ({mas_stock['cantidad']})\n") #imprimimos el producto con mayor stock

    except Exception as e:
        print("Error inesperado:", e)