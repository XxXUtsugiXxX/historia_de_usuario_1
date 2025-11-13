# iniciamos la lista vacia para agregarle los productos
inventario = []

#empezamos a crear las funciones

#en esta funcion solo pedimos los datos que seran agregados a la lista y los agregamos a la lista
def agregar (inventario):
    nombre = str(input("digita el nombre del producto: ")).lower()
    precio = int(input("digita el precio del producto: "))
    cantidad = int(input("digita la cantidad del producto: "))
    producto = {"nombre" :nombre,"precio": precio,"cantidad": cantidad}
    inventario.append(producto)
    
    
#en esta funcion mostramos todo lo que hemos ingresado a la lista
def Mostrar (inventario):
    for producto in inventario:      
        print(f"nombre: {producto ["nombre"]}, precio:{producto["precio"]}, cantidad:{producto["cantidad"]} ")
    else:
        print("inventario vacio")
        
#procedemos a hacer un calculo total del cada producto y cuanto valen todos los productos      
def Calcular (inventario):
    total = 0
    for calcular in inventario:      
        total = calcular["precio"] * calcular["cantidad"]
        print(total)
    
#aca lo unico que se hace es crear el menu 
while True:
    print("Menu principal")
    print("1. Agregar producto: ")
    print("2. Mostrar inventario: ")
    print("3. Calcular estadistica: ")
    print("4. salir")
    
# y por ultimo verificamos que los numeros que introduzca no sean menores a 1 ni mayores a 4
#en caso tal que pida un numero valido hasta que lo ingrese
#ya aca es donde empezamos tambien a llamar las funciones creadas
    opcion = int(input("digita una opcion de 1 a 4: "))
    if opcion < 1 or opcion > 4:
        opcion = int(input("digita una opcion  valida de 1 a 4: "))
        continue
    if opcion == 1:
        agregar(inventario)
    elif opcion == 2:
        Mostrar(inventario)
    elif opcion == 3:
        Calcular(inventario)
    else:
        print("saliste del menu")
        break
    
