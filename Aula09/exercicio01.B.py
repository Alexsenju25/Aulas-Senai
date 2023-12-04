class Calculadora:

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def soma(self):
        soma = self.numero1 + self.numero2
        

    def sub(self):
        sub = self.numero1 - self.numero2
        

    def mult(self):
        mul = self.numero1 * self.numero2
     
calculadora1 = Calculadora(4,5)

calculadora1.mult()