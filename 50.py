vocales = ["a","e","i","o","u"]
v_inicial = vocales[:]
print(f"Elemento eliminado vocales.pop():{vocales.pop()}")

v_a = vocales[:]
print(f"Elemento eliminado vocales.pop(2):{vocales.pop(2)}")
v_2 = vocales[:]
print(f"Elemento eliminado vocales.pop(0):{vocales.pop(0)}")
v_0 = vocales[:]
print(f"Elemento eliminado vocales.pop(-2):{vocales.pop(-2)}")
v_2_2 = vocales[:]

print(f"vocales original: {v_inicial}")
print(f"Elemento eliminado:{v_a}")
print(f"Elemento eliminado:{v_2}")
print(f"Elemento eliminado:{v_0}")
print(f"Elemento eliminado:{v_2_2}")
#error
#print(f"Elemento eliminado 5: {vocales.pop(5)}")

iva = 1.16

precio_final = 500 * iva
print(precio_final)
usuario = "Dani_Pro"
clave_correcta = True
intento_clave = False

if usuario == "Dani_Pro" or intento_clave == clave_correcta:
    print("Acceso Concedido")
else:
    print("ALERTA: Acceso Denegado")

datos = [10, "Valencia", 30.5]
datos[1] = datos[0] + datos[2]
print(datos)
flota = ["Furgon_1", "Gandola_2", "Cisterna_3"]
flota.append("Camioneta_4")
print(flota)

original = ["A", "B", "C"]
reporte_A = original
reporte_B = original[:]
original.pop()

print(reporte_A)
print(reporte_B)
print(original)


datos = [10, "Valencia", 30.5]
datos[1] = datos[0] + datos[2]
print(datos)




























    
