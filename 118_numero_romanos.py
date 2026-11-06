print("Numeros Romanos".center(40, "*"))
entrada_usuario = ""
num_romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
num_romanos_suma = 0
while True:
    entrada_usuario = input("Ingresa un numero entero para convertirlo en romano: ")
    try:
        entrada_usuario = int(entrada_usuario)
        if entrada_usuario <= 0 or entrada_usuario > 3999:
            print("El número ingresado debe estar en un rango de 1 y 3999, vuelva a intentar")
            continue
    except ValueError:
        print("Error, debe ingresar numeros enteros positivos")
    for romano, numero in num_romanos.items():
        if entrada_usuario == 1:
            print(romano)
            