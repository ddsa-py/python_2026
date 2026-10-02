guias_despacho = {"G-01", "G-02", "G-03", "G-04", "G-05"}
print(f"Guias despachos: {guias_despacho}")
guias_despacho.remove("G-01")
print(f"Guias despachos actualizada (remove 'g-01'): {guias_despacho}")
guias_despacho.discard("G-99")
print(f"Guias despachos (discard 'G-99'): {guias_despacho}")
guia_auditar = "G-05"
if guia_auditar in guias_despacho:
    guias_despacho.remove(guia_auditar)
    print(f"Guias despachos: {guias_despacho}")
else:
    print(f"Guia no existe {guia_auditar}")
balance_guias = (len(guias_despacho) * 300) + 25
print(f"Balance: {balance_guias}")


