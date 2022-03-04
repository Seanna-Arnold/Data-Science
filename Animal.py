class Animal(object): #Animal is inheriting from object
    def __init__(self, numteeth,spots,weight):
        self.numteeth = numteeth
        self.spots = spots
        self.weight = weight

class Lion(Animal): #Lion is Inheriting from Animal
    ''' An example of inheritance (see reading).
    This class inherits its constructor and the get_color method from Animal,
    and every instance of Cow is also an instance of Animal. '''
    def __init__(self, numteeth,spots,weight):
        super().__init__(numteeth,spots,weight)

    def weight_age(self):
        if self.weight <= 80:
            # set up conditional arguments that determine gender
             print("This is a lion cub")

        elif self.weight <= 120:
             print("This is a lioness")

        else:
             print("This is an adult, male Lion")

animal = Animal(10, 20, 30)            
lion = Lion(numteeth = 10, spots=False, weight=130)
#give input to test the program after coverting the class into a variable
lion.weight_age()  # add the variable to the function

class Cheetah(Animal):
    def __init__(self, numteeth,spots,weight):
        super().__init__(numteeth, spots, weight)

    def gender_spots(self):
        if self.spots == True:
            # spots on belly determines the gender of cheetah
            print("This is a male cheetah because it has spots on the belly")

        else:
            print("This is a female cheetah because it has no spots on the belly")
            
cheetah = Cheetah(8, True, 67)
cheetah.gender_spots()
