print("*************************************************")
print("*El Validador de Retiros de un Cajero Automático*")
print("*************************************************")

print("")

while True:
    monto= input("Ingrese monto a retirar: ").strip()
    if not monto.isdigit():
        print("¡Error!: Ingrese un monto numérico válido.")
        continue
    if monto == "99":
        print("Apagando cajero automático por mantenimiento...")
        break
    if monto == "0":
        print("Ingrese otro monto, no es posible retirar 0$")
        continue
    monto = int(monto)
    if monto <= 500:
        print("¡Retiro Autorizado!: Procesando entrega de efectivo.")
    else:
        print("Límite Excedido: El monto máximo de retiro es $500.")
