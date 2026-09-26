name = ("Ana", "Gerardo", "Maria", "Carlos", "Daniela", "Daniel", "Amanda")
#lista_name = list(name)

print(f"Lista de nombres: {name}")

while True:
    num = int(input(f"Ingrese un numero entre 0 hasta {len(name) - 1}: "))
    if 0 <= num < len(name):
        for nombre in range(len(name)):
            if nombre == num:
                print(f"El nombre es: {name[nombre]}")
                break
        break
    else:
        print("El numero sobrepasa el limite, vuelva a intentarlo")



