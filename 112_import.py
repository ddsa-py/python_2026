from math import sqrt, pi
radio_silo = 6
volumen_base = 500


altura_calculada = volumen_base / (pi * (radio_silo ** 2)) 
raiz_dimension = sqrt(altura_calculada)
print("La altura calculada del silo es:", altura_calculada)
print("La raíz cuadrada de la altura calculada es:", raiz_dimension)
codigo_auditoria = int(raiz_dimension * 100) + 600
print("El código de auditoría generado es:", codigo_auditoria)
