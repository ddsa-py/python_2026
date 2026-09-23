print(" AUDITORÍA PURIFICADA ALIMENTOS POLAR ".center(60, "#"))
print("Alimentos Polar (Planta San Joaquín, Carabobo)")
print()

lotes_harina = [200, 500, 800, 500, 150]
estatus_lotes = ["Aprobado", "Aprobado", "Alerta", "Rechazado"]
harina_apertura = lotes_harina[:]
posicion_harina= lotes_harina.index(500,2)
posicion_estatus = estatus_lotes.index("Alerta",1,4)

resultado = len(estatus_lotes[posicion_estatus]) * len(lotes_harina)
lotes_harina[posicion_harina] += resultado

print(f"1. Harina Apertura:       {harina_apertura}")
print(f"2. Índice posicion harina: {posicion_harina}")
print(f"3. Índice Estatus Buscado:{posicion_estatus}")
print(f"4. Lista Harina Final RAM: {lotes_harina}")




