print("Aeropuerto Internacional Arturo Michelena de Valencia".center(60,"/"))
print()
pista_vuelo = ["Avion_Alfa", "Avion_Bravo", "Avion_Coca", "Avion_Delta"]
reporte_manana = pista_vuelo[:]

pista_vuelo.insert(2,"AMBULANCIA_AEREA")
reporte_emerg = pista_vuelo[:]
pista_vuelo.insert(-1,"FUERZA_AEREA_1")
reporte_final = pista_vuelo[:]
pista_vuelo.insert(-2,"antepenultimo")
reporte_antepen = pista_vuelo[:]
print(f"Reporte mañana: {reporte_manana}")
print(f"Reporte tarde: {reporte_emerg}")
print(f"Reporte final: {reporte_final}")
print(f"Reporte final: {reporte_antepen}")

