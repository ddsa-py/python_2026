print(" AUDITORÍA DE EXTREMOS ALIMENTOS POLAR ".center(60, "#"))
print()
pesos_silos = [450, 120, 890, 310, 600]

silos_apertura = pesos_silos[:]
peso_maximo = max(pesos_silos)
peso_minimo  = min(pesos_silos)
pesos_silos[-1] *= (peso_maximo - peso_minimo)

print(f"1. Silos Apertura:        {silos_apertura}")
print(f"2. Peso Máximo Detectado: {peso_maximo}")
print(f"3. Peso Mínimo Detectado: {peso_minimo}")
print(f"4. Lista Silos Final RAM: {pesos_silos}")

print("Metodo count")
print(" AUDITORÍA DE CONTEO CERVECERÍA POLAR ".center(60, "#"))
print()
lotes_defectuosos = ["L-1", "L-2", "L-1", "L-3", "L-1", "L-2"]

defectuosos_apertura = lotes_defectuosos[:]
total_l1 = lotes_defectuosos.count("L-1")
resultado = len(lotes_defectuosos[0]) * total_l1
mutacion_final = len(lotes_defectuosos[-1]) + resultado



print(f"1. Defectuosos Apertura: {defectuosos_apertura}")
print(f"2. Total Repeticiones L1: {total_l1}")
print(f"3. Resultado Numérico:    {mutacion_final}")
