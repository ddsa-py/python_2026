personas = [("Carlos", 30), ("Daniel",  25), ("Javier", 35)]
dict_personas = {person: edad for person, edad in personas}
print(dict_personas)
print("**************************************************")
personas = [("Carlos", 30), ("Daniel",  25), ("Javier", 35)]
dict_personas = {person: edad for person, edad in personas if edad >= 30}
print(dict_personas)
dict_pers= {}

for p, e in personas:
    dict_pers[p] = e
print(dict_pers, end = " ")


