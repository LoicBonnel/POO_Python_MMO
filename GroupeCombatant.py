

class GroupeCombatant:
    def __init__(self, nom):
        self.nom = nom
        self.combattants = []


    def ajouter_combatant(self, combatant):
        self.combattants.append(combatant)
