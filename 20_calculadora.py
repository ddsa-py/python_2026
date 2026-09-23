print("Calculadora con una sola variable")
print("")
print("******************")
print("*Menu de opciones*")
print("******************")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Division entera")
print("6. Exponente")
print("7. MOdulo o Resto")
print("")
numero = int(input("Introduce la opcion deseada: "))

if numero == 1:
    print("Elegiste Suma")
    numero =int(input("Introduce el primer numero: "))
    numero +=int(input("Introduce el segundo numero: "))
    print("El resultado de la Suma es: ",numero)
elif numero == 2:
    print("Elegiste Resta")
    numero =int(input("Introduce el primer numero: "))
    numero -=int(input("Introduce el segundo numero: "))
    print("El resultado de la Resta es: ",numero)
elif numero == 3:
    print("Elegiste Multiplicacion")
    numero =int(input("Introduce el primer numero: "))
    numero *=int(input("Introduce el segundo numero: "))
    print("El resultado de la Multiplicacion es: ",numero)
elif numero == 4:
    print("Elegiste Division")
    numero =float(input("Introduce el primer numero: "))
    numero /=float(input("Introduce el segundo numero: "))
     
    print("El resultado de la Division es: ",round(numero, 2))
elif numero == 5:
    print("Elegiste Division Entera")
    numero =int(input("Introduce el primer numero: "))
    numero //=int(input("Introduce el segundo numero: "))
    print("El resultado de la Division Entera es: ",numero)
elif numero == 6:
    print("Elegiste Exponente")
    numero =int(input("Introduce el primer numero: "))
    numero **=int(input("Introduce el segundo numero: "))
    print("El resultado del Exponente es: ",numero)
elif numero == 7:
    print("Elegiste Modulo o Resto")
    numero =int(input("Introduce el primer numero: "))
    numero %=int(input("Introduce el segundo numero: "))
    print("El resultado de la Modulo o Resto es: ",numero)
else:
    print("El valor ingresado es incorrecto")
print("")


5