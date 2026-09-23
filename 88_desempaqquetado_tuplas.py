print(" AUDITORÍA DE DESEMPAQUETADO SIMÉTRICO - POLAR ".center(60, "#"))
lote_polar = ("silo-alfa", 500, 320, 480, "aprobado")


peso_1, peso_2, peso_3 = lote_polar[1:4]
print(peso_1, peso_2, peso_3)

balance_desempaquetado = ((peso_1 * len(lote_polar)) + peso_2) - peso_3


print(f"1. Renglón Control Final: {balance_desempaquetado}")
print(f"2. Pesos Desempaquetados: {peso_1}, {peso_2}, {peso_3}")
print(f"3. Tipo de Datos Libres:  {type(peso_1)}, {type(peso_2)}, {type(peso_3)}")

