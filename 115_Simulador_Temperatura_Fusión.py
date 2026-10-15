punto_fusion = 28
contador_global = 0
temperatura_usuario = 0
tiros_reserva = 0
while contador_global <= 5:
    while True:
        num = input("Ingrese un valor numerico: ")
        try:
            temperatura_usuario = int(num)
            break
        except ValueError as ve:
            contador_global += 1
            tiros_reserva = 5 - contador_global
            mensaje = "intento" if tiros_reserva == 1 or tiros_reserva == 0 else "intentos"
            print(f"Error, no se admiten letras, {tiros_reserva} {mensaje}")
            if contador_global >= 5:
                break


    contador_global += 1
    if temperatura_usuario == punto_fusion:
        print("Lo lograste a la perfeccion")
        break
    if contador_global >= 5 or int(num) == str:
        print("No lo lograste")
        break
    tiros_reserva = 5 - contador_global
    mensaje = "intento" if tiros_reserva == 1 or tiros_reserva == 0 else "intentos"
    if punto_fusion < temperatura_usuario:
        print(f"Bro bajale, {tiros_reserva} {mensaje}")
    elif punto_fusion > temperatura_usuario:
        print(f"Bro subele, {tiros_reserva} {mensaje}")
codigo_final = (contador_global * 500) + 300
print(f"Contador final: {codigo_final}")  
    
    
    
    