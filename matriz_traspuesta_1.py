matrix_original = [[10, 20, 30, 40],
                   [50, 60, 70, 80],
                   [90, 100, 110, 120]
                   ]

matrix_t = []

for _ in range(1):
    print("Matriz original")
    for i in range(len(matrix_original)):
        print(matrix_original[i])

print()

for j in range(4):
    fila_nueva = []
    for h in range(len(matrix_original)):
        #numero = matrix_original[h][j]
        fila_nueva.append(matrix_original[h][j])
    matrix_t.append(fila_nueva)

for _ in range(1):
    print("Matriz traspuesta")
    for k in range(len(matrix_t)):
        print(matrix_t[k])
resultado_auditoria =  (len(matrix_t) * matrix_original[0][0]) + 400
print()
print(f"Resultado Auditoria: {resultado_auditoria}")
