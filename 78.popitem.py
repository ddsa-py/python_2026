lotes_criticos = {"lote-alfa": 850,
                  "lote-beta": 420,
                  "lote-gamma": 150
                  }
error_nocturno = 0
buscar_codigo = lotes_criticos.get("lotegamma", -77)

if buscar_codigo == -77:
    print(f"Lote inexistente, error: -77")
    error_nocturno += 1
    
else:
    print(f"Codigo encontrado: {buscar_codigo}")
balance_nocturno = (len(lotes_criticos) * error_nocturno) + 300
print(f"Balance nocturno: {balance_nocturno}")

