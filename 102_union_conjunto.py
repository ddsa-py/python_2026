print(" CONSOLIDACIÓN HISTÓRICA DE FLOTAS - POLAR ".center(65, "="))
camiones_mañana = {"Camion-Alfa", "Camion-Beta", "Camion-Gamma"}
camiones_tarde = {"Camion-Gamma", "Camion-Delta", "Camion-Alfa"}
print(f"Camiones mañana: {camiones_mañana}")
print(f"Camiones tarde: {camiones_tarde}")
flota_unificada_metodo = camiones_mañana.union(camiones_tarde)
flota_unificada_pipe = camiones_tarde | camiones_mañana
print(f"Flota unificada metodo: {flota_unificada_metodo}")
print(f"Flota unificada pipe: {flota_unificada_pipe}")
codigo_auditoria = (len(flota_unificada_metodo) * len(camiones_mañana)) + 400
print(f"Código Control  : {codigo_auditoria}")
