import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        self.creer_paquet()

    def creer_paquet(self):
        couleurs = ["Coeur", "Carreau", "Trèfle", "Pique"]
        valeurs = list(range(2, 11)) + ["Valet", "Dame", "Roi", "As"]
        for couleur in couleurs:
            for valeur in valeurs:
                carte = Carte(valeur, couleur)
                self.paquet.append(carte)

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def distribuer_carte(self):
        return self.paquet.pop()

    def nouvelle_partie(self):
        self.paquet = []
        self.creer_paquet()
        self.melanger_paquet()

    def calculer_total(self, main):
        total = 0
        as_present = False
        for carte in main:
            if isinstance(carte.valeur, int):
                total += carte.valeur
            elif carte.valeur in ["Valet", "Dame", "Roi"]:
                total += 10
            elif carte.valeur == "As":
                as_present = True
                total += 11
        if as_present and total > 21:
            total -= 10
        return total

# Fonction pour afficher les cartes d'une main
def afficher_main(main):
    cartes = [carte.valeur for carte in main]
    return ", ".join(cartes)

# Début du jeu
print("Bienvenue au jeu de Blackjack!")

# Créer un nouveau jeu
jeu = Jeu()

# Distribuer les cartes initiales au joueur et au croupier
main_joueur = [jeu.distribuer_carte(), jeu.distribuer_carte()]
main_croupier = [jeu.distribuer_carte(), jeu.distribuer_carte()]

# Afficher les cartes du joueur et la carte visible du croupier
print("Cartes du joueur: ", afficher_main(main_joueur))
print("Carte visible du croupier: ", main_croupier[0].valeur)

# Demander au joueur s'il veut prendre ou passer
while True:
    choix = input("Voulez-vous prendre une carte supplémentaire (O/N) ? ")
    if choix.lower() == "o":
        nouvelle_carte = jeu.distribuer_carte()
        main_joueur.append(nouvelle_carte)
        print("Carte tirée: ", nouvelle_carte.valeur)
        total_joueur = jeu.calculer_total(main_joueur)
        print("Total du joueur: ", total_joueur)
        if total_joueur > 21:
            print("Le joueur a dépassé 21. Le croupier gagne.")
            break
    else:
        break

# Tour du croupier de jouer
total_croupier = jeu.calculer_total(main_croupier)
while total_croupier < 17:
    nouvelle_carte = jeu.distribuer_carte()
    main_croupier.append(nouvelle_carte)
    total_croupier = jeu.calculer_total(main_croupier)

# Déterminer le gagnant
total_joueur = jeu
