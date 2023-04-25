class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

# Création d'un objet de la classe Rectangle avec une largeur de 5 et une hauteur de 10
mon_rectangle = Rectangle(5, 10)

# Appel de la méthode aire sur l'objet mon_rectangle
resultat = mon_rectangle.aire()

# Impression du résultat
print("L'aire du rectangle est :", resultat)
