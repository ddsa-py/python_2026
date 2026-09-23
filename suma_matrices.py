import copy

# El archivador central con 3 matrices ya creadas de 2x2
matrix_lista = [
    [[10, 20],
     [30, 40]],  # Matriz 0 (Pantalón 0)
    [[5, 5],
     [10, 10]],    # Matriz 1 (Pantalón 1)
    [[2, 3],
     [1, 4]]

    ]

matrix_suma = []

for i in range(2):
    fila_suma = []
    for j in range(2):
        acumulador_celda = 0
        for m in range(3):
            acumulador_celda += matrix_lista[m][i][j]
        fila_suma.append(acumulador_celda)
    matrix_suma.append(fila_suma)

resultado_auditoria = len(matrix_suma) * 250

print(" REPORTE DE CONSOLIDACIÓN ESTÁTICA - POLAR ".center(60, "#"))
print(f"1. Renglón de Auditoría: {resultado_auditoria}")
print(f"2. Matriz Sumada Final:\n{matrix_suma}")

        
        
