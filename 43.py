print("El Auditor de Carga Aérea".center(60,"*"))
print()
acumulador =""

for i in range(10,51,5):
    if i == 35:
        print(f"Se cierra el muelle {i} por medidas de seguridad, 'Material peligroso'")
        print()
        break
        
    acumulador += "Muelle" + str(i) + "--"
print(acumulador.rstrip("--"))
    
