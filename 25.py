
while True:
    codigo = input("Ingrese por favor el código del paquete: ").strip()
    if codigo== "fin":
        print("Apagando el escáner de envíos...")
        break
    if not codigo.isdigit():
        print("¡Error!: El código de barras solo contiene números.")
        continue
    digitos = len(codigo)
    if digitos == 6:
        print("¡Código Válido!, posee exactamente: ", digitos, "digitos, Paquete registrado en el sistema.")
        break
    else:
        print("¡Código Inválido!: Debe tener exactamente 6 dígitos. Tu código tiene: ",digitos," caracteres. Intente de nuevo.")






















    
