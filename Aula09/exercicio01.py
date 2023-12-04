#Crie uma classe Calculadora que possui métodos para adicionar, subtrair, multiplicar e dividir dois números

class Calculadora:

    def __init__(self, numero1, numero2):
            self.numero1 = numero1
            self.numero2 = numero2

    def somar(self, numero1,numero2):
          return numero1 + numero2
    
    def subtrair(self, numero1, numero2):
          return numero1 - numero2
    
    def multiplicar(self, numero1, numero2):
          return numero1 * numero2
    
    def dividir(self,numero2):
        if numero2 == 0:
              return "Não é possivel dividir por zero"
        
calculadora1 = Calculadora (4,5)

calculadora1.somar ()