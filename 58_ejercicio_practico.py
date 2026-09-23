print("Ejercicio practico".center(60,"*"))
print()
num = int(input("¿Cuantos numeros enteros contendra la lista?: "))
lista = []


for i in range(1,num+1):
    num_= int(input(f"Introduce el #{i} numero entero: "))
    lista.append(num_)
    total =sum(lista)
print(f"Lista: {lista} suma total de la lista: {total}")
print()
print(" AUDITORÍA FLUX CONTROL CERVECERÍA POLAR ".center(60, "#"))
lista_polar = [10, 20, 30, 40]

polar_apertura = lista_polar[:]
suma_total = sum(lista_polar)
lista_polar.extend(range(50,80,10))
variable =  suma_total - len(lista_polar)
lista_polar[-1] *= variable
print(f"1. Polar Apertura:        {polar_apertura}")
print(f"2. Suma Total Inicial:    {suma_total}")
print(f"3. Lista Polar Final RAM: {lista_polar}")
    
    
    
