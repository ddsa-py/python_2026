tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla_concatenada = tupla1 + tupla2
print(f"Tupla concatenada: {tupla_concatenada}")
print(f"Tupla original #1 {tupla1}")
print(f"Tupla original #2 {tupla2}")

tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla1 += tupla2
print(f"Tupla concatenada: {tupla1}")
print(f"Tupla original #2 {tupla2}")
print()
tupla1 = (1,2,3)
lista_prueba = [4,5,6]
print(f"la tupla original #1 {tupla1} y la lista original: {lista_prueba}")
tupla1 += tuple(lista_prueba)
print(f"Tupla original concatenada: {tupla1}")
print(f"Lista prueba {lista_prueba}")







