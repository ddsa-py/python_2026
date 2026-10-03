lista_num = []
for i in range(10):
    elemento = i ** 2
    lista_num.append(elemento)
print(lista_num)

lista_num_compresion = [j ** 2 for j in range(10)]
print(lista_num_compresion)
print("par impar")
lista_pares = []
for i in range(10):

    if i % 2 == 0:
        x = i ** 2
        lista_pares.append(x)
    else:
        lista_pares.append(i)

print(lista_pares)
print()
print("par con compresion")
lista_par_compresion = [i ** 2 for i in range(10) if i % 2 == 0]
print(lista_par_compresion)










