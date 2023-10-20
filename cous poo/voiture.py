print ("/n")

class Voiture:
    def __init__(self, marque, couleur="rouge"):
        self.marque = marque
        self.couleur = couleur
        self.vitesse_Max = 300
        self.nb_roues = 4
        self.demarree = False
        self.vitesse = 0
       # self.vitesse_securite =self._vitesse_Max + 10 
        print("une voiture est créée")

    def demarrer(self):
        if (not self.demarree): 
            self.demarree = True
        print("la voiture démarre")


    def avancer(self, vitesse_cible):
        if self.demarree == True: 
            for i in range(0, vitesse_cible):
                if (self.vitesse + 1 <= self.vitesse_Max):
                    self.vitesse += 1
                    print(f"la voiture roule à {self.vitesse} km/h")

        
    def __str__(self):
        return f"Une voiture {self.marque} {self.couleur} roule à {self.vitesse_Max} km/h"


ma_voiture = Voiture("Yaris", "blanche")
print(ma_voiture)
ma_voiture.demarrer()
ma_voiture.avancer(200)

#ma_voiture._vitesse = 221


ta_voiture = Voiture("dacia")
print(ta_voiture)

