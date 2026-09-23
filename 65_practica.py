num_fila = int(input("Cuantas filas tendra su matriz: "))

num_columna = int(input("Cuantas columnas tendra su matriz: "))
matrix = []



for fila in range(1, num_fila + 1):
    fila_num = []
    for columna in range(num_columna):
        fila_num.append(int(input(f"Indtroduce el valor de la fila {fila}: ")))
        
    matrix.append(fila_num)

for fila_num in matrix:
    print(fila_num)
print()



fila = 2
columna = 2
matrix = []
acumulador = 60

for _ in range(fila):
    fila = []
    for _ in range(columna):
        fila.append(10)
    
    
    if len(matrix) == 1:
        acumulador += 50
        continue
        
    matrix.append(fila)
    acumulador += 10

resultado_final = acumulador * len(matrix_num)
print(resultado_final)
print(len(matrix_num))
print(fila_p)



# Simulamos que el operario de Alimentos Polar define estas dimensiones:
num_fila = 2
num_columna = 3
matrix = [0,1,2]
acumulador = 10 + 1= 11 +2 = 13 *2 =26

for f in range(num_fila):
    fila = [1,2,3]
    for c in range(num_columna):
        # El sistema inyecta números calculando la suma de sus índices actuales
        valor = f + c
        fila.append(valor)
        
    # 🚨 MIRA BIEN LA SANGRÍA DE LAS CONDICIONES (Fuera del bucle interno)
    if len(fila) == 3:
        acumulador += fila[1] # Suma el elemento del casillero 1 de esa fila
        
    if f == 0:
        matrix.append(fila)
        continue
        
    acumulador *= 2

resultado_final = acumulador + len(matrix)

    


























    
