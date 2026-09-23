print("ONTROL DE ACCESO BÚNKER".center(60,"="))
print()

while True:
    nombre = input("Ingrese el nombre del soldado: ").strip()
    if nombre == "APAGAR SENSOR" or nombre == "apagar sensor":
        print("Desactivando sistemas de seguridad...")
        break
    
    if not nombre.replace(" ","").isalpha():
        print("El nombre obligatoriamente debe contener únicamente letras y espacios, intenta de nuevo")
        continue
    nombre = nombre.capitalize()
    escuadron = input("Ingrese el Código del Escuadrón:")
    escuadron = escuadron.split()
    num_escuadron = len(escuadron)
    if num_escuadron > 3 or num_escuadron < 3:
        print("Error de longitud solo se permiten tres palabras, intente de nuevo")
        continue
    else:
        print(f"Soldado registrado: {nombre.ljust(25,".")}| ACCESO AUTORIZADO")
        break
    
        
    
