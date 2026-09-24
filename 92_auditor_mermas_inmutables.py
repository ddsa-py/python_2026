print(" BALANCE GENERAL DE CONTROL DE MERMAS - POLAR ".center(65, "="))
mermas_producción = {
    "Lote-Harina": 85,
    "Lote-Aceite": 40,
    "Lote-Arroz": 120,
    "Lote-Margarina": 35
}
total_mermas = 0
lista_mermas = list(mermas_producción.items())
print(f"{lista_mermas[0]}\n{lista_mermas[1]}\n{lista_mermas[2]}")
print()
mermas_producción_tuplas = tuple(mermas_producción.items())
for lote, kilos in mermas_producción_tuplas:
    total_mermas += kilos
    if kilos >= 50:
        print(f"Critico {lote} supera el umbral con {kilos} kg")
    else:
        print(f"tolerable {lote} bajo control con {kilos} kg")
balance_auditoria = (total_mermas * len(mermas_producción)) - 400

print(f"Total Kilos Desincorporados: {total_mermas} kg")
print(f"Código Balance Final:        {balance_auditoria}")
