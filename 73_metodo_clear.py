employees = {"Juan": {"edad": 28, "salario": 25000},
             "Maria": {"edad": 24, "salario": 20000}
             }
print(f"Diccionario original: {employees}")
print()

employees.clear()
print(f"Diccionario actualizado: {employees}")

inventario_planta = {"Almacen-1": 230,
                     "Almacen-2": {"pnt-1": 125, "pnt-2": 354, "pnt-3": 695}
                     }
variable_num = inventario_planta["Almacen-1"] * len(inventario_planta["Almacen-2"])
print(variable_num)

inventario_planta["Almacen-2"].clear()

print(inventario_planta)
