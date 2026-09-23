#ejercicio 1
print("*********Ejercicio #1*****************")
print()
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas" : 4
          }

print(f"Diccionario original: {fruits}")
print(f"Valor de la manzana: {fruits["manzanas"]}")
manzana = fruits.get("manzanas")
print(f"Valor de la manzana: {manzana}")
print()
#2 ejercicio
print("*********Ejercicio #2*****************")
print()
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas" : 4
          }
print(f"Diccionario original: {fruits}")
update_f = fruits.setdefault("mango", 6)
setdefaul_f = fruits.update({"bananas": 5})
variable = fruits["uvas"] = 3
print(f"Diccionario modificado: {fruits}")
print()
#3 ejercicio
print("*********Ejercicio #3*****************")
print()
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas" : 4
          }
print(f"Diccionario original: {fruits}")
peras_num1 = fruits.pop("peras", 2)
print(f"Diccionario modificado: {fruits}")
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas" : 4
          }
del fruits["peras"]
print(f"Diccionario modificado: {fruits}")
#ejercicio 4

print()
print("*********Ejercicio #4*****************")

fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas" : 4
          }
print(f"Diccionario original: {fruits}")
lista_total = list(fruits.items())
lista_key = list(fruits.keys())
lista_value = list(fruits.values())
print(f"Diccionario modificado lista completa: {lista_total}")
print(f"Diccionario modificado lista key: {lista_key}")
print(f"Diccionario modificado lista value: {lista_value}")
print()
#ejercicio 5
print("*********Ejercicio #5*****************")
print()
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas" : 4
          }

print(f"Diccionario original: {fruits}")


if "manzanas" in fruits:
    print("True")
else:
    print("False")





































