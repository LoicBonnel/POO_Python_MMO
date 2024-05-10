from Entite import Entite

class Humain(Entite):
    def __init__(self, nom, age, taille, vie, force, Qi):
        super().__init__(nom, age, taille, vie, force)
        self.Qi = Qi

    def detruireEnvironement(self):
        return f"{self.nom} fais bruler le terrain !"
