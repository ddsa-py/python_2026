import copy
print(" REPORTE DE CREACIÓN DE ALTA DENSIDAD - POLAR ".center(60, "#"))

# Tu punto de partida indestructible:
matrix_lista = []
cantidad_filtros_aplicados = 0

cantidad_matrices = int(input("Ingrese la cantidad de matrices: "))

if cantidad_matrices > 1:
    filas = int(input("Inmgrese la cantidad de filas para la matriz: "))
    columnas = int(input("Inmgrese la cantidad de columnas para la matriz: "))
    matrix_lista = []
    for m in range(cantidad_matrices):
        matrix = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                num = int(input(f"Ingrese en la matriz {m + 1} celdas[{i}][{j}]: "))
                if num  < 0:
                    cantidad_filtros_aplicados += 1
                    fila.append(0)
                else:
                    fila.append(num)
            matrix.append(fila)

        matrix_lista.append(matrix)


else:
    print("Las matrices deben ser mayor a 2")

resultado_auditoria = (len(matrix_lista) * cantidad_filtros_aplicados) + 400
    
    

for posicion in range(len(matrix_lista)):
    print(f"--- MATRIZ REAL {posicion + 1} ---")
    for fila_ in matrix_lista[posicion]:
        print(fila_)

print(f"1. Renglón de Auditoría: {resultado_auditoria}")
print(f"2. Filtros Activados:    {cantidad_filtros_aplicados}")



            
