matrix_original = [[10, 20, 30, 40],
                   [50, 60, 70, 80],
                   [90, 100, 110, 120]
                   ]
matrix_t = []
for _ in range(1):
    print("Matriz original")
    for j in range(len(matrix_original)):
        print(f"{matrix_original[j]}")

for i in range(4):
    fila_nueva = []
    for h in range(len(matrix_original)):
        fila_nueva.append(matrix_original[h][i])
    matrix_t.append(fila_nueva)
print()

for _ in range(1):
    print("Matriz traspuesta")
    for i in range(len(matrix_t)):
        print(matrix_t[i])


        
