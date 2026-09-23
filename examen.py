matriz_compleja = [[10,20],
                   [30, 40]]


acumulador_planta =0
conteo_vueltas =0

for fila in matriz_compleja:
    for elemento in fila:
        conteo_vueltas += 1
        if elemento % 20 == 0:
            acumulador_planta += elemento
            continue
        acumulador_planta += 5

resultado_final = acumulador_planta * conteo_vueltas
print(resultado_final)
