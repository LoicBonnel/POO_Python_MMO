from Entite import Entite

class Dragon(Entite):
    def __init__(self, nom, age, vie, force, taille, couleur):
        super().__init__(nom, age, vie, force, taille)
        self.couleur = couleur

    def cracher_feu(self):
        return f"{self.nom} crache du feu !"
