almacen = {"codigo_planta-1": 245,
           "codigo_planta-2": {"codigo-1": 345, "codigo-2": 203, "codigo-3": 115
            }
           }
print(f"Diccionario Almacen: {almacen}")
almacen_listas = list(almacen["codigo_planta-2"].keys())

print(f"Lista almacen: {almacen_listas}")

