print("Refinería de Combustible El Palito (Puerto Cabello)".center(60,"*"))
print()
tanques = ["Super", "Premium", "Regular", "Diesel"]
historial_apertura = tanques[:]
tanques[2] += "-95_Octanos"
historial_mod = tanques[:]
tanques.insert(1,"ULTRA_VIP")
historial_tarde = tanques[:]
tanque_despachado = tanques.pop()

emergencia_atendida = tanques.pop(1)
#emergencia_atendida = tanques[:]

print(f"1. Estado de Apertura:     {historial_apertura}")
print(f"2. Estado de Apertura:     {historial_mod}")
print(f"3. Estado del Turno Tarde: {historial_tarde}")
print(f"4. Tanque Despachado:      {tanque_despachado}")
print(f"5. Emergencia Atendida:    {emergencia_atendida}")
print(f"6. Fila Viva Actual RAM:   {tanques}")
