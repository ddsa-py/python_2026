print(" AUDITORÍA INTERACTIVA ALIMENTOS POLAR ".center(60, "#"))
print("Simulación de Interfaz y Control de Extremos")
print()

pesos_muelle= []
num = 3

for i in range(1,num+1):
    valor = int(input(f"Introduce tu #{i} valor o numero: "))
    pesos_muelle.append(valor)
foto_apertura = pesos_muelle[:]
peso_total = sum(pesos_muelle)

pesos_muelle[0] *= (peso_total - len(pesos_muelle))
print(f"1. Foto Apertura Muelle:   {foto_apertura}")
print(f"2. Peso Total Acumulado:   {peso_total}")
print(f"3. Lista Pesos Final RAM:  {pesos_muelle}")
