import copy
print(" AUDITORÍA DE MULTIPLICACIÓN MATRICIAL ASIMÉTRICA - POLAR ".center(60, "#"))


# Matriz A de 3 filas por 2 columnas (3x2)
matrix_a = [[1, 2],
            [3, 4],
            [5, 6]]

# Matriz B de 2 filas por 3 columnas (2x3)
matrix_b = [[5, 6, 7],
            [8, 9, 10]]

matrix_res = []

for i in range(3):
    fila_calculada = []
    for j in  range(3):
        suma_producto = 0
        for k in range(2):
            suma_producto += matrix_a[i][k] * matrix_b[k][j]
        fila_calculada.append(suma_producto)
    matrix_res.append(fila_calculada)

matrix_apertura = copy.deepcopy(matrix_res)
resultado_auditoria = (len(matrix_res) + len(fila_calculada)) * 100
print(f"1. Matrix Apertura RAM:    {matrix_apertura}")
print(f"2. Resultado Auditoría:    {resultado_auditoria}")
rejilla_final = f"{matrix_res}"
print(f"3. Matriz Res Final RAM:\n{rejilla_final}")



