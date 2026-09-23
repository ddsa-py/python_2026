print(" AUDITORÍA DE ALTO RENDIMIENTO - ALIMENTOS POLAR ".center(60, "#"))
camiones_polar = ["C-100", "C-200", "C-300", "C-400", "C-500"]

camiones_apertura = camiones_polar[:]

camiones_eliminados = []

camiones_eliminados.append(camiones_polar.pop(0))
camiones_eliminados.append(camiones_polar.pop(-1))
camiones_polar[-1] = len(camiones_polar[-1]) * len(camiones_polar)


print(f"1. Camiones Apertura:       {camiones_apertura}")
print(f"2. Camiones Eliminados RAM: {camiones_eliminados}")
print(f"3. Lista Camiones Final RAM:{camiones_polar}")

range(10,110,10)

numero= list(range(10,110,10))
print(numero)

nombre = "dioan daniel"

lista_nombre=list(nombre)
print(nombre, lista_nombre)


