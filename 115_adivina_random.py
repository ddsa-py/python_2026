import random
print("Binvenido adivina el numero secreto")
print("He seleccionado un numero entre 1 al 100. Adivina cual es")
numero = random.randint(1, 100)
print(numero)
contador = 0
 
while contador < 5: 
    try:
        num = int(input("Ingrese un numero: "))
        
    except ValueError:
        print("Error intente de nuevo")
        contador += 1