print("Planta de Distribución de Pepsi en la Zona Industrial de Valencia".center(60,"#"))
print()
lotes_pepsi = ["Lote_A", "Lote_B", "Lote_C", "Lote_D", "Lote_E", "Lote_F"]
reporte_apertura = lotes_pepsi[:]
del lotes_pepsi[1]
reporte_almuerzo = lotes_pepsi[:]

del lotes_pepsi[2:]

print(f"1. Inventario Apertura: {reporte_apertura}")
print(f"2. Inventario Almuerzo: {reporte_almuerzo}")
print(f"3. Inventario Final RAM: {lotes_pepsi}")

print()
print("El Depurador Dinámico de Flota".center(60,"*"))
print()

flota_polar = ["Gandola_1", "Camion_2", "Gandola_3", "Camion_4", "Gandola_5", "Camion_6", "Gandola_7"]
reporte_apertura = flota_polar[:]
indice_mitad = len(flota_polar) // 2
del flota_polar[indice_mitad]
reporte_mediodia = flota_polar[:]
del flota_polar[-3:]

print(f"1. Índice de la Mitad Calculado: {indice_mitad}")
print(f"2. Reporte de Apertura Flota:    {reporte_apertura}")
print(f"3. Reporte de Mediodía Flota:   {reporte_mediodia}")
print(f"4. Estado Final de la Flota RAM: {flota_polar}")

