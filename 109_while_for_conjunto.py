num = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print("Bucle for conjunto".center(50, "*"))
print()
print(f"Conjunto de numeros original: {num}{type(num)}")
print()
for i in num:
    if i == 10:
        print(i)
    else:
        print(i, end= " - ")
print("Bucle while".center(50, "*"))
print()
print(f"Conjunto de numeros original: {num}")
num = list(num)
print()
print(f"Lista original: {num}{type(num)}")
print()
elemento = 0
while elemento < len(num):
    if num[elemento] == 10:
        print(num[elemento])
        break
    else:
        print(num[elemento], end= " - ")
        elemento += 1




