import copy

matrix_a = [[2, 3],
            [4, 5]]

matrix_b = [[1, 2],
            [3, 4]]

matrix_res = []

print(" MONITOREO DE VIAJES DEL MENSAJERO K ".center(60, "#"))

# TRIPLE BUCLE PURO
for i in range(2):
    fila = []
    for j in range(2):
        acumulador = 0
        for k in range(2):
            # Guardamos los números que se van a multiplicar en este milisegundo
            num_a = matrix_a[i][k]
            num_b = matrix_b[k][j]
            
            # El mensajero hace la escala e intersecta los puntos
            acumulador += num_a * num_b
            
            # 🚨 PRINT MONITOR: Nos muestra qué números se están chocando en este instante
            print(f"Fila {i}, Columna {j} ──> Mensajero k={k} multiplicó: {num_a} * {num_b}")
            
        fila.append(acumulador)
    matrix_res.append(fila)

print("#" * 60)
print(f"Matriz Resultado Final Automatizada:\n{matrix_res}")
