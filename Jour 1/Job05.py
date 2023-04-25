class Animal: 
    def __init__(self, name, age ):
        self.name = name
        self.age = age 
        

    def show_infos(self):
        print("Je m'appelle ", self.name )
        print(" Mon age est de ", self.age , " ans")
        
    def vieillir(self):
        self.age += 1 

animal = Animal("Luna", 0)
animal.show_infos()
animal.vieillir() 
animal.show_infos()




