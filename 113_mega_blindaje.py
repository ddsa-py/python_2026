import math as m
presiones_base = [120, 0, 150, -80, 200]
print(f"Lista original Presiones base: {presiones_base}")
try:
    reporte_inyectores = [int(m.sqrt(presion))if presion > 0 else 555 for pos, presion in list(enumerate(presiones_base, start=1))]
except Exception as e:
    print(f"Error: {e}")
codigo_planta = (len(reporte_inyectores) * reporte_inyectores.count(555)) + len("Daniel")
print(f"Codigo de planta: {codigo_planta}")
