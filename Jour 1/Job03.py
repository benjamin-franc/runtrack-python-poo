class Operation:
    def __init__(self, nombre1 , nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def show_infos(self):
        print("Le nombre est ", self.nombre1)
        print("Le nombre est ", self.nombre2)

    def __add__(self , other):
        return self.nombre1 + self.nombre2


operation = Operation(12 , 3)
operation.show_infos()

resultat= operation + operation 
print(resultat)