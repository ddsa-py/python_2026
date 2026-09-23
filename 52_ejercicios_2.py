print("El Depurador Automatizado de Lotes Defectuosos")
print()
lotes_pepsi = ["Lote_1", "Lote_2", "Lote_3", "Lote_4", "Lote_5", "Lote_6", "Lote_7", "Lote_8"]
inventario_apertura = lotes_pepsi[:]
mitad_fila = len(lotes_pepsi) // 2
del lotes_pepsi[mitad_fila]
inventario_almuerzo = lotes_pepsi[:]
del lotes_pepsi[-4:]

print(f"1. Índice de la Mitad Calculado: {mitad_fila}")
print(f"2. Inventario de Apertura:       {inventario_apertura}")
print(f"3. Inventario al Almuerzo:       {inventario_almuerzo}")
print(f"4. Inventario Final Vivo RAM:    {lotes_pepsi}")
