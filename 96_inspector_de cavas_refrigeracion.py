print(" REPORTE TÉCNICO DE CADENA DE FRÍO - POLAR ".center(65, "="))
cavas_refrigeracion = ("Cava-Margarina", "Cava-Quesos", "Cava-Yogurt", "Cava-Jugos")
print(f"Sistemas de refrigeración activos: {cavas_refrigeracion}")
while True:
    num = int(input(f"Ingrese el indice o numero de la cava a auditar de 0 al {len(cavas_refrigeracion) - 1}: "))
    if num in range(len(cavas_refrigeracion)):
        print(f"monitoreo completado: nombre la cava {cavas_refrigeracion[num]}")
        break
    else:
        print("Indice de la cava auditar inexistente, vuelva a intentarlo")
codigo_temperatura = (num * len(cavas_refrigeracion)) + 500

print(f"Código Verificación de Cierre: {codigo_temperatura}")


