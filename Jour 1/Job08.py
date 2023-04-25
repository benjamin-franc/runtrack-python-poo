class Livre:
    def __init__(self, titre, auteur, page):
        self.__titre = titre
        self.__auteur = auteur
        self.__page = page
        self.__disponible = True

    def show_infos(self):
        print(self.__titre)
        print(self.__auteur)
        print(self.__page)

    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def set_page(self, nouvelle_page):
        if nouvelle_page < 0:
            print("Erreur: Le nombre de pages ne peut pas être négatif.")
        else:
            self.__page = nouvelle_page

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
        else:
            print("Le livre n'a pas été emprunté.")

livre = Livre("Harry Potter", "J.K ROWLING", 150)
livre.set_page(250)
livre.show_infos()

if livre.verification():
    print("Le livre est disponible.")
    livre.emprunter()
else:
    print("Le livre n'est pas disponible.")
