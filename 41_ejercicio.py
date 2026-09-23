print("El Generador de Códigos para una Línea de Autobuses".center(60,("*")))
print()
acumulador = ""
for i in range(5,27,3):
    
    acumulador = acumulador + "Asiento-" + str(i) + "/"
    

print(acumulador.rstrip("/"))
    
