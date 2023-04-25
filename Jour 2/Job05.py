import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

# Création d'un objet de la classe Rectangle avec une largeur de 5 et une hauteur de 10
mon_rectangle = Rectangle(5, 10)

# Appel de la méthode aire sur l'objet mon_rectangle
resultat_rectangle = mon_rectangle.aire()

# Impression du résultat
print("L'aire du rectangle est :", resultat_rectangle)

# Création d'un objet de la classe Cercle avec un rayon de 3
mon_cercle = Cercle(3)

# Appel de la méthode aire sur l'objet mon_cercle
resultat_cercle = mon_cercle.aire()

# Impression du résultat
print("L'aire du cercle est :", resultat_cercle)
