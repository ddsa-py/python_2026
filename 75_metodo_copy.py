matrix_a = {}

while True:
    numero = input("Ingrese la cantidad que contendra su diccionario: ")
    print()
    if numero.isdigit():
        numero = int(numero)
        break
    else:
        print("Error, solo se acepna numeros, vuelva a intentar")
print()
for i in range(numero):
    dictionary_keys = input("Ingrese el nombre de la clave para el diccionario: ")
    dictionary_values = int(input("Ingrese el valor para la clave del diccionario: "))
    matrix_a[dictionary_keys] = dictionary_values

print()
for _ in range(1):
    print("Matriz original")
    print(matrix_a)
print()

clave_extra = input("Ingrese una nueva clave para el diccionario: ")
valor_extra =  input("Ingrese un nuevo valor para la clave: ")

simulacion_polar = matrix_a.copy()
simulacion_polar[clave_extra]= valor_extra
for _ in range(1):
    print("Matriz copia")
    print(simulacion_polar)
print()
resultado_control = (len(matrix_a) * len(simulacion_polar)) + 900
print(f"Resultado control: {resultado_control}")
