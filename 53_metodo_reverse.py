vocales = ["a","e","i","o","u"]
print(f"Lista: {vocales}")
vocales.reverse()
print(f"Lista invertida: {vocales}")
print(f"Posicion 0: {vocales[0]}")


print()

vocales.reverse()
print(f"Lista invertida: {vocales}")
print(f"Posicion 0: {vocales[0]}")
print()
print("Planta de Distribución de Pepsi en la Zona Industrial de Valencia")
numeros = [10, 20, 30]
letras = ["A", "B", "C", "D"]
historial_letras = letras[:]
ultima_posicion = len(letras) // 2
numeros[-1] = numeros[0] * ultima_posicion
letras.reverse()
letra_despachada = letras.pop(3)
print(f"1. Letras Pasado:  {historial_letras}")
print(f"2. Letra Sacada:   {letra_despachada}")

print(f"3. Lista Números:  {numeros}")
print(f"4. Lista Letras:   {letras}")
