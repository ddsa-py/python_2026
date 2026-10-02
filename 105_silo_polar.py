print(" REPORTE ANALÍTICO DE SILOS - ALIMENTOS POLAR ".center(65, "="))
silo_esperado = {"Maíz", "Soya", "Trigo", "Arroz"}
silo_real= {"Trigo", "Arroz", "Cebada", "Malta"}
print(f"Silo esperado: {silo_esperado}")
print(f"Silo real: {silo_real}")
insumos_coincidentes = silo_esperado & silo_real
print(f"Insumos coincidentes: {insumos_coincidentes}")
insumos_exclusivos = silo_esperado ^ (silo_real)
print(f"Insumos exclusivos: {insumos_exclusivos}")
balance_final = (len(insumos_coincidentes) * len(insumos_exclusivos)) + 300
print(f"Balance final: {balance_final}")
