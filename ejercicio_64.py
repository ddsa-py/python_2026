import copy
print(" AUDITORÍA DE BUCLES ANIDADOS - ALIMENTOS POLAR ".center(60, "#"))
matriz_silos = [[10, 85, 20],
                [90, 30, 40],
                [100, 115, 130]]

silos_apertura = copy.deepcopy(matriz_silos)
print(f"1. Silos Apertura RAM:     {silos_apertura}")
print()
f=0
for fila in matriz_silos:
    c=0
    for columna in fila:
        if columna >= 80:
            matriz_silos[f][c] *= 2
        c +=1
    f+=1
rejilla_final = f"{matriz_silos[0]}\n{matriz_silos[1]}\n{matriz_silos[2]}"
print(f"2. Matriz Silos Final RAM:\n{rejilla_final}")
        
    



import copy

# Una matriz diminuta de 2x2
matriz = [[1,2],
          [3,4]]

f = 0 
for fila in matriz:
    c = 0 
    for pelota in fila:
        matriz[f][c] = matriz[f][c] * 10
        
        c += 1  
        
    f += 1  
    print()
print(matriz)


