print(" SISTEMA DE DETECCIÓN DE MERMAS INDUSTRIALES - POLAR ".center(65, "="))
lotes_produccion = (101, 202, 303, 202, 404, 505, 202)
print(f"Lotes en patio: {lotes_produccion}")

lote_defecto = int(input("Ingrese el codigo numerico del lote defectuoso para retirar: "))
lista_patio = list(lotes_produccion)
for posicion in range(len(lista_patio)):
    if lista_patio[posicion] == lote_defecto:
         lista_patio[posicion] = 999
print(lista_patio)

codigo_auditoria = (lista_patio.count(999) * len(lista_patio)) + 450

tupla_final = tuple(lista_patio)
print(f"Tupla de Producción Finalizada: {tupla_final}")
print(f"Código Control de Auditoría:    {codigo_auditoria}")


