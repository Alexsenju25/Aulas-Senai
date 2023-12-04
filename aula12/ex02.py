class Veiculo():
    def mover(self):
        pass
class Carro(Veiculo):
    def mover():
        return "Dirigindo"
    
class Aviao(Veiculo):
     def mover():
        return "Voado"
    

carro = Carro
aviao = Aviao

print(carro.mover())
print(aviao.mover())