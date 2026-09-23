print(" AUDITORÍA DE ULTRA PROFUNDIDAD - ALIMENTOS POLAR ".center(60, "#"))
reporte_infraestructura = [250, "Zona-A", [10, 20, [500, ["T-Falla", "T-Optima"]]]]

reporte_apertura = reporte_infraestructura[:]

estatus_critico = reporte_infraestructura[2][2][1][1]

reporte_infraestructura[0] //= (len(estatus_critico) - len(reporte_infraestructura[2][2][1]))


print(f"1. Reporte Apertura: {reporte_apertura}")
print(f"2. Estatus Extraído: {estatus_critico}")
print(f"3. Lista Reporte Final RAM: {reporte_infraestructura}")
