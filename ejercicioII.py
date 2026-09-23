import copy
print(" AUDITORÍA DE TRANSPOSICIÓN ASIMÉTRICA - ALIMENTOS POLAR ".center(60, "#"))


matriz_control = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]


control_apertura = copy.deepcopy(matriz_control)

f=0
for fila in matriz_control:
    c=0
    for columna in fila:
        if f > c:
            matriz_control[f][c] += matriz_control[c][f]
        c+=1
    f+=1

print(f"1. Control Apertura RAM:")
rejilla_apertura = f"{control_apertura[0]}\n{control_apertura[1]}\n{control_apertura[2]}"
print(rejilla_apertura)
print()
print(f"2. Matriz Mutada Final RAM:")
rejilla_final = f"{matriz_control[0]}\n{matriz_control[1]}\n{matriz_control[2]}"
print(rejilla_final)



import copy
print(" AUDITORÍA MATRICIAL DE RESOLUCIÓN - ALIMENTOS POLAR ".center(60, "#"))
codigos_tolvas = [[5, 12], [8, 15]]

tolvas_apertura = copy.deepcopy(codigos_tolvas)

f=0
for i in codigos_tolvas:
    c=0
    for e in i:
        if codigos_tolvas[f][c] % 2 == 0:
            codigos_tolvas[f][c] *= 10
        c+=1
    f+=1


print(f"1. Tolvas Apertura RAM: \n{tolvas_apertura[0]}\n{tolvas_apertura[1]}")

rejilla_final = f"{codigos_tolvas[0]}\n{codigos_tolvas[1]}"
print(f"2. Matriz Tolvas Final:\n{rejilla_final}")



matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

for fila in matrix:
    for columna in fila:
        print(columna, end=" ")
    print()












        
    
            





    





















            
