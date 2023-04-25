class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.get_longueur() + self.get_largeur())  # Utilisation des méthodes d'accès

    def surface(self):
        return self.get_longueur() * self.get_largeur()  # Utilisation des méthodes d'accès


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.get_hauteur()  # Utilisation des méthodes d'accès


# Instanciation de la classe Rectangle
rectangle1 = Rectangle(5, 10)
print("Longueur du rectangle: ", rectangle1.get_longueur())
print("Largeur du rectangle: ", rectangle1.get_largeur())
print("Périmètre du rectangle: ", rectangle1.perimetre())
print("Surface du rectangle: ", rectangle1.surface())

# Modification des attributs du rectangle
rectangle1.set_longueur(8)
rectangle1.set_largeur(12)
print("Nouvelle longueur du rectangle: ", rectangle1.get_longueur())
print("Nouvelle largeur du rectangle: ", rectangle1.get_largeur())
print("Nouveau périmètre du rectangle: ", rectangle1.perimetre())
print("Nouvelle surface du rectangle: ", rectangle1.surface())

# Instanciation de la classe Parallelepipede
parallelepipede1 = Parallelepipede(5, 10, 3)
print("Longueur du parallélépipède: ", parallelepipede1.get_longueur())
print("Largeur du parallélépipède: ", parallelepipede1.get_largeur())
print("Hauteur du parallélépipède: ", parallelepipede1.get_hauteur())
print("Périmètre du parallélépipède: ", parallelepipede1.perimetre())
print("Surface du parallélépipède: ", parallelepipede1.surface())
print("Volume du parallélépipède: ", parallelepipede1.volume())

# Modification des attributs du parallélépipède
parallelepipede1.set_longueur(8)
parallelepipede1.set_largeur(12)
parallelepipede1.set_hauteur(4)
print("Nouvelle longueur du parallélépipède: ", parallelepipede1.get_longueur())
print("Nouvelle largeur du parallélépipède: ", parallelepipede1.get_largeur())
print("Nouvelle hauteur du parallélépipède: ", parallelepipede1.get_hauteur())
print("Nouvelle hauteur du parallélépipède: ", parallelepipede1.perimetre())
print("Nouvelle hauteur du parallélépipède: ", parallelepipede1.surface())
print("Nouvelle hauteur du parallélépipède: ", parallelepipede1.volume())
