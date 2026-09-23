print("Ejericio practico".center(60,"*"))
print()
lista = ["A","a","B","b","c","E","E","f"]
print(f"Lista original: {lista}")

elemento = input("Introduce el elemento que deseas elimianr: ")

for _ in lista[:]:
    if elemento.lower() in lista[:]:
        lista.remove(elemento.lower())
    if elemento.upper() in lista[:]:
        lista.remove(elemento.upper())
print(lista)

datos = [10, 20, 30, 20, 40]
foto_pasado = datos[:]

datos.sort(reverse=True)
posicion = datos.index(20)

for _ in datos[:]:
    if 20 in datos:
        datos.remove(20)

resultado_final = sum(datos) + posicion + len(foto_pasado)
print(resultado_final, posicion)

