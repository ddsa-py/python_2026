while True:
    texto = input("Ingrese texto: ").strip().lower()
    if len(texto) != 0:
        print()
        break
    else:
        print("Error, debe escribir texto, vualva a intentar")
conteo_letra_m = 0    
frecuencias_polar = dict.fromkeys(texto, 0)

for i in texto:
    frecuencias_polar[i] += 1
print(frecuencias_polar)

longitud_diccionario = len(frecuencias_polar)

conteo_letra_m = frecuencias_polar.get("m", 0)

if conteo_letra_m == 0:
   print(f"Conteo de la letra sin 'm': {conteo_letra_m}")
else:
    print(f"Longitud diccionario 'm': {longitud_diccionario}")

    
balance_frecuencias = (longitud_diccionario * conteo_letra_m) + len(texto)
print(f"Balance de frecuancias: {balance_frecuencias}")   


