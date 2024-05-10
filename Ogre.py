from Entite import Entite

class Ogre(Entite):
    def __init__(self, nom, age, taille, vie, force, couleur):
        super().__init__(nom, age, vie, force,  taille)
        self.couleur = couleur

    def cracher_feu(self):
        return f"{self.nom} Se régale en mangant un gros nain !"