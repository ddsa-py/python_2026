import copy
print(" AUDITORÍA MATRICIAL DINÁMICA AVANZADA - POLAR ".center(60, "#"))

matrix = []

for fila_ in range(3):
    fila = []
    for columna in range(3):
        fila.append(100)
    if len(matrix) != 1:
        matrix.append(fila)
matrix_apertura = copy.deepcopy(matrix)
resultado_auditoria = (len(matrix) * len(matrix[0])) // len(fila)

print(f"1. Matrix Apertura RAM:    {matrix_apertura}")
print(f"2. Resultado Auditoría:    {resultado_auditoria}")

rejilla_final = f"{matrix[0]}"
print(f"3. Matriz Viva Final RAM:\n{rejilla_final}")



            
