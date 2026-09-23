print("Alimentos Polar en la Zona Industrial de Valencia".center(60,"#"))
print()
lotes_harina = [800, 1500, 600, 1200]
inventario_manana = lotes_harina[:]
lotes_harina[1]*=3
bultos_despachados = lotes_harina.pop()
inventario_tarde = lotes_harina[:]
lote_retenido = lotes_harina.pop(1)

print(f"1. Inventario Mañana:     {inventario_manana}")
print(f"2. Inventario Tarde:      {inventario_tarde}")
print(f"3. Bultos Despachados:    {bultos_despachados}")

print(f"4. Lote en Retención:     {lote_retenido}")
print(f"5. Stock Vivo Actual RAM: {lotes_harina}")
