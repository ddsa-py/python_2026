carga_estandar = 1500
bultos_seguros  = 0
errores_teclado = 0
while True:
    entrada_cruda = input("Ingresa un valor numerico: ")
    try:
        bultos_seguros = int(entrada_cruda)
        break
    except ValueError:
        errores_teclado += 1
        print(f"Error, solo se admiten valores numericos, te quedan {5 - errores_teclado}")
        
    if errores_teclado >= 5:
        print(f"💥 Tolva de empaque bloqueada por seguridad. Game Over")
        break
while errores_teclado < 5:
    if bultos_seguros < carga_estandar:
        print(f"¡💥 Alerta de merma! Faltan bultos, la carga está en {bultos_seguros} kg. Idiota, súbele material")
    else:
        
        print(f"🏆 Tolva validada con {bultos_seguros} kg. Despacho en verde total")
    break
codigo_planta = (errores_teclado * 200) + 400
print(f"Código Control de Planta: {codigo_planta}")