print(
    "Confeccionar una clase que represente un empleado. Definir como atributos su"
    "nombre y su sueldo.\nEn el método __init__ cargar los atributos por teclado y luego"
    "en otro método imprimir sus datos\ny por último uno que imprima un mensaje si"
    "debe pagar impuestos (si el sueldo supera a 3000)"
    "\n\n"
)

# Class Empleado
# Attributes
#   name
#   salary
#   __init__(name, salary)
#   print_empleado()
#   get_taxes()


class Empleado:
    name, salary = None, None

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print(self):
        print(f"Nombre: {self.name}\nSueldo: {self.salary}")

    def get_taxes(self):
        if self.salary > 3000:
            print("Debe pagar impuestos")


def main():
    # Pedir los datos por teclado
    print("Ingrese datos del empleado\n")
    nombre = input("Nombre: ")
    sueldo = int(input("Sueldo: "))
    print("")

    # Inicializar y cargar los datos en el objeto
    empleado = Empleado(nombre, sueldo)

    # Mostrar los datos
    empleado.print()
    empleado.get_taxes()


main()
