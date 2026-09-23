print("Cervecería Polar (Planta San Joaquín, Carabobo)".center(60,"*"))
print()
galones_aditivos = [450, 120, 310, 120, 890]
lotes_seguridad = ["L-3", "L-1", "L-4", "L-2"]

aditivos_apertura = galones_aditivos[:]
lotes_seguridad.sort()
indice_galon = galones_aditivos.index(120,2)
variable = len(lotes_seguridad[2])

indice_lote = lotes_seguridad.index("L-3",1,4)
galones_aditivos[indice_galon] +=  variable * len(lotes_seguridad)


print(f"1. Aditivos Apertura:     {aditivos_apertura}")
print(f"2. Índice Galón Buscado:  {indice_galon}")
print(f"3. Índice Lote Buscado:   {indice_lote}")
print(f"4. Lista Aditivos Final:  {galones_aditivos}")
print(f"5. Lista Lotes Final RAM: {lotes_seguridad}")

