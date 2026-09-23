import copy
print(" AUDITORÍA MATRICIAL DINÁMICA DE RECHAZOS - POLAR ".center(60, "#"))

matrix = []
lotes_rechazados = 0
for i in range(3):
    fila = []
    for j in range(2):
        fila.append(55)
    if len(matrix) <= 0:
        matrix.append(fila)
    else:
        lotes_rechazados += 1
        continue
matrix_apertura = copy.deepcopy(matrix)
resultado_auditoria = ((len(matrix) + len(fila)) * lotes_rechazados) + 500


print(f"1. Matrix Apertura RAM:    {matrix_apertura}")
print(f"2. Resultado Auditoría:    {resultado_auditoria}")
rejilla_final = f"{matrix}"
print(f"3. Matriz Viva Final RAM:\n{rejilla_final}")
import copy
matrix_c = []

matrix_a = [[2,4,6],
            [8,10,6],
            [7,8,9]]

matrix_b = [[9,8,7],
            [6,5,10],
            [10,10,10]]

for i in range(3):
    fila_a = []
    for j in range(3):
        fila_a.append(matrix_a[i][j] // matrix_b[i][j])
    matrix_c.append(fila_a)

rejilla = copy.deepcopy(matrix_c)
rejilla = f"{matrix_c[0]}\n{matrix_c[1]}\n{matrix_c[2]}"

for i in range(len(matrix_a)):
    if i != 1:
        print(f"{matrix_a[i]}   {matrix_b[i]}    {matrix_c[i]}")
    else:
        print(f"{matrix_a[i]} - {matrix_b[i]} =  {matrix_c[i]}")
    
print()
print(rejilla)
