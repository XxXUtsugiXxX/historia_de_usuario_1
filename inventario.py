
#Se inicia pidiendo los 3 datos principales: nombre, precio y producto.
#tambien se ponr un .lower() para que todo lo tome en minuzcula

nombre = str(input("digita el nombre del producto: ")).lower()
precio = float(input("ingresa el precio del producto: "))
cantidad = int(input("ingresa la cantidad del producto: "))

#Aca verificamos que los datos sean validos (cantidad y precio)
#de que si nos ponen negativos muestre error y los pida nuevamente

while precio <= 0 or cantidad <= 0:
    if precio <=0:
        precio = float(input("ingresa un precio valido del producto: "))
    elif cantidad <= 0:
        cantidad = int(input("ingresa una cantidad valida del producto: "))
        
#Hacemos el calculo total de todo para poderlo imprimir
#importante hacerlo fuera del bucle para que si se guarde y no salga error al momento de imprimir
    
costo_total = precio * cantidad
    
#Aca ya solo imprimimos todas las variables con su cantidad asignada, nombre, precio, cantidad y costo total


print(f"Producto: {nombre} | Precio: {precio} | cantidad: {cantidad} | Total: {costo_total}")