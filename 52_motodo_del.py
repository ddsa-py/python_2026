vocales = ["a","e","i","o","u"]
print(f"Listas: {vocales}")
del vocales[3]
print(f"del vocales[3]: {vocales}")
print()

vocales = ["a","e","i","o","u"]
print(f"Listas: {vocales}")
del vocales[:2]
print(f"del vocales[:2]: {vocales}")
print()

vocales = ["a","e","i","o","u"]
print(f"Listas: {vocales}")
del vocales[:]
print(f"del vocales[:]: {vocales}")
print()

vocales = ["a","e","i","o","u"]
print(f"Listas: {vocales}")
del vocales #se genera un error ya que no existe la lista vocales
print(f"del vocales: {vocales}")
print()
