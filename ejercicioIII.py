import copy
print(" AUDITORÍA DE SUMA MATRICIAL #14 - ALIMENTOS POLAR ".center(60, "#"))

matrix_linea_1 = [[10, 20], [30, 40], [50, 60]]
matrix_linea_2 = [[5, 5], [10, 10], [15, 15]]
matrix_total = []
lotes_rebotados = 10

for i in range(3):
    fila_suma = []
    for j in range(2):
        fila_suma.append(matrix_linea_1[i][j] + matrix_linea_2[i][j])
    if len(matrix_total) <= 1:
        matrix_total.append(fila_suma)
    else:
        lotes_rebotados += 5
        continue
matrix_apertura = copy.deepcopy(matrix_total)

resultado_auditoria = (len(matrix_total) * lotes_rebotados) + len(fila_suma)

print(f"1. Matrix Apertura RAM:    {matrix_apertura}")
print(f"2. Resultado Auditoría:    {resultado_auditoria}")
rejilla_final = f"{matrix_total}"
print(f"3. Matriz Total Final RAM:\n{rejilla_final}")

        
