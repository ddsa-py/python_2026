print(" AUDITORÍA SIMULTÁNEA DE SILOS - ALIMENTOS POLAR ".center(60, "#"))
print()

print("Ejercicio".center(60,"#"))
print()
registro_silos = ["s-2", "S-2", "S-5", "s-2", "S-2", "S-9"]
silos_apertura = registro_silos[:]
contador = registro_silos.count("s-2") + registro_silos.count("S-2")
for _ in registro_silos[:]:
    if "S-2".lower() in registro_silos[:]:
        registro_silos.remove("S-2".lower())
    if "S-2".upper() in registro_silos[:]:
        registro_silos.remove("S-2".upper())

auditoria_silos = len(registro_silos) * len(silos_apertura)


print(f"1. Silos Apertura:        {silos_apertura}")
print(f"2. Reporte Final Neto:    {auditoria_silos}")
print(f"3. Lista Silos Final RAM: {registro_silos}")
print(f"4. Lista s-1 y S-1 eliminados en registro silos: {contador}")
print()


















































print(" AUDITORÍA SIMULTÁNEA DE BARRAS - ALIMENTOS POLAR ".center(60, "#"))
registro_barras = ["h-5", "H-5", "H-9", "h-5", "H-5", "H-7", "h-5"]
barras_apertura = registro_barras[:]
contador = registro_barras.count("h-5") + registro_barras.count("H-5")
for _ in registro_barras[:]:
    if "h-5".lower() in registro_barras[:]:
        registro_barras.remove("h-5".lower())

    if "h-5".upper() in registro_barras[:]:
        registro_barras.remove("h-5".upper())

reporte_barras = (len(registro_barras )  * len(barras_apertura)) + len("H-9")

print(f"1. Barras Apertura:       {barras_apertura}")
print(f"2. Reporte Final Neto:    {reporte_barras}")
print(f"3. Lista Barras Final RAM: {registro_barras}")
print(f"3. Total eliminados: {contador}")

print()

print(" AUDITORÍA MAESTRA DE EXTREMOS Y CONTEO - ALIMENTOS POLAR ".center(60, "#"))
registro_pesos = [420, 150, 890, 150, 310, 150, 600]
estatus_lotes  = ["l-2", "L-2", "L-5", "l-2", "L-2", "L-9", "l-2"]
lotes_apertura  = estatus_lotes[:]
contador = estatus_lotes.count("l-2") + estatus_lotes.count("L-2")

for _ in estatus_lotes[:]:
    if "l-2".lower() in estatus_lotes[:]:
        estatus_lotes.remove("l-2".lower())
    if "l-2".upper() in estatus_lotes[:]:
        estatus_lotes.remove("l-2".upper())

peso_maximo = max(registro_pesos)
peso_minimo = min(registro_pesos)

reporte_final = len(estatus_lotes) * len(lotes_apertura) + (peso_maximo - peso_minimo)


print(f"1. Lotes Apertura:        {lotes_apertura}")
print(f"2. Peso Máximo Detectado: {peso_maximo}")
print(f"3. Peso Mínimo Detectado: {peso_minimo}")
print(f"4. Reporte Final Neto:    {reporte_final}")
print(f"5. Lista Lotes Final RAM: {estatus_lotes}")
print(f"6. Total eliminados: {contador}")




# Generar un separador de reporte en la consola 5 veces
for _ in range(5):
    _
print("#" * 20)

numeros = [1,2,3,4,5]
print(f"Lista numeros: {numeros}")
lista = []
if _ in numeros[:]:
    num2 = numeros.pop()
    lista.insert(0,num2)
    num1 = numeros.pop(0)
    lista.insert(0,num1)
print(f"Lista numeros restantes: {numeros}")
print(f"Lista de numeros eliminados: {lista}")






































































































