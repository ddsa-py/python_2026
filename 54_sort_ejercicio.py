print("Cervecería Polar (Planta San Joaquín, Carabobo)".center(60,"*"))
print()
lotes = [105, 302, 98, 410]
codigos = ["C", "A", "D", "B"]
lotes_apertura =  lotes[:]
lotes.sort(reverse=True)
lotes_medio= lotes[:]
codigos.sort()
lotes[-1] = lotes[0] * len(codigos)
codigo_despachado = codigos.pop(2)
print(f"1. Lotes Apertura: {lotes_apertura}")
print(f"2. Lotes medio: {lotes_medio}")
print(f"3. Codigo Sacado:  {codigo_despachado}")
print(f"4. Lista Lotes:    {lotes}")
print(f"5. Lista Codigos:  {codigos}")
print()
print(" AUDITORÍA EN CALIENTE ALIMENTOS POLAR ".center(60, "#"))
print()
print("El Sincronizador de Calidad y Despacho".center(60, "#"))
print()
pesos_lotes = [520, 110, 840, 310]
zonas_carga = ["Valencia", "Maracay", "Caracas", "Barquisimeto"]
pesos_apertura = pesos_lotes[:]
pesos_lotes.sort()
pesos_medio = pesos_lotes[:]
zonas_carga.sort(reverse=True)
pesos_medio_carga = zonas_carga[:]

resultado = pesos_lotes[-1] + len(zonas_carga)
pesos_lotes[0] = resultado
zona_despachada = zonas_carga.pop(1)

print(f"1. Pesos Apertura:        {pesos_apertura}")
print(f"2. Pesos medio a - z:        {pesos_medio}")
print(f"3. Pesos carga z - a:        {pesos_medio_carga}")
print(f"4. Zona Despachada Pura:  {zona_despachada}")
print(f"5. Lista Pesos Final RAM: {pesos_lotes}")
print(f"6. Lista Zonas Final RAM: {zonas_carga}")


