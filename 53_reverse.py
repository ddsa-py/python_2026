lote_pesado = [50, 100, 150]
lote_ligero = ["X", "Y", "Z"]
ligero_pasado = lote_ligero[:]
resultado = lote_pesado[-1] * len(lote_ligero)
lote_pesado[0] = resultado
lote_ligero.reverse()
elemento_retirado = lote_ligero.pop(2)
print(f"1. Pasado Blindado: {ligero_pasado}")
print(f"2. Elemento Sacado: {elemento_retirado}")
print(f"3. Lista Pesada:    {lote_pesado}")
print(f"4. Lista Ligera:    {lote_ligero}")
