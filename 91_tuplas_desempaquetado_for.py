frutas = (("001", "manzana", "roja"),
          ("002", "pera", "verde"),
          ("003", "naranja", "naranja")
          )
print(f"{frutas[0]}\n{frutas[1]}\n{frutas[2]}")

for codigo, fruta, color in frutas:
    print(f"El codigo: {codigo} - {fruta} es de color {color}")

