

def agregar (inventarioL):
    nombre = str(input("digita el nombre del producto: ")).lower()
    precio = int(input("digita el precio del producto: "))
    cantidad = int(input("digita la cantidad del producto: "))
    inventarioD = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventarioL.append(inventarioD)

def Mostrar (inventarioL):
    for inventarioD in inventarioL:      
        print(f"nombre: {inventarioD ["nombre"]}, precio:{inventarioD["precio"]}, cantidad:{inventarioD["cantidad"]} ")
    else:
        print("inventario vacio")

def eliminar_estudiante():
    try:
        documento_buscar = int(input("Ingrese el documento del estudiante a actualizar: "))
    except ValueError:
        print("digite un numero valido")
        return
    for estudiante in estudiantes:
        if estudiante["documento"] == documento_buscar:
            print()
            return