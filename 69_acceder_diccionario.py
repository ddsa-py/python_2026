diccionario = {"a": 1,
               "e": 2
               }
print(diccionario)
print(f"Clave a: {diccionario['a']}")
print(f"Clave e: {diccionario['e']}")
print()

diccionario = {"numero": [18,20,28],
               "Grupo": {"a": 1, "b": 2}
               }
print(f"Clave numero: {diccionario['numero']}")
print(f"Clave Grupo: {diccionario['Grupo']}")
print(f"Clave numero posicion 1: {diccionario['numero'][1]}")
print(f"Clave Grupo  'b': {diccionario['Grupo']['b']}")
print(diccionario["z"])

