import random
from Entite import Entite

class Arene:
    def __init__(self):
        pass

    def areneAleatoire(self):
        chiffreAleatoire = random.randint(1, 3)
        pArene = chiffreAleatoire
        if pArene == 1:
            return f"Chateau du Hobbit"
        if pArene == 2:
            return f"Volcan en fusion"
        if pArene == 3:
            return f"Stade de France"




