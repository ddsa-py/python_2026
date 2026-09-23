import copy
print(" AUDITORÍA INTEGRAL DE SEGURIDAD - POLAR ".center(60, "#"))

# Tu punto de partida indestructible en la RAM:
archivador_polar = []
matrix_consolidada = []
lotes_bloqueados_pantalla = 0

cantidad_matrices = int(input("Ingrese la cantidad de matrices: "))

if cantidad_matrices > 1:
    
    filas = int(input("Ingrese la cantidad de filas para la matriz: "))
    columnas = int(input("Ingrese la cantidad de columnas para la matriz: "))
    for m in range(cantidad_matrices):
        matrix = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                variable = int(input(f"Ingrese en la matriz {m+1} celda[{i}][{j}]: "))
                fila.append(variable)
            matrix.append(fila)
        archivador_polar.append(matrix)
    
    for posicion in range(len(archivador_polar)):
        if archivador_polar[posicion][0][0] > 100:
            lotes_bloqueados_pantalla += 1
            continue
        print(f"Matriz {posicion + 1}")
        for fila_ in archivador_polar[posicion]:
            print(fila_)

    for i_ in range(filas):
        fila_suma = []
        for j_ in range(columnas):
            acumulador = 0
            for m_ in range(len(archivador_polar)):
                acumulador += archivador_polar[m_][i_][j_]
            fila_suma.append(acumulador)
        matrix_consolidada.append(fila_suma)
   
    resultado_auditoria = (len(matrix_consolidada) + lotes_bloqueados_pantalla) * 200

    print(f"1. Renglón Control Final: {resultado_auditoria}")
    print(f"2. Matrices Ocultas:     {lotes_bloqueados_pantalla}")
    print(f"3. Matriz Consolidada:\n{matrix_consolidada}")
else:
    print("Error, debe ser mayor a dos matrices")





