vocales = ["a","e","i","o","u","a"]
print(f"Lista: {vocales}")
print(f"\nLa letra 'a' esta en la posicion: {vocales.index("a")}")
print(f"\nLa letra 'i' esta en la posicion: {vocales.index("i")}")
print(f"\nLa letra 'u' posicion 2-final esta en la posicion: {vocales.index("u", 2)}")
print(f"\nLa letra 'i' posicion 2-4 esta en la posicion: {vocales.index("i", 2, 4)}")
#prueba que produce error list= print(f"\nLa letra 'u' posicion 2-4 esta en la posicion: {vocales.index("u", 2, 4)}")
print()
inicio=0
for i in vocales[:]:
    if i == "a":
        volc= vocales.index("a",inicio)
        print(volc)
        inicio = volc + 1
        
#porque imprimio dos 0 deberia imprimir 0 y 5 no?

print()
tanques = [100, 250, 150, 400, 150]
estatus = ["Vacio", "Lleno", "Alerta", "Vacio", "Lleno"]
tanques_apertura = tanques[:]
indice_tanque= tanques.index(150,3) #4
indice_alerta =  estatus.index("Alerta",1, 4) # 2
resul = len(estatus[indice_alerta])
resultado = resul * len(tanques)

tanques[indice_tanque] = resultado

print(f"1. Tanques Apertura: {tanques_apertura}")
print(f"2. Índice Aditivo:   {indice_tanque}")
print(f"3. Índice Alerta:    {indice_alerta}")
print(f"4. Lista Tanques RAM: {tanques}")
