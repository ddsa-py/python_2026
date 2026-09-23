import copy
print(" AUDITORÍA MATRICIAL DE VOLUMEN - ALIMENTOS POLAR ".center(60, "#"))
matriz_pesos = [[10, 50, 20, 80],
                [90, 30, 40, 15],
                [100, 115, 60, 70],
                [35, 45, 120, 85]]

pesos_apertura = copy.deepcopy(matriz_pesos)

f=0
for  fila in matriz_pesos:
    c=0
    for columna in fila:
        if matriz_pesos[f][c] >= 80:
            matriz_pesos[f][c] *= 2
        c+=1
    f+=1

print(f"1. Pesos Apertura RAM:\n{pesos_apertura[0]}\n{pesos_apertura[1]}\n{pesos_apertura[2]}\n{pesos_apertura[3]}")

rejilla_final = f"{matriz_pesos[0]}\n{matriz_pesos[1]}\n{matriz_pesos[2]}\n{matriz_pesos[3]}"
print(f"2. Matriz Pesos Final RAM:\n{rejilla_final}")

print("\n")


import copy

print(" AUDITORÍA CRIPTOGRÁFICA MATRICIAL - ALIMENTOS POLAR ".center(60, "#"))
matriz_seguridad = [["P-1", "A-Ok", "P-2"],
                    ["B-X", "P-3", "B-Y"],
                    ["P-4", "P-5", "C-Z"]]

seguridad_apertura = copy.deepcopy(matriz_seguridad)

f=0
for fila in matriz_seguridad:
    c=0
    for columna in fila:
        if "P" in matriz_seguridad[f][c] and len(matriz_seguridad[f][c]) <= 3:
            matriz_seguridad[f][c] *= len(matriz_seguridad[2][2])
        c+=1
    f+=1


print(f"1. Seguridad Apertura RAM: \n{seguridad_apertura[0]}\n{seguridad_apertura[1]}\n{seguridad_apertura[2]}")
print()
rejilla_final = f"{matriz_seguridad[0]}\n{matriz_seguridad[1]}\n{matriz_seguridad[2]}"
print(f"2. Matriz Cifrada Final RAM:\n{rejilla_final}")

        
            
            
        










































































