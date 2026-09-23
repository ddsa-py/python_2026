print("Distribuidora de Alimentos Polar en la Zona Industrial de Valencia".center(60,"*"))
print()

marcas = ["P.A.N.", "Juana", "P.A.N.", "Demasa", "P.A.N."]
inventario_apertura = marcas[:]

marcas.remove("Juana")
inventario_mediodia = marcas[:]

#marcas.remove("PAN")
#inventario_fallido = marcas[:]
#list.remove(x): x not in list

print(f"1. Apertura de Planta: {inventario_apertura}")
print(f"2. Reporte Mediodía:   {inventario_mediodia}")
print(f"3. Stock Final Vivo:   {marcas}")
#prueba con ciclo for
print()
for i in marcas[:]:
    if i == "P.A.N.":
        marcas.remove("P.A.N.")
print(f"Prueba con ciclo for: {marcas}")
print()

numeros = [10, 20]

# Intentas recorrer la lista directa y duplicar cada número al final
for i in numeros[:]:
    numeros.append(i * 2) # ◄── ¡LA TRAMPA!
    print(i)
print(numeros)

    
