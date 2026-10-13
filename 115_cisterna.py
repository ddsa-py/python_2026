limite_seguro = 5000
litros_validados = 0
alertas_letra = 0
mensaje = "intentos "if alertas_letra <= 4 else "intento"
while True:
    volumen_crudo = input("Ingrese un valor numerico: ")
    try:
        litros_validados = int(volumen_crudo)
        break
    except ValueError as ve:
        alertas_letra += 1
        mensaje = "intentos " if alertas_letra < 4 else "intento"
        print(f"Error compañero, te quedan {5 - alertas_letra} {mensaje}")
    if alertas_letra >= 5:
        print("Fin del juego")
        break
while alertas_letra < 5:
    if litros_validados < limite_seguro:
        print("El estado de la carga es insuficiente")
    else:
        print("Perfecto carga validada")
    break
codigo_planta = (alertas_letra  * 300) + 100
print(f"codigo planta {codigo_planta}")
