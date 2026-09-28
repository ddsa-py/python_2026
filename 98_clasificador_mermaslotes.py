print(" CLASIFICACIÓN DE CONTROL DE MERMAS - PLANTA SAN JOAQUÍN ".center(65, "="))
mermas_lotes = (
    ("Lote-Maíz", 150),
    ("Lote-Arroz", 85),
    ("Lote-Soya", 210),
    ("Lote-Harina", 60)
)
print(f"Mermas originales registradas: {mermas_lotes}")
lista_mermas = list(mermas_lotes)

for i in range(len(lista_mermas)):
    for j in range(i + 1, len(lista_mermas)):
        if lista_mermas[i][1] > lista_mermas[j][1]:
            lista_mermas[i], lista_mermas[j] = lista_mermas[j], lista_mermas[i]

codigo_auditoria = (lista_mermas[0][1] * len(lista_mermas)) + 260

print(f"El lote con MENOR cantidad de merma es: {lista_mermas[0]}")
print(f"El lote con MAYOR cantidad de merma es: {lista_mermas[-1]}")
print(f"Código Control de Auditoría:            {codigo_auditoria}")