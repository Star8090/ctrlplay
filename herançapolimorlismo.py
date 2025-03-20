# # encapisulamento

# class A:
#     a = 1
#     __b = 2

# class B(A):
#   __c = 3
#   def __int__(self):
#    print(self.a)
#    print(self.__c)

# exibirA = A() 
# print(exibirA.a) #exibindo atributo publico d a classe A
# print(exibirA.__b) # ERRO: atributo privado da classe A


class animal:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade

    def emitirsom(self):
      return "som de animal"
    def informacao(self):
      return f"nome: {self.nome}, idade: {self.idade} anos"
    
class cachorro(animal):
    def emitirsom(self):
        return "au!"
      
class gato(animal):
    def emitirsom(self):
        return "miauuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu"
    
class jacare(animal):
    def emitirsom(self):
        return "arigator"

class blobfish(animal):
    def emitirsom(self):
        return "BLOB BLOO BLOU"


animal1 = cachorro("osvaldo", 5)
animal2 = gato("adolf", 7)
animal3 = jacare("losé", 67)
animal4 = blobfish("joao", 10000)

print(animal1.emitirsom())
print(animal2.emitirsom())
print(animal3.emitirsom())
print(animal4.emitirsom())