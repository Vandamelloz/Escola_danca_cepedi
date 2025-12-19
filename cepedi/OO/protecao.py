#VISIBILIDADE DA CLASSE
class Animal:
 def __init(self, especie, peso):
    self.especie= especie
    self.peso= peso
 def getEspecie(self):
   return self.especie
 def setEspecie(self, novaEspecie):
   self.__especie= novaEspecie
 def respirar():
   print("Chamei respirar!")

class Cachorro(Animal):
  def latir():
     respirar()
     print("Auau")
     pass
class Gato(Animal):
 pass
   