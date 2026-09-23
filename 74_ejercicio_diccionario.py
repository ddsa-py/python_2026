almacen = {}

cantidad = int(input("Ingrese la cantidad para crear el diccionario: "))

print(f"Bloque 1")

for i in range(cantidad):
    keys_plano = input("Ingrese el nombre para la clave del diccionario: ")
    values_plano = int(input("Ingrese el valor para cada clave del diccionario: "))
    almacen[keys_plano] = values_plano


#opcion = input("Ingrese 'si'/'no' para crear un sub-diccionario ").lower()

#if opcion == "si":
print(f"Bloque 2")
nombre_sub_diccionario = input("Ingrese el nombre para el sub-diccionario: ")
almacen[nombre_sub_diccionario] = {}
cantidad_sub_diccionario = int(input("Ingrese la cantidad para el sub-diccionario: "))
    #while True:
     #   if not cantidad_sub_diccionario.isdigit():
      #      print("Error, intente de nuevo solo numeros")
       #     continue
        #else:
for i in range(cantidad_sub_diccionario):
    keys_sub_diccionario = input("Ingrese el nombre de la clave para el sub-diccionario: ")
    values_sub_diccionario = int(input("Ingrese el valor de la clave para el sub-diccionario: "))
    almacen[nombre_sub_diccionario][keys_sub_diccionario] = values_sub_diccionario
#else:
    #print(f"Diccionario {almacen}")
        
print(f"Diccionario almacen: {almacen}")
        #print()

lista_almacen = list(almacen[nombre_sub_diccionario].keys())

keys_diccionario = lista_almacen[0]

        #print(f"Lista sud-diccionario claves: {lista_almacen} - primera clave: {keys_diccionario}")
lista_almacen_original = list(almacen.items())
temp = int(input("Ingrese la temperatura corregida: "))
        #print(lista_almacen_original)
        #print()
almacen[nombre_sub_diccionario][keys_diccionario] = temp
lista_almacen_values = list(almacen[nombre_sub_diccionario].values())
resultado_auditoria = (len(lista_almacen_values) + temp) * 100
print(f"Diccionario modificado: {almacen}")
print()
print(f"Resultado auditoria: {resultado_auditoria}")














