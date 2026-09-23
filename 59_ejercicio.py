print(" AUDITORÍA DE CONTEO AVANZADO ALIMENTOS POLAR ".center(60, "#"))
registro_fallas = ["F-Sellado", "F-Peso", "F-Sellado", "F-Corte", "F-Sellado"]
registro_apertura = registro_fallas[:]
total_sellado = registro_fallas.count("F-Sellado")

reporte_matematico = len(registro_fallas[-1]) + (len(registro_fallas[0]) * total_sellado)


print(f"1. Registro Apertura:    {registro_apertura}")
print(f"2. Total Fallas Sellado: {total_sellado}")
print(f"3. Reporte Final Neto:   {reporte_matematico}")
