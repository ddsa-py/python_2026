print("El Validador de Moneda Corto".center(60,"*"))
print()
while True:
    transf = input("Ingrese el detalle de la transferencia: ").strip()
    if transf == "apagar":
        print("Cerrando el sitema")
        break
    if "$" not in transf:
        print("❌ Transmisión rechazada: Falta la moneda de cambio.")
        continue
    print("✅ Transferencia Procesada con Éxito.")
    break
