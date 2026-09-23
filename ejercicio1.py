import copy
print(" AUDITORÍA DE LOTES REEMPLAZADOS - POLAR ".center(60, "#"))
print(" REPORTE DE REJILLAS DE PRODUCCIÓN ".center(60, "#"))

cantidad_matrices = int(input("Cuantas matrices quiere crear: "))
matrix_lista = []
if cantidad_matrices < 1:
    print("Las matrices deben ser mayor a dos matrices")
else:
    filas = int(input("Ingrese la cantidad de filas que contendra la matriz: "))
    columnas = int(input("Ingrese la cantidad de columnas que contendra la matriz: "))
    for m in range(cantidad_matrices):
        matrix =[]
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor_ingresado = int(input(f"Ingrese en la matriz {m + 1} celda[{i}][{j}]: "))
                if valor_ingresado != 0:
                    fila.append(valor_ingresado)
               
                    
            matrix.append(fila)
        matrix_lista.append(matrix)
    resultado_auditoria = len(matrix_lista) * 300

for posicion in range(len(matrix_lista)):
    if len(matrix_lista[posicion][0]) == 2:
        print(f"--- MATRIZ REAL {posicion + 1} ---")
        for fila in matrix_lista[posicion]:
            print(fila)
    else:
        continue
resultado_control = len(matrix_lista) * 50
        
total_filas_ram = len(matrix_lista) * filas

print(f"Total de Filas Procesadas en RAM: {total_filas_ram}")
print(f"1. Renglón Control Final: {resultado_control}")    
print(f"1. Renglón de Auditoría: {resultado_auditoria}")
print(f"2. Almacén RAM Completo:\n{matrix_lista}")


        

        



