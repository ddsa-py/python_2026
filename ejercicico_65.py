import copy
matrix = []
fila_num = 2
columna_num = 2

for i in range(fila_num):
    fila = []
    for j in range(columna_num):
        fila.append(int(input(f"Ingresa el valor de la unidad #{i}: ")))
        
    if len(matrix) == 0:
        matrix.append(fila)
ma= copy.deepcopy(matrix)

resultado_auditoria = (len(matrix) + len(matrix[0])) * 100

print(" AUDITORÍA DE LLENADO DINÁMICO #13 - ALIMENTOS POLAR ".center(60, "#"))
print(f"1. Resultado Auditoría:    {resultado_auditoria}")
rejilla_final = f"{matrix}"
print(f"2. Matriz Viva Final RAM:\n{rejilla_final}")
print()
print(ma)        
