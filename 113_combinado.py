import math as m
import random as rd
print(" AUDITORÍA COMBINADA DE RESISTENCIA INDUSTRIAL - POLAR ".center(65, "="))
esfuerzo_bruto = rd.randint(10, 30)
resistencia_flujo = m.sqrt(esfuerzo_bruto ** 3)
codigo_control = (int(resistencia_flujo) * 10) + 100
print(f"Esfuerzo base generado:    {esfuerzo_bruto}")
print(f"Resistencia de flujo real: {resistencia_flujo}")
print(f"Código Control de Planta:  {codigo_control}")