print(" AUDITORÍA SIMULTÁNEA CERVECERÍA POLAR ".center(60, "#"))
registro_botellas = ["P-1", "p-1", "P-2", "P-1", "p-1", "P-3"]
botellas_apertura = registro_botellas[:]
contar = registro_botellas.count("P-1") + registro_botellas.count("p-1")

for _ in registro_botellas[:]:
    if "p-1".lower() in registro_botellas[:]:
        registro_botellas.remove("p-1".lower())
    if "P-1".upper() in registro_botellas[:]:
        registro_botellas.remove("p-1".upper())
auditoria_total = len(registro_botellas) + len(botellas_apertura)


print(f"1. Botellas Apertura:     {botellas_apertura}")
print(f"2. Reporte Final Neto:    {auditoria_total}")
print(f"3. Lista Botellas Final:  {registro_botellas}")
print(f"3. Total a eliminar:  {contar}")
