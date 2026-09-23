import copy

fila_num = int(input("Ingrese la cantidad de filas que desea para la matriz: "))
columna_num = int(input("Ingrese la cantidad de columnas que desea para la matriz: "))
matrix = []
for i in range(fila_num):
    fila=[]
    
    for _ in range(columna_num):
        fila.append(int(input(f"Ingrese el numero de la #{i} fila: ")))
        
    matrix.append(fila)
    
for fila in matrix:
    
    print(fila)


fila_num = 3
columna_num = 2
matrix = []
acumulador =0


for i in range(fila_num):
    fila = []
    for j in range(columna_num):
        valor_sensor = i * j
        fila.append(valor_sensor)
        
    if len(matrix) == 1:
        acumulador += 100
        continue
        
    matrix.append(fila)
    
    acumulador= acumulador + sum(fila)
    
print(f"Acumulador: {acumulador}{fila}")




















    

resultado_final = acumulador * len(matrix)
