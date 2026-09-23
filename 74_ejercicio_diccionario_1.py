almacen = {}

print("Primer Bloque llenado del diccionario")
print()


while True:
    cantidad_diccionario = input("Ingrese la cantidad que para la logitud del diccionario: ")
    if cantidad_diccionario.isdigit():
        cantidad_diccionario = int(cantidad_diccionario)
        break
    else:
        print("Error, solo se acepta un valor numerico, vuelva a intentarlo")
        print()
print()
for i in range(cantidad_diccionario):
    keys_dictionario = input("Ingrese el nombre de la clave del diccionario: ")
    values_dictionario = input("Ingrese el valor para la clave del diccionario: ")
    almacen[keys_dictionario] = values_dictionario
    
opcion = input("Ingrese si/no si desea crear un diccionario: ").lower()
if opcion == "si":
    while True:
        cantidad_sub_dictionary = input("Ingrese la cantidad para la longitud del sub-diccionario: ")
        if cantidad_sub_dictionary.isdigit():
            cantidad_sub_dictionary = int(cantidad_sub_dictionary)
            #print(cantidad_sub_dictionary)
            break
        else:
            print("Error, solo se acepta un valor numerico, vuelva a intentarlo")
    print()
    print("Segundo Bloque creacion y llenado del sub-diccionario")
    print()
    name_sub_dictionary = input("Ingrese el nombre del diccionario: ")
    almacen[name_sub_dictionary] = {}

    for i in range(cantidad_sub_dictionary):
        keys_sub_dictionary = input("Ingrese el nombre de la clave para el sub-diccionario: ")
        values_sub_dictionary = int(input("Ingrese el valor de la clave para el sub-dictionary: "))
        almacen[name_sub_dictionary][keys_sub_dictionary] = values_sub_dictionary
    print(f"Diccionario: {almacen}")
    lista_almacen_completa = list(almacen.items())
    lista_almacen_values = list(almacen[name_sub_dictionary].values())
    lista_almacen_keys = list(almacen[name_sub_dictionary].keys())
    prim_almacen_keys = lista_almacen_keys[0]
    print(f"Los nombres clave del sub-diccionario: {lista_almacen_keys}")
    print(f"Valores del dub-diccionario: {lista_almacen_values}")
    print(f"Lista completa del Diccionario: {lista_almacen_completa}")
 
    temp = int(input("Ingrese el valor de la nueva temperatura: "))
    almacen[name_sub_dictionary][prim_almacen_keys] = temp
    print(f"Diccionario modificado: {almacen}")
    
else:
    print(almacen)
























    

    
