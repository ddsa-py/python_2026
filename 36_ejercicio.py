print("Sistema de facturación automatizado".center(50,"+"))
print()
while True:
    codigo = input("Ingrese el codigo de paquete: ").strip()
    if codigo == "apagar":
        print("Cerrando sistema...")
        break
    if not "USA" in codigo:
        print("Error, el codigo debe empezar con 'USA', vuelva a intentar")
        continue
    variable_uno = codigo[:3]
    variable_dos = codigo[4:7]
    variable_tres = codigo[8:12]
    variable_cuatro = codigo[13:]
    print(f"[ORIGEN: {variable_uno}] | [DESTINO: {variable_dos}] | [AÑO: {variable_tres}] | [TRANSPORTE: {variable_cuatro}]")
    break

    
