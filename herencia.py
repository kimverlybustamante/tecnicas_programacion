# Clase base
class Figura:
    def area(self):
        return 0

# Clases hijas
class Cuadrado(Figura):
    def _init_(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

class Rectangulo(Figura):
    def _init_(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

# Uso de la herencia
fig1 = Cuadrado(4)
fig2 = Rectangulo(3, 6)

print(f"Área del cuadrado: {fig1.area()}")
print(f"Área del rectángulo: {fig2.area()}")