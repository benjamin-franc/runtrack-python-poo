class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("L'âge de la personne est :", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, new_age):
        self.age = new_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=14):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation d'une classe Personne avec un age par défaut de 14
personne1 = Personne()
# Instanciation d'une classe Eleve avec un age par défaut de 14
eleve1 = Eleve()
# Affichage de l'âge par défaut de l'élève
eleve1.affichageAge()

        

