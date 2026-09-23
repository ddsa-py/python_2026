print("ejercicio 84")
#1 ejercicio
print()
contador_num = 0
texto = input("Ingrese texto: ")
dictionary = dict.fromkeys(texto, 0)
print()
for i in dictionary:
    contador = texto.count(i)
    dictionary[i] = contador
    #dictionary.setdefault(i, contador)
        
print(dictionary)
print()
#metodo dos
string = input("Ingrese texto: ")

letters = dict.fromkeys(string, 0)
for letter in string:
    letters[letter] += 1
print(letters)
    





