class Personne:
    def __init__(self, age=15):
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
# Instanciation d'une classe Personne avec un age par défaut de 14
personne1 = Personne()

# Instanciation d'une classe Eleve avec un age par défaut de 14
eleve1 = Eleve()
# Appel de la méthode bonjour de la classe Eleve
eleve1.bonjour()
eleve1.affichageAge()
# Appel de la méthode allerEnCours de la classe Eleve
eleve1.allerEnCours()
# Redéfinition de l'âge de l'élève à 15 ans
eleve1.modifierAge(15)

# Instanciation d'une classe Professeur avec un age de 40 ans
professeur1 = Professeur("Mathématiques", 40)
# Appel de la méthode bonjour de la classe Professeur
professeur1.bonjour()
# Appel de la méthode enseigner de la classe Professeur
professeur1.enseigner()
