print(" ****** BIENVENIDO A BURGER KING ********")
print("Ingrese los datos para la factura electrónica")
nCliente=input("Ingrese su nombre: ")
nCedula=int(input("Ingrese su número de cédula: "))
correo=input("Ingrese su correo: ")
numHamburguesas=int(input("Ingrese el número de hamburguesas a adquirir:"))

print("Ingrese uno de los siguientes tipos de hamburguesas: ")
print("1) sencilla")
print("2) doble")
print("3) triple")
tipoHamburguesa=int(input("Ingrese la opción: "))
match (tipoHamburguesa):
    case 1:
        precio = numHamburguesas*1.50 
    case 2:
        precio = numHamburguesas * 2.50
    case 3:
        precio = numHamburguesas * 3.25
    case _:
        print("No existe ese tipo de hamburguesa")

print("Ingrese su forma de pago")
print("1) Tajeta de crédito")
print("2) Efectivo")
tipoPago = int(input("Ingrese la opción: "))
match (tipoPago):
    case 1:
        recargo = precio * 0.05
        pf = precio + recargo
        print(f"Genial, {nCliente} el precio final a pagar es ${round(pf,2)}")
        print(f"La factura se enviará a su correo {correo}")
    case 2:
        print(f"Genial, {nCliente} el precio final a pagar es ${round(precio,2)}")
        print(f"La factura se enviará a su correo {correo}")
    case _:
        print("No existe la forma de pago seleccionada")
