tupla1 = (1, 2, 3, 4, 5)
tupla2 = (8, 6, 4, 2, 0)
lista_resultado= []

print("Tupla 1:", end=" ")
print(f"{tupla1}".rjust(20, " "))
print("+".rjust(15, " "))

print("Tupla 2:", end=" ")
print(f"{tupla2}".rjust(20, " "))
print("             ".ljust(30, "="))

for tupla_1, tupla_2 in zip(tupla1, tupla2):
    resultado = tupla_1 +  tupla_2
    lista_resultado.append(resultado)
print("suma:", end=" ")
print(f"{tuple(lista_resultado)}".rjust(23, " "))

