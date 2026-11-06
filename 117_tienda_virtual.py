#Línea  reservada
valores_metal = {"hierro": 5, "cobre": 12 , "aluminio": 8}
tonelaje = {}
conteo_descargar = {}
total = 0
total_final_pagar = 0
simbolo = "$"
tonelaje_neto = 0
texto = ""
producto = ""
cantidad_metal = 0
conteo_descargar_list = []
valores_metal_list = []

while True:
    print("Productos Disponibles")
    print()
    [print(f"• {producto} ${precio}") for producto, precio in valores_metal.items()]
    print()
    producto = input("Ingrese el nombre del metal: ").strip().lower()
    if producto == "salir":
        
        print("\nGracias")
        print()
        break
    
    if producto not in valores_metal:
        print("Producto no valido, por favor, seleccione un producto del menu")
        print()
        continue
    cantidad_metal = input("Ingrese la cantidad a ingresar: ").strip()
    try:
        cantidad_metal = int(cantidad_metal)
        print()
        if cantidad_metal <=0:
            print("Error, solo se admiten valores numericos positivos")
            continue
    except Exception:
        print("Error, Solo se admiten valores numericos positivos")
        continue
    texto = "tonelada" if cantidad_metal == 1 else "toneladas"
    total = cantidad_metal * valores_metal[producto]
    total_final_pagar += total
    tonelaje_neto += cantidad_metal
    tonelaje[producto] = tonelaje.get(producto, 0) + cantidad_metal
    conteo_descargar[producto] = conteo_descargar.get(producto,0) + 1
    
    print(f"Se ha agregado {cantidad_metal} {texto} de {producto}\n")
    valores_metal_list = list(tonelaje.items())
    conteo_descargar_list = list(conteo_descargar.items())
    

if not conteo_descargar:
    print("Auditoría de Planta: No se registraron movimientos en este turno.")
    print()
else:
    print(f"Cantidad de tipos de metal retirado: {conteo_descargar_list}")
    print(f"Metales: {valores_metal_list}")
    print(f"Cantidad total de toneladas {tonelaje_neto}")
    print(f"Total a pagar {simbolo}{total_final_pagar}")