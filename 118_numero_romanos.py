print("Numeros Romanos".center(40, "*"))
entrada_usuario = ""
resultado_romano = ""
num_romanos = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

while True:
    resultado_romano = ""
    entrada_usuario = input("Ingresa un numero entero para convertirlo en romano: ").strip()
    
    try:
        entrada_usuario = int(entrada_usuario)
        num = int(entrada_usuario)
        if entrada_usuario <= 0 or entrada_usuario > 3999:
            print("El número ingresado debe estar en un rango de 1 y 3999, vuelva a intentar")
            continue
    except ValueError:
        print("Error, debe ingresar numeros enteros positivos")
        continue

    for numero, letra in num_romanos.items():
        while entrada_usuario >= numero:
            entrada_usuario -= numero
            resultado_romano += letra
            
    print(f"{num} Número Romano: {resultado_romano} ")
    
    