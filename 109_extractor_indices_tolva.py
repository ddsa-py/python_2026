tolvas_activas = {"T-1", "T-2", "T-3"}
print()
print(f"Tolvas activas: {tolvas_activas}")
lista_tolvas = list(tolvas_activas)
print()
print(f"lista tolvas: {lista_tolvas}{type(lista_tolvas)}")
elemento = 0
while elemento < len(lista_tolvas):
    print(lista_tolvas[elemento], end=" ")
    elemento += 1
print()
balance_mecanico = (len(lista_tolvas) * 150) + 50
print()
print(f"Balance mecanico: {balance_mecanico}")
print("Ciclo for".center(50, "*"))
tolvas_activas1 = list(tolvas_activas)
for tole in (tolvas_activas1):
    if tole == "T-3":
        print(tole)
        break
    else:
        print(tole, end=" - ")