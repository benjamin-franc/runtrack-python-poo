class Livre:
    def __init__(self , titre, auteur, page ):
        self.__titre = titre
        self.__auteur = auteur
        self.__page = page 

    def show_infos(self):
        print(self.__titre)
        print(self.__auteur)
        print(self.__page)

    def get_titre(self):
        self.__titre
    
    def get_auteur(self):
        self.__auteur
    
    def set_page(self , nouvelle_page):
        self.__page = nouvelle_page

    def set_page(self, nouvelle_page):
        if nouvelle_page < 0:
            print("Erreur: Le nombre de pages ne peut pas être négatif.")
        else:
            self.__page = nouvelle_page
    
livre = Livre("Harry Potter" ,"J.K ROWLING", 150 )
livre.set_page(250)
livre.show_infos()