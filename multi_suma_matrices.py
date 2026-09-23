import copy
print(" AUDITORÍA COMBINADA DE MATRICES - POLAR ".center(60, "#"))

archivador_polar = []
matrix_suma = []
matrix_multi = []
matrix_resta = []

cantidad_matrices = int(input("Ingrese por favor la cantidad de matrices que desea: "))

if cantidad_matrices > 1:
    filas = int(input("Ingrese la cantidad de filas para las matrices: "))
    columnas = int(input("Ingrese la cantidad de columnas para las matrices: "))

    for m in range(cantidad_matrices):
        matrix = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                variable = int(input(f"Ingrese el valor matriz {m + 1} celda[{i}][{j}]: "))
                fila.append(variable)
            matrix.append(fila)
        archivador_polar.append(matrix)
    #print(archivador_polar)
    for posicion in range(len(archivador_polar)):
        print(f"Matriz {posicion + 1}")
        for fila_archivador in archivador_polar[posicion]:
            print(fila_archivador)
#suma
    for i_ in range(filas):
        fila_suma = []
        for j_ in range(columnas):
            acumulador_suma = 0    
            for m_ in range(len(archivador_polar)):
                acumulador_suma += archivador_polar[m_][i_][j_]
            fila_suma.append(acumulador_suma)          
        matrix_suma.append(fila_suma)
    #multiplicacion
    for i_m in range(filas):
        fila_multi = []
        for j_m in range(columnas):
            acumulador_multi = 0
            for k in range(cantidad_matrices):
                acumulador_multi += archivador_polar[0][i_m][k] * archivador_polar[1][k][j_m]
            fila_multi.append(acumulador_multi)
        matrix_multi.append(fila_multi)
    #resta
    for i_r in range(filas):
        fila_resta = []
        for j_r in range(columnas):
            acumulador_resta = archivador_polar[0][i_r][j_r]
            for m_r in range(1,len(archivador_polar)):
                acumulador_resta -= archivador_polar[m_r][i_r][j_r]
            fila_resta.append(acumulador_resta)
        matrix_resta.append(fila_resta)

    for _ in range(1):
        print(f"Matriz Resta")
        for fila_archivador in matrix_resta:
            print(fila_archivador)
        

    for posicion_ in range(1):
        print(f"Matriz suma")
        for fila_archivador in matrix_suma:
            print(fila_archivador)
    for posicion_m in range(1):
        print(f"Matriz multiplicacion")
        for fila_archivador_ in matrix_multi:
            print(fila_archivador_)
        
    
        
    resultado_auditoria = (len(matrix_suma) + len(matrix_multi)) * 350
    print()        
    print(f"1. Renglón Control Final: {resultado_auditoria}")
    print(f"2. Matriz Sumada:\n{matrix_suma}")
    print(f"3. Matriz Multiplicada:\n{matrix_multi}")            
else:
    print("Error, las matrices deben ser mayor a 2")



















    
