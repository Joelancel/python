from random import randint

class Dice:
    def __init__(self, faces=6):
        self._face= faces
    
    def __str__(self) -> str:
        return f"I'm a {self._face} faces dice"
    
    def roll(self):
        return randint(1,self._face)

class RiggedDice(Dice):
        
    def roll(self, rigged=False): 
        return self._face if rigged else super().roll()


if __name__=="__main__":
    d1= RiggedDice()
    
    print(d1.roll(True))
    print(d1.roll())