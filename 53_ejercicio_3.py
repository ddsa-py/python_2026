print("Cervecería Polar (Planta San Joaquín, Carabobo)".center(60,"*"))
print()
tanques_polar = [500, 200, 800]
guias_despacho = ["G-10", "G-20", "G-30", "G-40"]
prueba = guias_despacho[::-1]
print(f"Prueba con sciling: {prueba}")
historial_guias = guias_despacho[:]
resultado = tanques_polar[1] - len(guias_despacho)
tanques_polar[-1] = resultado
guias_despacho.reverse()

guia_procesada = guias_despacho.pop(2)

print(f"1. Guías Pasado Blindado: {historial_guias}")
print(f"2. Guía Procesada Pura:    {guia_procesada}")
print(f"3. Tanques Polar Final:    {tanques_polar}")
print(f"4. Guías Despacho Final:   {guias_despacho}")
