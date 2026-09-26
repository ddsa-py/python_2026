tupla_exer = (5, 8, 3, 3, 1, 6, 2)
print(tupla_exer)
num = int(input("Cual de estos numeros quiere modificar por 0: "))
tupla_lista = list(tupla_exer)
#print(tupla_lista)
for i in range(len(tupla_lista)):
    if tupla_lista[i] == num:
        tupla_lista[i] = 0
print(tuple(tupla_lista))









