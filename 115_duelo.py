capacidad_maxima = 8000
registro_inyectado = 0
fallos_datos = 0
tiros_reserva = 0
while True:
    num = input("Ingrese un numnero: ")
    try:
        registro_inyectado = int(num)
        break
    except ValueError as ve:
        fallos_datos += 1
        fallos_datos_al = 5 - fallos_datos
        mensaje = "intento" if fallos_datos_al == 1 or fallos_datos_al == 0 else "intentos"
        print(f"Amigo fallaste solo datos numerico, te quedan {fallos_datos_al} {mensaje}")
    if fallos_datos >= 5:
        print("Fin del juego")
        break
while fallos_datos < 5:
    if registro_inyectado < capacidad_maxima:
        print(f"Carga incompleta, regargar mas, agregar")
    else:
        print(f"Cargar perfecta")
    break
codigo_final = (fallos_datos * 400) + 200
print(f"Codigo final: {codigo_final}")
