import copy
print(" AUDITORÍA MATRICIAL AVANZADA - EMPRESAS POLAR ".center(60, "#"))
matriz_empaque = [[120, 300, 450],
                  [510, 220, 630],
                  [700, 850, 910]]

empaque_apertura = copy.deepcopy(matriz_empaque)

techo_presion = matriz_empaque[-1][-2]
piso_temperatura = matriz_empaque[-3][-3]

matriz_empaque[0][1] //= techo_presion - (piso_temperatura * len(matriz_empaque[0]))


print(f"1. Empaque Apertura RAM:   {empaque_apertura}")
print(f"2. Techo Presión Extraído: {techo_presion}")
print(f"3. Piso Temperatura Extra: {piso_temperatura}")
rejilla_final = f"{matriz_empaque[0]}\n{matriz_empaque[1]}\n{matriz_empaque[2]}"
print(f"4. Matriz Empaque Final RAM:\n{rejilla_final}")

matrix =[[1,2,3],[4,5,6],[7,8,9]]

for fila in matrix:
    for columna in fila:
        print(columna, end="")
