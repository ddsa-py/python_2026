niveles_silos = [80, 45, 120, 30, 95]
print("Niveles de los silos:", niveles_silos)
matriz_base = list(enumerate(niveles_silos, start=1))
print("Matriz base:", matriz_base)
for pos, carga in matriz_base:
    if carga < 50:
        print(f"El silo {pos} está en nivel crítico: {carga}")

    else:
        print(f"El silo {pos} está en nivel aceptable: {carga}")
print("***************************************")

reporte_final = ["ALERTA" if carga < 50 else 999 for pos, carga in matriz_base]  
print(reporte_final)
codigo_planta = (len(reporte_final) * reporte_final.count("ALERTA")) + 800
print(codigo_planta)