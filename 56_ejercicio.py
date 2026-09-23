print(" AUDITORÍA EN CALIENTE ALIMENTOS POLAR - RETO EXTEND ".center(60, "#"))
print()


lotes_maiz = [100, 200]
estatus_muelle = ["Procesado", "Procesado", "Critico", "Procesado"]
maiz_apertura = lotes_maiz[:]
lotes_maiz.extend(range(300,550,50))
posicion_falla = estatus_muelle.index("Critico")
resultado = len(lotes_maiz) + len(estatus_muelle[posicion_falla])
lotes_maiz[posicion_falla] *= resultado

print(f"1. Maíz Apertura:          {maiz_apertura}")
print(f"2. Índice de Falla Buscado: {posicion_falla}")
print(f"3. Lista Maíz Final RAM:   {lotes_maiz}")
print(f"4. Lista Muelle Final:     {estatus_muelle}")
