print(
    "Desarrollar una clase que represente un punto en el plano y tenga los siguientes"
    "\nmétodos: inicializar los valores de x e y que llegan como parámetros, imprimir en"
    "\nque cuadrante se encuentra dicho punto (concepto matemático, primer cuadrante"
    "\nsi x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)"
    "\n\n"
)

# Class Coordinate
# Attributes
#   x
#   y
#   __init__(x, y)
#   get_quadrant()


class Coordenada:
    X = 0
    y = 0

    is_quadrant_1 = lambda self: self.x > 0 and self.y > 0
    is_quadrant_2 = lambda self: self.x < 0 and self.y > 0
    is_quadrant_2 = lambda self: self.x < 0 and self.y < 0
    is_quadrant_2 = lambda self: self.x > 0 and self.y < 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_quadrant(self):
        if self.is_quadrant_1:
            return "Cuadrante 1"
        elif self.is_quadrant_2:
            return "Cuadrante 2"
        elif self.is_quadrant_3:
            return "Cuadrante 3"
        elif self.is_quadrant_4:
            return "Cuadrante 4"


def main():
    try:
        # Pedir los datos por teclado
        print("Ingrese las coordenadas\n")
        x = int(input("X: "))
        y = int(input("Y: "))
        print("")

        # Inicializar y cargar los datos en el objeto
        punto = Coordenada(x, y)

        # Mostrar los datos
        cuadrante = punto.get_quadrant()
        print(f"El cuadrante de la coordenada es: {cuadrante}")
    except ValueError:
        print("Dato invalido.")


main()
