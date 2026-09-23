print("************************************")
print("*Administrador de un Tanque de Agua*")
print("************************************")
print("")
print("Opciones:")
print("")
print("1 - Llenado Inicial y Recarga")
print("2 - Consumo o Vaciado")
print("3 - Duplicar Reserva de Emergencia")
print("")

litros = int(input("Por favor indicar la opcion: "))
print("")
if litros == 1:
    print("Elegiste Llenado")
    print("")
    litros= int(input("Cuántos litros de inicio tiene: "))
    litros+=int(input("Cuántos litros entran de la tubería: "))
    print("El tanque ahora tiene: ",litros," litros.")
elif litros == 2:
    print("Elegiste Consumo")
    print("")
    litros= int(input("Cuántos litros actuales posee: "))
    litros-=int(input("Cuántos litros gasto en su casa: "))
    print("El tanque ahora tiene: ",litros," litros.")
elif litros == 3:
    print("Elegiste Duplicar Reserva")
    print("")
    litros= int(input("Cuántos litros actuales posee: "))
    litros*=2
    print("La reserva mística ahora tiene: ",litros," litros.")
else:
    print("Opcion incorrecta")
    
    
