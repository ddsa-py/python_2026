
#opcion 1
#nombre = input("Ingrese su nombre: ")
#edad = int(input("Ingrese su edad: "))
#print("hola {} su edad es: {}".format(nombre,edad))
print("")
#opcion 2
#print("Su nombre es {nombre} y su edad es {edad} ".format(nombre="Carlos",edad=40))
print("")
#opcion 3
#nombre = input("Ingrese su nombre: ")
#edad = int(input("Ingrese su edad: "))
#print("hola {0} su edad es: {1}".format(nombre,edad))
print("")
print("El Generador de Recibos de una Tienda de Deportes")

while True:
    articulo = input("Ingrese el nombre del articulo: ").strip()
    if articulo == "apagar":
        print("Cerrando caja registradora...")
        break
    precio = input("Ingrese el costo del articulo: ")
    if not precio.isdigit():
        print("¡Error!: El precio debe ser un número entero.")
        continue
    precio = int(precio)
    print("Opcion 1: ", end=" ")
    print("Artículo: {} - Precio: ${}".format(articulo,precio))
    print("Opcion 2: ", end=" ")
    print("Artículo: {art} - Precio: ${costo}".format(art=articulo,costo=precio))
    print("Opcion 3: ", end=" ")
    print("Artículo: {0} - Precio: ${1}".format(articulo,precio))
    print("Recibo con exito")
    break
    
    
               
