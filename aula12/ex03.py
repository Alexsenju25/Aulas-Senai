class Shape():
    def calcular_area(self):
        pass
class Circulo(Shape):
    def calcular_area(self, r):
        return ( 3.14 * r ** 2)
           

class Retangulo(Shape):
    def calcular_area(self, b, a):
        return (b * a)        

circulo = Circulo()
retangulo = Retangulo()

print(circulo.calcular_area(10))
print(retangulo.calcular_area(3,14))
        