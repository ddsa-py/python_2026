print("El Validador de Sensores de una Planta Química\n")

while True:
    tipo = input("Ingrese el tipo de tubería (gas o agua): ").strip().lower()
    if tipo == "apagar":
        print("Cerrando panel de control químico...")
        break
    if tipo != "agua" and tipo != "gas":
        print("Error vuelva a intentar")
        continue
    codigo = input("Ingrese la lectura del sensor: ").strip()

    if tipo == "gas":
        temperatura_limpia = codigo.lstrip("!")
    else:
        temperatura_limpia = codigo.rstrip("w")
    if not temperatura_limpia.isdigit():
        print("Error... contiene letras corruptas ")
        continue
    print(f"🌡 Tubería de {tipo.title()} Monitoreada | Temperatura: {temperatura_limpia} °C | Normal.")
    break
    
    
    
