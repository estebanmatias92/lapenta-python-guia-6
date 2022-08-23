print(
    "Desarrollar un programa que cargue los lados de un triángulo e implemente los"
    "\nsiguientes métodos: inicializar los atributos, imprimir el valor del lado mayor y otro"
    "\nmétodo que muestre si es equilátero o no. El nombre de la clase llamarla"
    " Triangulo."
)

# Class Triangulo
# Attributes
#   a
#   b
#   c
#   set_sides(a, b, c)
#   get_biggest_side()
#   get_type()


class Triangulo:
    a, b, c = None, None, None

    def set_sides(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_biggest_side(self):
        return max([self.a, self.b, self.c])

    def get_type(self):
        if self.a == self.b == self.c:
            return "Equilatero"
        elif self.a != self.b != self.c:
            return "Escaleno"
        else:
            return "Isosceles"


def main():
    # Pedir los datos por teclado
    print("Ingresar el largo de los lado del triangulo en centimetros\n")
    lado_a = int(input("Largo de Lado A: "))
    lado_b = int(input("Largo de Lado B: "))
    lado_c = int(input("Largo de Lado C: "))
    print("")

    # Inicializar objeto
    triangulo = Triangulo()

    # Cargar los datos en el objeto
    triangulo.set_sides(lado_a, lado_b, lado_c)

    # Mostrar los datos
    largo_mayor = triangulo.get_biggest_side()
    print(f"El lado mayor mide {largo_mayor} CMs")

    tipo_triangulo = triangulo.get_type()
    print(f"El tipo de triangulo es: {tipo_triangulo}")


main()
