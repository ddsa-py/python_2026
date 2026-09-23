import copy
print(" REPORTE DE REJILLAS SELECTIVAS - POLAR ".center(60, "#"))

# Tu punto de partida indestructible en la RAM:
archivador_general = []
lotes_rechazados_pantalla = 0

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
        archivador_general.append(matrix)
    for posicion in range(len(archivador_general)):
        if len(archivador_general[posicion]) <= 2:
            print(f"Matriz {posicion + 1}")
            for fila_ in archivador_general[posicion]:
                print(fila_)
        else:
            lotes_rechazados_pantalla += 1
            continue
else:
    print("Error, debe ser mayor a dos matrices")

resultado_auditoria = (len(archivador_general) + lotes_rechazados_pantalla) * 50


print(f"1. Renglón de Auditoría: {resultado_auditoria}")
print(f"2. Matrices Ocultas:     {lotes_rechazados_pantalla}")
print(f"3. Estructura Cruda RAM:\n{archivador_general}")

