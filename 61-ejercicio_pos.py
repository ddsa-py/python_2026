print(" AUDITORÍA MAESTRA DE LOTES - ALIMENTOS POLAR ".center(60, "#"))

lotes_produccion = [100, 200, 300, 200, 400]

produccion_inicial = lotes_produccion[:]

total_defectuosos  = lotes_produccion.count(200)

for _ in lotes_produccion[:]:
    if 200 in lotes_produccion[:]:
      lotes_produccion.remove(200)
lotes_produccion.append(999)
      
resultado_auditoria = sum(lotes_produccion) * total_defectuosos + len(produccion_inicial)

print(f"1. Producción Inicial:     {produccion_inicial}")
print(f"2. Total Lotes Defectuosos: {total_defectuosos}")
print(f"3. Resultado Auditoría:    {resultado_auditoria}")
print(f"4. Lista Final en RAM:     {lotes_produccion}")



numeros = [5,4,8,6,2,3,1,0]
numeros.sort()
print(f"{numeros}")
numeros.sort(reverse=True)

nombre = "daniel"
print(f"{nombre}")
print(f"{list(nombre)}")
nombre=list(nombre)
print(f"{nombre[::-1]}")
