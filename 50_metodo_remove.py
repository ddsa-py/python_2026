print("Metodo remove()")
print()
vocales =["a","e","i","o","u"]
print(f"{vocales} \nElemento a eliminar: i")
vocales.remove("i")
print(vocales)
print()

vocales =["a","e","i","o","u"]
print(f"{vocales} \nElemento a eliminar: o")
vocales.remove("o")
print(vocales)
print()

vocales =["a","e","i","o","i"]
print(f"{vocales} \nElemento a eliminar: i")
vocales.remove("i")
print(vocales)
print()

vocales =["a","e","i","o","i"]
print(f"{vocales} \nElemento a eliminar: i con bucle")
for i in vocales:
    if i == "i":
        vocales.remove("i")
print(vocales)
print()

#se produce error
vocales =["a","e","i","o","i"]
print(f"{vocales} \nElemento a eliminar: I")
vocales.remove("I")
print(vocales)
print()


