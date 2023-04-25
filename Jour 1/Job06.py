class Rectangle:
    def __init__(self , longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur 

    def show_infos(self):
        print(self.__longueur)
        print(self.__largeur)

    def get_longueur(self):
        return self.__longueur
    
    def set_largeur(self , nouvelle_largeur):
        self.__largeur = nouvelle_largeur
    
rectangle = Rectangle(10 , 5 )
print(rectangle.get_longueur())
rectangle.set_largeur(7)
rectangle.show_infos()