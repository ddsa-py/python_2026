print("Ascensor inteligente").strip()
print()
pisos_acumulados = ""

for i in range(2,21,2):
    pisos_acumulados += str(i) + ","
    
print("Los pisos de los ascensores es: " , pisos_acumulados.rstrip(","))
