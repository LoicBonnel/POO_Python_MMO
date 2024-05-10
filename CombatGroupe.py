import random
from Entite import Entite
from Arene import Arene
from GroupeCombatant import GroupeCombatant

class CombatGroupe:
    def __init__(self, groupe1, groupe2):
        self.groupe1 = groupe1
        self.groupe2 = groupe2

    def __str__(self):
        arene_instance = Arene()
        arene = arene_instance.areneAleatoire()
        return f"Le combat entre {self.groupe1.nom} et {self.groupe2.nom} va démarrer dans l'arène {arene}. La foule est en délire."

    def vainqueurAleatoire(self):
        if len(self.groupe1.combattants) > len(self.groupe2.combattants):
            phrase = f"{self.groupe1.nom} a déchiré son adversaire de manière sanglante !!!"
        elif len(self.groupe1.combattants) < len(self.groupe2.combattants):
            phrase = f"{self.groupe2.nom} vient de remporter le combat, regardez ça {self.groupe1.nom} gissent sur le sol !!!"
        else:
            combattant1 = random.choice(self.groupe1.combattants)
            combattant2 = random.choice(self.groupe2.combattants)
            chiffreAleatoire = random.randint(1, 11)
            if chiffreAleatoire > 5:
                phrase = f"{combattant1.nom} a déchiré son adversaire de manière sanglante !!!"
            elif chiffreAleatoire > 10:
                phrase = f"{combattant2.nom} vient de remporter le combat, regardez ça {combattant1.nom} cour dans les jupons de sa mère !!!"
            else:
                phrase = f"Au mon dieu quel dénouement incroyable c'est un match nul entre {combattant2.nom} et {combattant1.nom} l'arène raffle les paris Messieurs Dames !!!"
        return phrase
