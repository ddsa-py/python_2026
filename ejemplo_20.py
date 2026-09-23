num= input("Ingrese un numero: ").strip()

if num.isdigit():
    num=int
    num+=10
    print(num)
else:
    print("Valor incorrecto")
    
