from Entite import Entite

class Elfe(Entite):
    def __init__(self, nom, age, vie, force, taille, clan):
        super().__init__(nom, age, vie, force, taille)
        self.clan = clan