print("Alimentos Polar (Planta San Joaquín, Carabobo)")
print()
codigos_barras = [101, 505, 909, 505, 303]
estatus_empaque = ["Rechazado", "Aprobado", "Espera", "Rechazado", "Aprobado"]
barras_apertura =  codigos_barras[:]
indice_codigo = codigos_barras.index(505,2)
indice_estatus = estatus_empaque.index("Espera",1,4)
longitud = len(estatus_empaque[2])
codigos_barras[indice_codigo] *= longitud

print(f"1. Códigos Apertura:      {barras_apertura}")
print(f"2. Índice Código Buscado: {indice_codigo}")
print(f"3. Índice Estatus Buscado:{indice_estatus}")
print(f"4. Lista Códigos Final:   {codigos_barras}")
