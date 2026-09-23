vocales = ("a", "e", "i", "o", "u")
print(f"vocales {type(vocales)}")
print()
print(f"vocales[:3]: {vocales[:3]}")
var_1, var_2, var_3 = vocales[:3]
print(var_1, var_2, var_3)

print()
print("****************************************")
vocales_non = ("a", "b", "c", "d", "e")
print(vocales_non)
print(f"{vocales_non[1:]}")
var_1, var_2, var_3, var_4 = vocales_non[1:5]
print(var_1, var_2, var_3,var_4)


paises = ("mexico", "brasil", "argentina", "españa")
print(f"paises: {paises}")
p1, p2, p3 = paises[:3]
print(f"primer pais: {p1}")
print(f"Segundo pais: {p2}")
print(f"Tercer pais: {p3}")
p1 = paises[0]
print(f"pais [0]: {p1}")
p1 = paises[-1]
print(f"Ultimo pais: {p1}")
