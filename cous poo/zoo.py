class Animal:
    def __init__(self, nom):
        self.nom = nom 
        print(f"Création d'un animal {self.nom}")
    def nourrir(self):
         print("Verifier que l'animal est vivant")
         print("Calcul du stock")
         print("Debut de l'alimentation de l'animal")

        

class Chat(Animal) : 
       def nourrir(self):
            super().nourrir()
            print("je le fais un calin") 
       
class Requin(Animal) :
     def nourrir(self):
          super().nourrir()
          print("Wallah je cours/nage vite")

class Licorne(Animal):
     def nourrir(self):
          super().nourrir()
          print("je fais rien")

minou = Chat("miaous")
# minou.nourrir()

croc = Requin("Bill Gates")
# croc.nourrir()

php_bien_code = Licorne("yo")
# php_bien_code.nourrir()

animaux = [minou,croc,php_bien_code]

animal: Animal
for animal in animaux:
     animal.nourrir()
     print("---")