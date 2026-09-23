print(" AUDITORÍA MATRICIAL DE ALTO BLINDAJE - CERVECERÍA POLAR ".center(60, "#"))
import copy
calderas_polar = [[100, 150, 200],
                  [210, 220, 230],
                  [300, 310, 320]]

calderas_apertura = copy.deepcopy(calderas_polar)


presion_alta = calderas_polar[2][1]
presion_baja = calderas_polar[0][1]

calderas_polar[1][1] *= (presion_alta - presion_baja)

print(f"1. Calderas Apertura RAM:  {calderas_apertura}")
print(f"2. Presión Alta Extraída:  {presion_alta}")
print(f"3. Presión Baja Extraída:  {presion_baja}")
rejilla_final = f"{calderas_polar[0]}\n{calderas_polar[1]}\n{calderas_polar[2]}"
print(f"4. Calderas Final RAM:\n{rejilla_final}")





