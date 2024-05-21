class Cuenta:
    def __init__(self, nombre, apellido, dinero):
        self.nombre = nombre
        self.apellido = apellido
        self.dinero = dinero

    def mostrarDatos(self):
        datos = f"nombre: {self.nombre} {self.apellido}\ndinero: {self.dinero} bs"
        return datos

    def ingresarDinero(self, ingreso):
        self.dinero = ingreso + self.dinero
        print("Ha ingresado su dinero exitosamente")
    
    def retirarDinero(self, transferencia):
        if transferencia > self.dinero:
            print("No tiene suficiente dinero")
        else:
            self.dinero = self.dinero - transferencia
            print("Ha retirado su dinero exitosamente")

def opcionElegir():
        try:
            menu = "-----------Cuenta Bancaria---------\n0.Ingresar Dinero a la cuenta\n1.Retira dinero de la cuenta\n2.Mostrar Informacion\n3.Salir"
            print(menu)
            opcion = int(input("Ingresa una opcion: "))
            return opcion
        except:
            print()
            print("--Ingrese una opcion correcta--")
            print()
            print(menu)
            opcion = int(input("Ingrese una opcion: "))
            return opcion


def main():
    global opcion

    print("Vamos a crearte una cuenta Bancaria")

    nombre = str(input("Ingrese su nombre: "))
    apellido = str(input("Ingrese su nombre: "))
    dinero = int(input("Con cuanto dinero desea ingresar en su cuenta: "))


    if dinero < 0:
        print("No es posible ingresar este monto")
        opcion = opcionElegir()

    p = Cuenta(nombre , apellido , dinero)

    #Mensaje Despues de haber creado la cuenta
    print("--Su cuenta ha sido creada exitosamente--")
    opcion = opcionElegir()
        
    while opcion < 4:

        match opcion:
            case 0:
                dinero = int(input("Ingrese el monto desea ingresar: "))

                if dinero < 0:
                    print("Ingrese un monto valido")
                    opcion = opcionElegir()

                p.ingresarDinero(dinero)

                print(f"--HA INGRESADO {dinero} BS EXITOSAMENTE A SU CUENTA--")
                opcion = opcionElegir()

            case 1:
                
                dinero = int(input("Cuanto dinero desea retirar: "))

                if dinero > p.dinero:
                    print("No tiene suficiente dinero en la cuenta")
                    opcion = opcionElegir()
                p.retirarDinero(dinero)

                print(f"--SE HA RETIRADO {dinero} BS EXITOSAMENTE DE SU CUENTA--")
                opcion = opcionElegir()

            case 2:
                print("--MOSTRANDO SU INFORMACION--")
                print(p.mostrarDatos())

                opcion = opcionElegir()

            case _:
                break




main()

#Mejoras