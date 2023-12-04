class Animal():
    def emitir_som():
        pass
class Gato(Animal):
    def emitir_som():
        return "Miau"
    
class Cachorro(Animal):
     def emitir_som():
        return "Au au"
    

cachorro = Cachorro
gato = Gato

print(cachorro.emitir_som())
print(gato.emitir_som())