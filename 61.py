print(" AUDITORÍA SECUENCIAL DE TOLVAS - ALIMENTOS POLAR ".center(60, "#"))
reporte_tolvas = ["  T-Alfa  ", "T-Beta", "  T-Alfa  ", "T-Gamma", "  t-alfa  "]
pos = 0
tolvas_apertura = reporte_tolvas[:]

for i in reporte_tolvas[:]:
    variable = i.strip().upper()
    reporte_tolvas[pos] = variable
    pos += 1
    if  i == "T-BETA":
        continue

auditoria_tolvas = reporte_tolvas.count("T-ALFA") * (len(reporte_tolvas[0]) + len(tolvas_apertura))

print(f"1. Tolvas Apertura:       {tolvas_apertura}")
print(f"2. Reporte Final Neto:    {auditoria_tolvas}")
print(f"3. Lista Tolvas Final RAM: {reporte_tolvas}")
