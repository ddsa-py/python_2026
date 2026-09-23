print("El Control de Calidad de la Fábrica".center(41,"*"))
print("\n")
produccion = [500, 495, 500, 505, 500, 480, 500, 510]
contador=0
defectuosas=0

for i in produccion:
    if i == 500:
        contador+=1
    else:
        defectuosas+=1
print(f"La produccion perfecta fue de: {contador} y las defectuosas fueron: {defectuosas}")

print("Clase range")
print()
numero= range(10)
print("numero= range(10)")
print(numero)

for i in range(10):
    print(i,end=",")
print()
for i in range(2,11):
    print(i,end=" ")
print()

for i in range(1,11,3):
    print(i,end=",")
print()
for i in range(3,19,3):
    print(i,end=" ")
print()
for i in range(10,0,-1):
    print(i,end=" ")







