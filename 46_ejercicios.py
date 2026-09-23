

camiones = ["Camion_A", "Camion_B", "Camion_C", "Camion_D", "Camion_E"]
#print(f"Lista de camiones original: {camiones}")
camiones[1] = "MANTENIMIENTO"
reporte_manana = camiones[:]

camiones[2:4] = ["Gandola_1", "Gandola_2", "Gandola_3"]
reporte_tarde = camiones[:]
print(f"Reporte mañana: {reporte_manana}")
print(f"Reporte Tarde: {reporte_tarde}")
print(f"Lista de camiones: {camiones}")

print()
print("** El Historial de Aviones en Pista **")
print()
pista = ["Avion_1", "Avion_2", "Avion_3", "Avion_4"]

pista[0]= "DESPEGADO"
reporte_manana = pista[:]
pista[1:3] = "Carga_A", "Carga_B", "Carga_C"

reporte_tarde = pista[:]
print(f"Reporte Mañana Blindado: {reporte_manana}")
print(f"Reporte Tarde Blindado: {reporte_tarde}")
print(f"Lista Final Viva en RAM: {pista}")


print()
print("Banca de Inversiones de Valencia (Carabobo).")
print()

tasas = [5.5, 8.2, 12.0, 4.1]
tasas[1] *=  1.5

portafolio_manana = tasas[:]
tasas[1:3] = [3.0, 2.5, 1.8]
portafolio_tarde = tasas[:]
print(f"Historial Mañana Blindado: {portafolio_manana}")
print(f"Historial Tarde Blindado: {portafolio_tarde}")
print(f"Lista Financiera Viva actual: {tasas}")






























