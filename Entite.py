class Entite:
    def __init__(self, nom, age, taille, vie, force):
        self.nom = nom
        self.age = age
        self.taille = taille
        self.vie = vie
        self.force = force

    def __str__(self):
        return f"{self.nom}, âgé de {self.age} ans, de taille {self.taille}, avec {self.vie} de vie et une force de {self.force}."

    def parler(self, message):
        return f"{self.nom} dit : {message}"

    def vieillir(self, annees=1):
        self.age += annees
