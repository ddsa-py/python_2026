import copy
print(" AUDITORÍA MATRICIAL MULTIVARIABLE - POLAR ".center(60, "#"))

matrix_x = [[2, 4], [6, 8], [10, 12]]
matrix_y = [[1, 3], [5, 7], [9, 11]]
matrix_z = []

registro_alerta = 100
lotes_procesados = 0
contador_fallos = 0
multiplicador_seguridad = 5

for i in range(3):
    fila_calculada = []
    for j in range(2):
        fila_calculada.append(matrix_x[i][j]  + matrix_y[i][j])
    lotes_procesados += 1
    if len(matrix_z) != 1:
        matrix_z.append(fila_calculada)

    else:
        contador_fallos += 1
        registro_alerta -= 20
        continue
matrix_apertura = copy.deepcopy(matrix_z)
resultado_auditoria =   (((len(matrix_z) + lotes_procesados) * registro_alerta) - (contador_fallos * multiplicador_seguridad))  + len(fila_calculada)

print(f"1. Matrix Apertura RAM:    {matrix_apertura}")
print(f"2. Resultado Auditoría:    {resultado_auditoria}")
rejilla_final = f"{matrix_z}"
print(f"3. Matriz Viva Final RAM:\n{rejilla_final}")



























        
        
