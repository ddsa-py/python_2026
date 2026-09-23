print("Automotores Ford en Valencia".center(60,"*"))
print()
chasis = ["Chasis_1", "Chasis_2", "Chasis_3", "Chasis_4"]
estado_inicial = chasis[:]
chasis.insert(0,"Mustang_VIP")
estado_primero = chasis[:]
chasis.insert(3,"Camioneta_F150")
estado_intermedio = chasis[:]
chasis.insert(200,9999)
print(f"1. Inicial Blindado: {estado_inicial}")
print(f"2. Primero Blindado: {estado_primero}")
print(f"3. Intermedio Blindado: {estado_intermedio}")
print(f"4. Línea Final Viva RAM: {chasis}")






