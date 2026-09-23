print(" AUDITORÍA MATRICIAL DE SILOS - ALIMENTOS POLAR ".center(60, "#"))
matrix = [[150,200,310],
          [420,150,890],
          [600,150,200]]

matrix_apertura = matrix[:]

peso_maximo = matrix[1][2]
peso_minimo = matrix[0][1]

matrix[0][1] *= (peso_maximo - peso_minimo)


print(f"1. Matrix Apertura:       {matrix_apertura}")
print(f"2. Peso Máximo Extraído:  {peso_maximo}")

rejilla_final = f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}"
print(f"3. Matrix Final RAM:\n{rejilla_final}")
