import copy
silos_polar = [["S-10", "S-Alfa", "S-20"],
               ["S-Beta", "S-30", "S-Gamma"],
               ["S-40", "S-50", "S-Delta"]]

silos_apertura = copy.deepcopy(silos_polar)


f=0
for fila in silos_polar:
    c=0
    for columna in fila:
        if "S-" in silos_polar[f][c]:
            num= len(silos_polar[f][c])
            if num >=5:
                silos_polar[f][c] *= (num - len(silos_polar[0][0]) )
        c+=1
    f+=1
rejilla = f"{silos_polar[0]}\n{silos_polar[1]}\n{silos_polar[2]}"
print(rejilla)
print()
print(f"{silos_apertura[0]}\n{silos_apertura[1]}\n{silos_apertura[2]}")
            
            
            
            
