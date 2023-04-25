class Vehicule:
    def __init__(self, marque, model, annee, prix):
        self.marque = marque
        self.model = model
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque:", self.marque)
        print("model:", self.model)
        print("Année:", self.annee)
        print("Prix:", self.prix)


class Voiture(Vehicule):
    def __init__(self, marque, model, annee, prix, portes):
        super().__init__(marque, model, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes:", self.portes)


# Instanciation d'un objet Voiture avec les attributs nécessaires
voiture1 = Voiture("Mercedes", "Classe A", 2020, 18500, 4)

# Appel à la méthode informationsVehicule de la classe Voiture
voiture1.informationsVehicule()

class Vehicule:
    def __init__(self, marque, model, annee, prix):
        self.marque = marque
        self.model = model
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque:", self.marque)
        print("Model:", self.model)
        print("Année:", self.annee)
        print("Prix:", self.prix)


class Voiture(Vehicule):
    def __init__(self, marque, model, annee, prix, portes):
        super().__init__(marque, model, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes:", self.portes)


class Moto(Vehicule):
    def __init__(self, marque, model, annee, prix, roues=2):
        super().__init__(marque, model, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues:", self.roues)


# Instanciation d'un objet Moto avec les attributs nécessaires
moto1 = Moto("Yamaha", "1200Vmax", 1987, 4500)

# Appel à la méthode informationsVehicule de la classe Moto
moto1.informationsVehicule()

class Vehicule:
    def __init__(self, marque, model, annee, prix):
        self.marque = marque
        self.model = model
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque:", self.marque)
        print("model:", self.model)
        print("Année:", self.annee)
        print("Prix:", self.prix)

    def demarrer(self):
        print("Attention, je roule.")


class Voiture(Vehicule):
    def __init__(self, marque, model, annee, prix, portes):
        super().__init__(marque, model, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes:", self.portes)

    def demarrer(self):
        print("La voiture démarre et file à toute allure!")


class Moto(Vehicule):
    def __init__(self, marque, model, annee, prix, roues=2):
        super().__init__(marque, model, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues:", self.roues)

    def demarrer(self):
        print("La moto démarre avec un rugissement puissant!")


# Instanciation d'un objet Voiture et d'un objet Moto
voiture1 = Voiture("Mercedes","Classe A", 2020, 18500, 4)
moto1 = Moto("Yamaha","Vmax", 1987, 4500)

# Appel à la méthode demarrer de la classe Voiture et Moto
voiture1.demarrer()
moto1.demarrer()

