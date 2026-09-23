print("Metodo sum")
numeros = [1,2,3]
print(f"La suma de la lista numeros: {numeros}: {sum(numeros)}")

numeros = [1,2,3]
print(f"La suma de la lista numeros con valor inicial 10: {numeros}: {sum(numeros,10)}")
numeros = [1,2,3]
print(f"La suma de la lista numeros con valor inicial 20: {numeros}: {sum(numeros,20)}")
numeros = [1,2,3, True]
print(f"La suma de la lista numeros con valor True: {numeros}: {sum(numeros)}")
numeros = [1,2,3, "a"]

#con errorprint(f"La suma de la lista numeros con un string {numeros}: {sum(numeros)}")
numeros = [1,2,3.5, True]
print(f"La suma de la lista numeros con valor float: {numeros}: {sum(numeros)}")

numeros = [1,2,3.5, True]
print(f"La suma de la lista numeros con valor -2: {numeros}: {sum(numeros, -2)}")
print()
print(" AUDITORÍA MATEMÁTICA CERVECERÍA POLAR - VIDEO 57 ".center(60, "#"))
pesos_lotes = [120, 340, 50, 210]
alertas_val = [False, True, False]
pesos_apertura = pesos_lotes[:]
total_desplazado = sum(pesos_lotes, -20)
total_alertas = sum(alertas_val)
resultado = total_alertas + len(pesos_lotes)
pesos_lotes[-1] *=  resultado

print(f"1. Pesos Apertura:        {pesos_apertura}")
print(f"2. Total con Base -20:    {total_desplazado}")
print(f"3. Total Alertas Binarias:{total_alertas}")
print(f"4. Lista Pesos Final RAM: {pesos_lotes}")
