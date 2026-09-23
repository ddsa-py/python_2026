print("El Auditor de Equipaje de Mano (Aeropuerto de Maiquetía)".center(70,"*"))
print()
#num = 0
equipaje = input("Ingresa  el codigo el equipaje: ").strip()

for i in equipaje:
    if i == "!":
        break
    elif i in "1234567890":
        num= 0
        num += int(i)
        
print()        
print(f"Peso total acumulado antes de la alerta {num}Kg")

nombres = ["dani", "ernesto", "luis"]

for i in nombres:
    # Esta variable es MOMENTÁNEA. Nace y muere en cada vuelta.
    nombre_limpio = i.upper() 
    
    print(f"Procesando: {nombre_limpio}")
print(F"Nombres originales {nombres}")
