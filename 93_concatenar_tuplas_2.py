print(" CONSOLIDACIÓN DE LOGÍSTICA - PLANTA SAN JOAQUÍN ".center(65, "="))
despacho_mañana = ("Harina-PAN", "Aceite-Mazeite")
despacho_tarde = ("Arroz-Primor", "Margarina-Mavesa")
devoluciones_lista = ["Vinagre-Olula", "Sal-Marina"]
print(f"Tupla despacho mañana: {despacho_mañana}")
print(f"Tupla despacho tarde: {despacho_tarde}")
print(f"lista devolucion: {devoluciones_lista}")
consolidado_tupla = despacho_mañana + despacho_tarde
print(f"Tupla consolidado: {consolidado_tupla}")
print()
consolidado_tupla += tuple(devoluciones_lista)
print(f"Tupla consolidado: {consolidado_tupla}")
print()
for producto in consolidado_tupla:
    print(f"Producto listo en anden: {producto}")
print()
codigo_seguridad = (len(consolidado_tupla[0]) * len(consolidado_tupla)) + 250
print(f"Total ítems en inventario: {len(consolidado_tupla)}")
print(f"Código Control de Cierre:  {codigo_seguridad}")

