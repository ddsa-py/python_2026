print(" AUDITORÍA DE SEGURIDAD INMUTABLE DE TUPLAS - POLAR ".center(60, "#"))

alerta_seguridad = 0
while True:
    toneladas = input("Ingrese cantidad de toneladas: ").strip()
    if toneladas.isdigit():
        toneladas = int(toneladas)
        print()
        break
    else:
        print("Error solo numeros enteros, repita el proceso")

registro_inmutable  = ("trigo polar", toneladas, 14.5,  True)

if type(registro_inmutable) == tuple:
    alerta_seguridad  = 100
    print(f"EL registro inmutable es: {type(registro_inmutable)}")
else:
    alerta_seguridad = 0
balance_tuplas = (len(registro_inmutable) * toneladas) + alerta_seguridad

print(f"1. Renglón Control Final: {balance_tuplas}")
print(f"2. Alerta de Inmutabilidad: {alerta_seguridad}")
print(f"3. Tupla Congelada RAM:    {registro_inmutable}")

