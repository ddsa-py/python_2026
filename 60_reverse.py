print(" AUDITORÍA DE RENDIMIENTO DE LOTES - ALIMENTOS POLAR ".center(60, "#"))
lotes_harina = ["H-10", "H-20", "H-30", "H-40", "H-50"]
harina_apertura = lotes_harina[:]

harina_descartada= []
harina_descartada.append(lotes_harina.pop())
harina_descartada.append(lotes_harina.pop(0))

lotes_harina[-1] = len(lotes_harina[-1]) * len(lotes_harina)


print(f"1. Harina Apertura:        {harina_apertura}")
print(f"2. Harina Descartada RAM:  {harina_descartada}")
print(f"3. Lista Harina Final RAM: {lotes_harina}")

nombre = "daniel"
nombre = list(nombre)
nombre.reverse()
print(f"{nombre}")

numeros = "123456"

numeros = list(numeros)
print(numeros)
print(numeros[::-1])

apellido = "salazar"
print(apellido)
print(list(apellido))
print(apellido)
