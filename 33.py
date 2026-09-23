string = "la CasA es BonitA"
print(f"Antes de capitalize(): {string}")
string = string.capitalize()
print(f"Despues de capitalize(): {string}")
print("El Sistema de Redacción de un Periódico Digital\n")
print("*******************************")
while True:
    titulares = input("Ingrese el titular de noticias: ").strip()
    #if titulares == "apagar" or titulares == "Apagar":
     #   print("Cerrando el sistema de titulares...")
      #  break
    #if not titulares.isdigit():
     #   print("Error... Solo acepta  letras, vuelve a intentar...")
      #  continue
    titular_limpio = titulares.capitalize()
    #else:
    print(f"El titular aceptado es: {titular_limpio}")
     #   break
    
        
