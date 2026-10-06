print(" AUDITORÍA COMPACTA DE TOLVAS DE MATERIA PRIMA - POLAR ".center(65, "="))
mermas_crudas = [10, 15, 20, 25, 30, 35, 40]
print()
print(f"Lista mermas crudas: {mermas_crudas}")
reporte_purificado = [i * 10  for i in mermas_crudas if i >= 25 ]
print(reporte_purificado)
codigo_planta = (len(reporte_purificado) * 100) + 50
print(codigo_planta)
print("***************************************")
mermas_crudas1 = [10, 15, 20, 25, 30, 35, 40]
print(f"Lista mermas crudas: {mermas_crudas1}")
lista_merma1 = [i * 10 if i >= 25 else i for i in mermas_crudas1]
print(lista_merma1)
num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(type(num))
tupla_num = {i * 5 if i > 0 else i for i in num}
print(tupla_num)