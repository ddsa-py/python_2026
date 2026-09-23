print("*El Calculador Automatizado de Descuentos de un Almacén*")
print("")
while True:
    prenda = input("Ingrese el nombre de la prenda de vestir: ").strip().title()
    if prenda == "Apagar":
        print("Cerrando la consola de cobro...")
        break
    while True:
        precio = input("Ingrese el precio original de la prenda de vestir: ")
        if not precio.isdigit():
            print("¡Error!: El precio debe ser un número entero.")
            continue
        precio = int(precio)
        if precio <= 10:
            print("La prenda debe ser mayor a 10$")
            continue
        break
    print(f"La ropa {prenda} tiene un costo de {precio}$, tiene un descuento de 10$, total a pagar: {precio - 10}$")
    break
