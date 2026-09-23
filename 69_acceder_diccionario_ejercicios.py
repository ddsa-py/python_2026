import copy 
lote_san_joaquin = {"Codigo": "PL-40",
                    "datos_producción": {"maquina": "A1", "operarios": ["Pedro", "Luis"]
                        }
                    }
                    

nombre_extraido = lote_san_joaquin["datos_producción"]["operarios"][1]
resultado_auditoria = len(nombre_extraido) * 150

print(" REPORTE DE EXTRACCIÓN TRIDIMENSIONAL - POLAR ".center(60, "#"))
print(f"1. Renglón Control Final: {resultado_auditoria}")
print(f"2. Operario Detectado:   {nombre_extraido}")

import copy

# Tu punto de partida en la memoria:
gandola_despacho = {"id_gandola": "GN-100",
                    "logistica": {"ruta": "Troncal 1", "lotes_carga": [350, 420, 180]
                        }
                    }
lote_detectado = gandola_despacho["logistica"]["lotes_carga"][1]
resultado_auditoria = (lote_detectado + len(gandola_despacho["id_gandola"])) * 2

print(" REPORTE LOGÍSTICO DE CARGA DE SALIDA - POLAR ".center(60, "#"))
print(f"1. Renglón Control Final: {resultado_auditoria}")
print(f"2. Carga Crítica Leída:   {lote_detectado}")
print(f"{gandola_despacho['id_gandola']}")

silo_polar = {"planta": "San Joaquin",
              "monitoreo": {"tipo_grano": "Maiz Blanco", "capacidad_ton": [150, 380, 240]
                 }
              }
toneladas_disponibles = silo_polar["monitoreo"]["capacidad_ton"][2]
resultado_auditoria = (toneladas_disponibles + len(silo_polar["planta"])) * 3

print(" REPORTE ANALÍTICO DE SILOS - POLAR ".center(60, "#"))
print(f"1. Renglón Control Final: {resultado_auditoria}")
print(f"2. Toneladas Extraídas:   {toneladas_disponibles}")














