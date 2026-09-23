import copy
# Mini-matriz con letras minúsculas en la RAM
letras = [["a", "b"], 
          ["c", "d"]]

f = 0 
for fila in letras:
    
    c = 0  
    for caracter in fila:
        
        
        letras[f][c] = letras[f][c].upper()
        
        c += 1 
    f += 1  
    rejillas = (f"{letras[0]}\n{letras[1]}")
    
print(rejillas)
print()
import copy
lotes_polar = [["pan-a", "pan-b"], 
               ["pan-c", "pan-d"]]
lotes_apertura = copy.deepcopy(lotes_polar)

f=0
for fila in lotes_polar:
   c=0
   for columna in fila:
       lotes_polar[f][c] = lotes_polar[f][c].upper()
       c+=1
   f+=1
rejilla= f"{lotes_polar[0]}\n{lotes_polar[1]}"

print(rejilla)
print()
print(f"{lotes_apertura[0]}\n{lotes_polar[1]}")
