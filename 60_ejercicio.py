numeros = [1,2,3,4,5]
lista=[]
print(numeros)

    
lista.append(numeros.pop(0))
lista.append(numeros.pop())
print(numeros)
print(lista)
print()
print(" AUDITORÍA MATRICIAL ALIMENTOS POLAR - VIDEO 61 ".center(60, "#"))
matriz_polar = [[10, 20], [30, 40], [50, 60]]

matriz_apertura = matriz_polar[:]
bloque_despachado = matriz_polar.pop(2)

matriz_polar[0] = len(bloque_despachado) * sum(bloque_despachado)


print(f"1. Matriz Apertura:       {matriz_apertura}")
print(f"2. Bloque Despachado:     {bloque_despachado}")
print(f"3. Matriz Final RAM:      {matriz_polar}")

print()
print(" AUDITORÍA DE REPASO ALIMENTOS POLAR - VIDEO 60 ".center(60, "#"))
silos_polar = ["S-10", "S-20", "S-30", "S-40", "S-50"]
silos_apertura  = silos_polar[:]

silos_eliminados = []
silos_eliminados.insert(0,silos_polar.pop(-1))
silos_eliminados.insert(0,silos_polar.pop(0))
silos_polar[-1] =  len(silos_polar[-1]) * (len(silos_eliminados))
 

print(f"1. Silos Apertura:        {silos_apertura}")
print(f"2. Silos Eliminados RAM:  {silos_eliminados}")
print(f"3. Lista Silos Final RAM: {silos_polar}")





































