numeros = [10, 30, 40]
print(numeros)

numeros.insert(1,20)
print(numeros)
con_20 = numeros[:]
numeros.insert(-1,45)
con_1 = numeros[:]
print(f"Se realiza la insercion con insert(1,20):{con_20}")
print(f"Se realiza la insercion con insert(-1,45):{con_1}")
#por que si le coloque -1 no se coloco al final
print()

camiones = ["Furgon_A", "Plataforma_B", "Gandola_C"]
reporte_inicial = camiones[:]
camiones.insert(1,"Cisterna_VIP")
reporte_intermedio = camiones[:]
camiones.insert(0,999)
print(f"Reporte Inicial:     {reporte_inicial}")
print(f"Reporte Intermedio:  {reporte_intermedio}")
print(f"Lista de Salida Viva: {camiones}")

print()
print("***Metodo insert()***")
print()
letras =["b","d","f","g","h"]
lista_original = letras[:]
letras.insert(0,"a")
lista_a = letras[:]
letras.insert(2,"c")
lista_c = letras[:]
letras.insert(4,"e")
lista_e = letras[:]
letras.insert(100,"z")
lista_z = letras[:]

print(f"lista original: {lista_original}")
print(f"lista con a posicion 0: {lista_a}")
print(f"lista con c posicion 2: {lista_c}")
print(f"lista con e posicion 4: {lista_e}")
print(f"lista con z posicion 100: {lista_z}")



































