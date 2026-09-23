print("El Sistema de Despacho de Cargas de Fibex Telecom".center(60,"*"))
print()
while True:
    codigo = input("Ingresar codigo del camión: ")
    if codigo == "apagar":
        print("Cerrando el sistema...")
        break
    if " " in codigo:
        print("Error, el codigo no puede contener espacios en blanco, vuelva a intentar")
        continue
    if "Fibex" not in codigo:
        print("Debe contener la palabra Fibex con letra mayuscula")
        continue
    codigo_num = len(codigo)
    if not (codigo_num >= 6 and codigo_num <=12):
        print("El codigo debe incluir entre 6 y 12 caracteres, vuelva a intentar")
        continue
    print(f"Camión autorizado, codigo: '{codigo}'")
    break
    
