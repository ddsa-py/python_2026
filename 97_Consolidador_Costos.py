print(" AUDITORÍA FINANCIERA DE PRODUCCIÓN - POLAR ".center(65, "="))
costos_materia_prima = (120, 340, 250, 500, 180)
costos_operativos = (80, 160, 150, 300, 120)
totales_acumulados = []

for mp, op in zip(costos_materia_prima, costos_operativos):
    totales_acumulados.append(mp + op)
indicador_auditoria = ((totales_acumulados[0] + totales_acumulados[-1]) * len(totales_acumulados)) - 100


print(f"{costos_materia_prima}".rjust(25, " "))
print(f"{costos_operativos}".rjust(25, " "))
print(f"{tuple(totales_acumulados)}".rjust(25, " "))
print(f"Código Verificación de Cierre: {indicador_auditoria}")
