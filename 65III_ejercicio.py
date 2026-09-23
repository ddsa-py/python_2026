import copy
print(" AUDITORÍA DE LLENADO DINÁMICO - ALIMENTOS POLAR ".center(60, "#"))

matrix = []

fila_num = int(input("Ingresa el numero de filas: "))
columna_num = int(input("Ingresa el numero de columnas: "))

for i in range(fila_num):
    fila = []
    for j in range(columna_num):
        fila.append(int(input("Ingresa el valor de la temperatura: ")))
    if 100 not in fila[:]:
        matrix.append(fila)
matrix_apertura = copy.deepcopy(matrix)
resultado_auditoria = (len(matrix) * len(matrix[0])) - 50

print(f"1. Matrix Apertura RAM:    {matrix_apertura}")
print(f"2. Resultado Auditoría:    {resultado_auditoria}")

rejilla_final = f"{matrix}"
print(f"3. Matriz Viva Final RAM:\n{rejilla_final}")



# Simulamos que el operario de la planta define estas dimensiones:
num_fila = 3
num_columna = 2
matrix = [0.1]
contador_rechazos = 2

for i in range(num_fila):
    fila = [2,3]
    for j in range(num_columna):
        # Inyección basada en la suma de los índices de control
        valor = i + j
        fila.append(valor)
        
    # 🚨 EVALÚA LA SANGRÍA DE LA COMPUERTA LÓGICA (Nivel 1 de control)
    if 2 in fila:
        contador_rechazos += 1
        continue
        
    matrix.append(fila)

resultado_final = (len(matrix) * contador_rechazos) + 1














