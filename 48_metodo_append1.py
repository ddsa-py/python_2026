print("El Historial de Chasis en la Línea de Ensamblaje".center(60,"*"))
print()
linea_produccion = ["Chasis_1", "Chasis_2", "Chasis_3", "Chasis_4", "Chasis_5"]
reporte_mañana = linea_produccion[:]
lote_pintura = linea_produccion[1:4]
linea_produccion.append("Mustang-2026")
reporte_tarde = linea_produccion[:]
linea_produccion.append(480.5)
print(f"Reporte Mañana Blindado: {reporte_mañana}")
print(f"Lote Central Pintura:     {lote_pintura}")
print(f"Reporte Tarde Blindado:  {reporte_tarde}")
print(f"Línea de Producción Viva: {linea_produccion}")




numeros = [10, 20, 30]

numeros[-1] = 99
numeros.append(100)
print(f"Lista Final en la RAM: {numeros}")
numeros[2:3] = [101,102,103]
print(f"Lista Final en la RAM: {numeros}")
numeros[:] = [1]
print(f"Lista Final en la RAM: {numeros}")
numeros[:] = []
print(f"Lista Final en la RAM: {numeros}")
#da error por qu?
numeros[:] = "1"
print(f"Lista Final en la RAM: {numeros}")

numeros[:] = "todos por igual"
print(f"Lista Final en la RAM: {numeros}")
























