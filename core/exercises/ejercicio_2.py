print(
    "Confeccionar una clase que permita carga el nombre y la edad de una persona."
    "\nMostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)"
    "\n\n"
)

# Class Persona
# Attributes
#   name
#   age
#   set_name()
#   set_age()
#   print_persona()


class Persona:
    name = None
    age = None

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def print(self):
        print(f"Nombre: {self.name}\nEdad: {self.age}")

        if self.age >= 18:
            print("Es mayor de edad")


def main():
    # Pedir los datos por teclado
    print("Ingrese datos de la persona\n")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    print("")

    # Inicializar objeto
    persona = Persona()

    # Cargar los datos en el objeto
    persona.set_name(nombre)
    persona.set_age(edad)

    # Mostrar los datos
    persona.print()


main()
