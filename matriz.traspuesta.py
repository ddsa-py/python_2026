matrix_a = [[10, 20, 30],
            [40, 50, 60]
            ]
matrix_t = []
for _ in range(1):
    print("Matriz original")
    for g in range(len(matrix_a)):
        print(f"{matrix_a[g]}")

for j in range(3):
    nueva_fila = []
    for i in range(len(matrix_a)):
        numero = matrix_a[i][j]
        nueva_fila.append(numero)
    matrix_t.append(nueva_fila)

print()
for _ in range(1):
    print("Matriz Traspuesta")
    for j in range(len(matrix_t)):
        print(f"{matrix_t[j]}")
print()
resultado = len(matrix_t) * 500
print(f"Resultado control: {resultado}")


