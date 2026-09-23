print(" Aduana Marítima de Puerto Cabello".center(60,"*"))
print()
codigos = ["A1", "B2", "C3", "D4", "E5", "F6"]

print(f"\ncodigos[2]: {codigos[2]}")
print(f"\ncodigos[-2]: {codigos[-2]}")


print(f"\ncodigos[2:5]: {codigos[2:5]}")

print(f"\ncodigos[len(codigos)-1]: {codigos[len(codigos)-1]}")

print("*****************************************************")
print()
vagones = ["V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8"]

print(f"\nvagones[:3] Delanteros: {vagones[:3]}")

print(f"\nvagones[3:7] centrales: {vagones[3:7]}")

print(f"\nvagones[::2] Impares: {vagones[::2]}")
print("***************************************")


texto = "la casa de pony"
print(texto[::2])
texto = "la", "casa", "de", "pony"
print(texto[::2])
texto = ["la", "casa", "de", "pony"]
print(texto[::2])

