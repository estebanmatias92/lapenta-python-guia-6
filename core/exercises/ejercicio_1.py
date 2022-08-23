print(
    "Implementar una clase llamada Alumno que tenga como atributos su nombre y su"
    " nota.\nDefinir los métodos para inicializar sus atributos, imprimirlos y mostrar un"
    " mensaje si está regular (nota mayor o igual a 4)"
    "\n\n"
)

# Class Alumno
# Attributes
#   name
#   score
#   set_name()
#   set_score()
#   print_alumno()


class Alumno:
    name = None
    score = None

    def set_name(self, name):
        self.name = name

    def set_score(self, score):
        self.score = score

    def print(self):
        print(f"Nombre: {self.name}\nNota: {self.score}")

        if self.score >= 4:
            print("El alumno esta regular")


def main():
    # Pedir los datos por teclado
    print("Ingrese datos del alumno\n")
    nombre = input("Nombre: ")
    nota = int(input("Nota: "))
    print("")

    # Inicializar objeto
    alumno = Alumno()

    # Cargar los datos en el objeto
    alumno.set_name(nombre)
    alumno.set_score(nota)

    # Mostrar los datos
    alumno.print()


main()
