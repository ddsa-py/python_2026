print("***********************************************************************")
print("*El Desafío: El Control de Capacidad de un Estacionamiento Inteligente*")
print("***********************************************************************")

print("")


while True:
    puesto= input("Ingrese la cantidad de puestos ingresados: ").strip()
    if not puesto.isdigit():
        print("¡Error!: Ingrese un número válido.")
        continue
    if puesto == "404":
        print("Apagando sistema del estacionamiento...")
        break
    puesto = int(puesto)
    if puesto > 0:
        print("¡Acceso Autorizado!: Abriendo barrera.")
    else:
        print("Estacionamiento Lleno: Acceso Denegado.")
    
