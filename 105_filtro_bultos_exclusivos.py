print(" AUDITORÍA DE EMBARQUES EXCLUSIVOS - ALIMENTOS POLAR ".center(65, "="))
gandola_mañana = {"Harina", "Margarina", "Sal", "Azúcar"}
gandola_tarde = {"Sal", "Azúcar", "Levadura", "Manteca"}
print(f"Gandola de la mañana: {gandola_mañana}")
print(f"Gandola de la tarde: {gandola_tarde}")
bultos_unicos = gandola_mañana ^ gandola_tarde
print(f"Bultos unicos: {bultos_unicos}")
codigo_verificacion = (len(bultos_unicos) * len(gandola_tarde)) + 100
print(f"Codigo verificacion: {codigo_verificacion}")

