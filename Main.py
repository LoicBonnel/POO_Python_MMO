from CombatGroupe import CombatGroupe
from Dragon import Dragon
from Elfe import Elfe
from GroupeCombatant import GroupeCombatant
from Humain import Humain
from Nain import Nain
from Combat import Combat
from Ogre import Ogre


def Main():
    Smaug = Dragon("Smaug", 1000, "grande", 2500, 700, "rouge")
    Legolas = Elfe("Legolas", 1000, 66, 300 , "moyenne" ,"Sindar")
    Barik = Nain("Gimli", 150, 300, 900 ,"petite" , "forgeron")
    Nounours = Ogre("Nounours", 380, 3000, 2600, 6000, "Violet")

    print(Barik)
    print(Barik.parler("Par la barbe de Durin !"))

    print(Smaug)
    print(Smaug.parler("Je suis le roi sous la montagne !"))
    print(Smaug.cracher_feu())

    print(Legolas)
    print(Legolas.parler("Bonjour !"))

    Combat1 = Combat(Legolas, Smaug)
    print(Combat1)

    print(Combat1.vainceurAleatoire())

    GroupeCombatantDeLaTerre = GroupeCombatant("GroupeCombatantDeLaTerre")
    GroupeCombatantDeLaTerre.ajouter_combatant(Barik)
    GroupeCombatantDeLaTerre.ajouter_combatant(Legolas)
    GroupeCombatantDeLaTerre.ajouter_combatant(Smaug)

    GroupeCombatantDuFeu = GroupeCombatant("GroupeCombatantDuFeu")
    GroupeCombatantDuFeu.ajouter_combatant(Nounours)

    combatGroupe1 = CombatGroupe(GroupeCombatantDeLaTerre, GroupeCombatantDuFeu)
    print(combatGroupe1)

    print(combatGroupe1.vainqueurAleatoire())

if __name__ == "__main__":
    Main()