import copy
print(" AUDITORÍA COMPLETA DE FUSIÓN BACKEND - POLAR ".center(60, "#"))

# Tu punto de partida en la memoria volátil:
archivador_polar = []
matrix_consolidada = []


cantidad_matrices = int(input("Ingrese la cantidad de matrices: "))

if cantidad_matrices > 1:
    
    filas = int(input("Ingrese la cantidad de filas para la matriz: "))
    columnas = int(input("Ingrese la cantidad de columnas para la matriz: "))
    for m in range(cantidad_matrices):
        matrix = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(int(input(f"Ingrese en la matriz {m+1} celda[{i}][{j}]: ")))
            matrix.append(fila)
        archivador_polar.append(matrix)
    for posicion in range(len(archivador_polar)):
        print(f"Matriz {posicion + 1}")
        for fila_ in archivador_polar[posicion]:
            print(fila_)
    for i_ in range(filas):
        fila_suma =[]
        for j_ in range(columnas):
            acumulador_celda = 0
            for m_ in range(len(archivador_polar)):
                acumulador_celda += archivador_polar[m_][i_][j_]
            fila_suma.append(acumulador_celda)
        matrix_consolidada.append(fila_suma)
        
else:
    print("Error, debe ser mayor a dos matrices")

resultado_final = len(matrix_consolidada) * 400

print(" AUDITORÍA COMPLETA DE FUSIÓN BACKEND - POLAR ".center(60, "#"))
print(f"1. Renglón Control Final: {resultado_final}")
print(f"2. Matriz Consolidada:\n{matrix_consolidada}")









