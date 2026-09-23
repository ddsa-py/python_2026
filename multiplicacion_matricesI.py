matrix_a = [[1, 2],
            [3, 4]]

matrix_b = [[5, 6],
            [7, 8]]
matrix_res = []

for i in range(2):
    fila = []
    for j in range(2):
        acumulador = 0
        for k in range(2):
            acumulador += matrix_a[i][k] * matrix_b[k][j]
        fila.append(acumulador)
    matrix_res.append(fila)
resultado_final = len(matrix_res) * 150

print(" AUDITORÍA DE MULTIPLICACIÓN EN CALIENTE - POLAR ".center(60, "#"))
print(f"1. Renglón de Auditoría: {resultado_final}")
print(f"2. Matriz Multiplicada:\n{matrix_res}")

    
            
