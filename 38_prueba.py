print("Preuba".center(30,"+"))
print()
while True:
    frase = input("Ingrese una frase: ")
    frase_num = frase.count("")
    palabra = input("Ingrese la palabra que desea eliminar de la frase: ").strip()
    palabra_num = len(palabra)
    frase_encontrada= frase.find(palabra)
    
    print([:frase_encontrada] ,[palabra_num:]) 
    
    print(frase_num,frase_encontrada,palabra_num)
        
        
    
