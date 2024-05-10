import random
from Entite import Entite
from Arene import Arene

class Combat:
    def __init__(self, pcombatant1, pcombatant2):
        self.combattant1 = pcombatant1
        self.combattant2 = pcombatant2

    def __str__(self):
        arene_instance = Arene()
        arene = arene_instance.areneAleatoire()
        return f"Le combat entre {self.combattant1.nom} et {self.combattant2.nom},vas démarrer dans l'arène {arene} la foule est en délire."


    def vainceurAleatoire(self):
        chiffreAleatoire = random.randint(1, 11)
        if chiffreAleatoire > 5:
            phrase = f"{self.combattant1.nom} a déchiré son adversaire de manière sanglante !!!"
        elif chiffreAleatoire > 11:
            phrase = f"{self.combattant2.nom} vient de remporter le combat, regardez ça {self.combattant1.nom} cour dans les jupons de sa mère !!!"
        else:
            phrase = f"Au mon dieu quel dénouement incroyable c'est un match nul entre {self.combattant2.nom} et {self.combattant1.nom} l'arène raffle les paris Messieurs Dammes !!!"
        return phrase
