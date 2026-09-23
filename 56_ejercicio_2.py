print(" AUDITORÍA MATEMÁTICA ALIMENTOS POLAR - RETO SUM ".center(60, "#"))
print("El Consolidador Matemático de Silos")
print()

carga_maiz = [150, 200, 350] 
alertas_silo = [True, False, True, True]

maiz_apertura = carga_maiz[:]
carga_desplazada = sum(carga_maiz, -50)
total_criticos = sum(alertas_silo)
variable = total_criticos + len(carga_maiz)
carga_maiz[0] *= variable


print(f"1. Maíz Apertura:          {maiz_apertura}")
print(f"2. Carga con Base -50:     {carga_desplazada}")
print(f"3. Total Silos Críticos:   {total_criticos}")
print(f"4. Lista Maíz Final RAM:   {carga_maiz}")
