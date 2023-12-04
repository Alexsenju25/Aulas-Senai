class Retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcula_area(self, base, altura):
        base = int (input ("Digite a base"))
        altura = int (input ("Digite a altura"))
        print ( f" A área do retângulo é {base * altura}")

retangulo_1 = Retangulo (15,2)

retangulo_1.calcula_area (15.2)
    
    




