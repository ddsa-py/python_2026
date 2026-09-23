print("Cervecería Polar (Planta San Joaquín, Carabobo)".center(60,"*"))
print()
carga = ["Camion_A", "Camion_B", "Camion_C"]
reporte_manana = carga[:]
carga.append("Gandola_X")
reporte_tarde = carga[:]
carga.append(45.8)
print(f"Reporte Mañana Blindado: {reporte_manana}")
print(f"Reporte Tarde Blindado: {reporte_tarde}")
print(f"Lista de Carga Final Viva: {carga}")
print()
print("**El Clasificador de Envíos Prioritarios**")
print()
paquetes = ["P1", "P2", "P3", "P4", "P5", "P6"]
historial_inicial = paquetes[:]
lote_express = paquetes[2:5]
paquetes.append("INTER-99")
historial_actualizado = paquetes[:]
paquetes.append(12.4)
print(f"Historial Inicial Blindado: {historial_inicial}")
print(f"Lote Express Aislado: {lote_express}")
print(f"Historial Actualizado Tarde: {historial_actualizado}")
print(f"Lista de Paquetes Final Viva: {paquetes}")
