print("El Filtro de Auditoría de Cuentas Bancarias".center(61,("*")))
print()
contador = ""
for i in range(10,36,5):
    if i == 25:
        continue
    contador =contador + str(i) + "-"
print(contador.rstrip("-"))
