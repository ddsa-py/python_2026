name = ("Ana", "Gerardo", "Maria", "Carlos", "Daniela", "Daniel", "Amanda")
apuntador = 0
while apuntador == 0:
    num = int(input(f"Ingrese un numero del 0 al {len(name) - 1} "))
    if 0 <= num < len(name):
        print(f"el nombre es: {name[num]}")
        apuntador = 1
    else:
        print("Ingrese un numero valido")



