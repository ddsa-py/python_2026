import copy
print(" AUDITORÍA MATRICIAL DE ENGRANAJES - POLAR ".center(60, "#"))

matrix = []

for _ in range(3):
    fila=[]
    for _ in range(2):
        fila.append(77)
    if len(matrix) % 2 ==0:
        matrix.append(fila)
matrix_apertura = copy.deepcopy(matrix)

resultado_auditoria  = (len(matrix) + len(matrix[0])) * 100

print(f"1. Matrix Apertura RAM:    {matrix_apertura}")
print(f"2. Resultado Auditoría:    {resultado_auditoria}")
rejilla_final = f"{matrix[0]}"
print(f"3. Matriz Viva Final RAM:\n{rejilla_final}")
print(fila)
import copy
print(" AUDITORÍA MATRICIAL DINÁMICA INDEPENDIENTE - POLAR ".center(60, "#"))
matrix = []

for _ in range(3):
    fila=[]
    for columna in range(2):
        fila.append(88)
    if len(matrix) == 0 or len(matrix) == 2:
        matrix.append(fila)
matrix_apertura = copy.deepcopy(matrix)
resultado_auditoria = ((len(matrix) + len(matrix[0])) * len(fila)) + 500



print(f"1. Matrix Apertura RAM:    {matrix_apertura}")
print(f"2. Resultado Auditoría:    {resultado_auditoria}")
rejilla_final = f"{matrix}"
print(f"3. Matriz Viva Final RAM:\n{rejilla_final}")


        







































    
