from Entite import Entite

class Nain(Entite):
    def __init__(self, nom, age, vie, force, taille, metier):
        super().__init__(nom, age, vie, force, taille)
        self.metier = metier