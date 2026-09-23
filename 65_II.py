import copy
print(" AUDITORÍA MATRICIAL DINÁMICA DE ALTOS FLUJOS - POLAR ".center(60, "#"))

matrix = []


for i in range(3):
    fila=[]
    for e in range(3):
        fila.append(99)
    if len(matrix) != 1:
        matrix.append(fila)
matrix_apertura = copy.deepcopy(matrix)

resultado_auditoria = 1000
resultado_auditoria -=  (len(matrix) * len(fila))

print(f"1. Matrix Apertura RAM:    {matrix_apertura}")
print(f"2. Resultado Auditoría:    {resultado_auditoria}")
rejilla_final = f"{matrix}"
print(f"3. Matriz Viva Final RAM:\n{rejilla_final}")





