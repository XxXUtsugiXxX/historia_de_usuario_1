from datetime import date, datetime

booksL = [
    {
        "nombre": "principe de percia",
        "autor": "juan",
        "categoria": "aventura",
        "precio_unitario": 3000,
        "stock": 10,
    },
    {
        "nombre": "narnia",
        "autor": "felipe",
        "categoria": "aventura, accion",
        "precio_unitario": 120,
        "stock": 30,
    },
    {
        "nombre": "tron",
        "autor": "pablo",
        "categoria": "carreras",
        "precio_unitario": 1500,
        "stock": 15,
    },
    {
        "nombre": "principe de persia",
        "autor": "juanito",
        "categoria": "aventura, accion",
        "precio_unitario": 200,
        "stock": 20,
    },
    {
        "nombre": "psicologia oscura",
        "autor": "andres",
        "categoria": "psicologia",
        "precio_unitario": 80,
        "stock": 25,
    }
]

# Lista donde se guardan las ventas
sales = []


def ask_number(texto, tipo=float):
    """Securely request a number from the user.
        If they enter an invalid number, request it again.."""
    while True:
        try:
            valor = tipo(input(texto))
            return valor
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")


def add_product():
    """Register a new product in the inventory."""
    print("register product")

    name = input("Nombre del producto: ")
    author = input("Autor: ")
    category = input("Categoría: ")
    unit_price = ask_number("Precio unitario: ", float)
    stock = ask_number("Cantidad en stock: ", int)

    producto = {
        "nombre": name,
        "autor": author,
        "categoria": category,
        "precio_unitario": unit_price,
        "stock": stock,
    }

    booksL.append(producto)
    print("✔ Producto agregado exitosamente.")


def see_inventory():
    """Displays all products in inventory."""
    print("inventario")
    for i, p in enumerate(booksL):
        print(f"{i+1}. {p['nombre']} | Autor: {p['autor']} | Stock: {p['stock']} | Precio: ${p['precio_unitario']}")


def update_product():
    """Modify an existing product."""
    see_inventory()
    name = ask_number("Seleccione número de producto a actualizar: ", int) - 1

    if name not in range(len(booksL)):
        print("Número inválido.")
        return

    print("\nSi deja un campo vacío, se mantiene el valor actual.\n")

    producto = booksL[name]

    nuevo_nombre = input(f"Nuevo nombre ({producto['nombre']}): ") or producto["nombre"]
    nuevo_autor = input(f"Nueva autor ({producto['autor']}): ") or producto["autor"]
    nueva_categoria = input(f"Nueva categoría ({producto['categoria']}): ") or producto["categoria"]

    precio = input(f"Nuevo precio ({producto['precio_unitario']}): ")
    stock = input(f"Nuevo stock ({producto['stock']}): ")

    producto["nombre"] = nuevo_nombre
    producto["autor"] = nuevo_autor
    producto["categoria"] = nueva_categoria
    producto["precio_unitario"] = float(precio) if precio else producto["precio_unitario"]
    producto["stock"] = int(stock) if stock else producto["stock"]

    print("Producto actualizado correctamente.")


def delete_product():
    """Remove a product from the inventory."""
    see_inventory()
    name = ("Digita el nombre del libro a eliminar: ")

    if name not in booksL:
        print("Nombre no esta en la lista.")
        return

    eliminado = booksL.pop(name)
    print(f"✔ Producto '{eliminado['nombre']}' eliminado.")


def register_product():
    hora = datetime.now()
    """Record a sale and automatically update the inventory."""
    print("Registrar venta")

    cliente = input("Nombre del cliente: ")

    see_inventory()
    name = ("digite el nombre del libro: ")

    if name not in booksL:
        print("nombre inválido.")
        return

    producto = booksL[name]

    cantidad = ask_number("Cantidad vendida: ", int)

    if cantidad > producto["stock"]:
        print("Stock insuficiente. No se puede realizar la venta.")
        return

    descuento = ask_number("Descuento aplicado (%): ", float)

    # Actualiza stock
    producto["stock"] -= cantidad

    total = (producto["precio_unitario"] * cantidad) * (1 - descuento / 100)

    venta = {
        "cliente": cliente,
        "producto": producto["nombre"],
        "cantidad": cantidad,
        "descuento": descuento,
        "fecha": hora,
        "total": total
    }

    sales.append(venta)
    print("Se realizo y registro una venta.")


def see_sale():
    """Displays the complete sales history."""
    print("historial de ventas")
    for v in sales:
        print(f"{v['fecha']} - {v['producto']} x{v['cantidad']} | Cliente: {v['cliente']} | Total: ${v['total']}")



def top_3_product():
    """Show the 3 best-selling products."""
    print("3 productos mas vendidos")

    count = {}

    for sale in sales:
        count[sale["producto"]] = count.get(sale["producto"], 0) + sale["cantidad"]

    ranking = sorted(count.items(), key=lambda x: x[1], reverse=True)

    print(ranking[:3])


def sale_for_author():
    """Groups sales by author."""
    print("ventas por autor")

    totals = {}

    for venta in sales:
        autor = next(p["autor"] for p in booksL if p["nombre"] == venta["producto"])
        totals[autor] = totals.get(autor, 0) + venta["total"]

    for autor, total in totals.items():
        print(f"{autor}: ${total}")


def report_income():
    """Shows gross and net income."""
    print("Reporte de ingreso")

    bruto = sum(v["total"] for v in sales)
    neto = bruto * 0.90  

    print(f"Ingreso bruto: ${bruto}")
    print(f"Ingreso neto (después del 10%): ${neto}")


            
while True:
    print("\nMenu principal")
    print("1. Agregar libros: ")
    print("2. Mostrar ver libros: ")
    print("3. Actualizar libros: ")
    print("4. eliminar libros")
    print("5. registrar libros")
    print("6. top mas vendidos")
    print("7. reporte de ingresos")    
    print("8. reporte de ingresos por autor") 
    

    opcion = int(input("digita una opcion de 1 a 6: "))
    if opcion < 1 or opcion > 10:
        opcion = int(input("digita una opcion  valida de 1 a 6: "))
        continue
    if opcion == 1:
        add_product()
    elif opcion == 2:
        see_inventory()
    elif opcion == 3:
        update_product()
    elif opcion == 4:
        delete_product()
    elif opcion == 5:
        register_product()
    elif opcion == 6:
        top_3_product()
    elif opcion == 7:
        report_income()
    elif opcion == 8:
        sale_for_author()

    else:
        print("saliste del menu")
        break