print(" REPORTE HISTÓRICO DE SEGURIDAD DE TOLVAS - POLAR ".center(65, "="))
silos_polar = ("Silo-Harina", "Silo-Aceite", "Silo-Arroz", "Silo-Azúcar", "Silo-Soya")
print(f"Silos activos en Planta: {silos_polar}")
while True:
    numero = int(input(f"Ingrese un numero que desea auditar del o al {len(silos_polar) - 1}: "))
    if numero in range(len(silos_polar)):
        print(f"Auditoria de proceso: {silos_polar[numero]} operando en condiciones optimas")
        break
    else:
        print("Índice fuera de rango. Tolva inexistente. Intente de nuevo.")
codigo_cierre = (numero * len(silos_polar)) + 250
print(f"Código Verificación de Cierre: {codigo_cierre}")
