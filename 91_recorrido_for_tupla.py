print(" REPORTE INDUSTRIAL DE INVENTARIO - SILOS POLAR ".center(65, "="))
monitoreo_silos = (
    ("Silo-A", 450, "Maíz Amarillo"),
    ("Silo-B", 600, "Arroz en Grano"),
    ("Silo-C", 350, "Harina de Soya")
)
tonelaje_acumulado: int  = 0
for nombre_silo, capacidad,  material in monitoreo_silos:
    tonelaje_acumulado += int(capacidad)
    print(f"El {nombre_silo} contiene: {capacidad} toneladas de: {material}")
indicador_eficiencia = (tonelaje_acumulado * len(monitoreo_silos)) - 400
print(f"El indicador de Eficiencia es: {indicador_eficiencia}")

