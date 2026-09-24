print(" CONTROL DE LOGÍSTICA DE TRANSPORTE - POLAR ".center(65, "="))
flota_despacho = (
    ("Camion-01", "Valencia", 25),
    ("Camion-02", "Maracay", 18),
    ("Camion-03", "Caracas", 32)
)
total_toneladas = 0
print(f"{flota_despacho[0]}\n{flota_despacho[1]}\n{flota_despacho[2]}" )
for identificador, destino, carga in flota_despacho:
    total_toneladas += int(carga)
    print(f"El {identificador} va hacia: {destino} transportando {carga} toneladas")
codigo_verificacion = (total_toneladas * len(flota_despacho)) - 150
print(f"Carga Total Despachada: {total_toneladas} Ton")
print(f"Código Verificación Final: {codigo_verificacion}")

