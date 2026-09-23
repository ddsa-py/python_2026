import os
while True:
    num= input("Ingrese el tiempo de apagado en minutos: ")
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Error, solo se permiten numeros, intente de nuevo")
        print()


segundos = num * 60

os.system(f"shutdown -s -t {segundos}")
print(f"🖥️Sistema programado para apagarse en {num} hora(s) ({segundos} segundos)")

    
