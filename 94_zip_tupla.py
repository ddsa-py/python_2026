print(" AUDITORÍA MAESTRA DE DESPACHOS PARALELOS - POLAR ".center(65, "="))
unidades_transporte = ("Camion-Alfa", "Camion-Beta", "Camion-Gamma", "Camion-Delta")
bultos_cargados = (450, 600, 350, 500)
destinos_ruta = ("Valencia", "Maracay", "Caracas", "Barquisimeto")
total_bultos_planta = 0
matriz_auditoria = list(zip(unidades_transporte, bultos_cargados, destinos_ruta))
print(matriz_auditoria)
for camion, bultos, ciudad in zip(unidades_transporte, bultos_cargados, destinos_ruta):
    total_bultos_planta += bultos
    if bultos >= 500:
        print(f"Despacho de alta prioridad: {camion} lleva {bultos} bultos hacia {ciudad}")
    else:
        print(f"Despacho estandar: {camion} lleva {bultos} bultos hacia {ciudad}")
codigo_control_final = (total_bultos_planta * len(matriz_auditoria) - 900)
print(f"Volumen Total Sincronizado: {total_bultos_planta} Bultos")
print(f"Código Control de Cierre:   {codigo_control_final}")


