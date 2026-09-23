import copy
print(" AUDITORÍA MATRICIAL DINÁMICA - ALIMENTOS POLAR ".center(60, "#"))
matrix = []

for fila in range(3):
    fila = []
    for columna in range(2):
        fila.append(50)
    if len(matrix) <= 1:
        matrix.append(fila)
matrix_apertura = copy.deepcopy(matrix)

resultado_auditoria = (len(matrix) * len(fila)) + 100


print(f"1. Matrix Apertura RAM:    {matrix_apertura}")
print(f"2. Resultado Auditoría:    {resultado_auditoria}")

rejilla_final = f"{matrix[0]}\n{matrix[1]}    "
print(f"3. Matriz Viva Final RAM:\n{rejilla_final}")

        

