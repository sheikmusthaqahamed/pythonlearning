
class Dog():

    def __init__(self,name,breed,colour):
        self.name = name #public 
        self._breed = breed #protected
        self.__colour = colour #private

    def sound(self):
        print(f"{self.name} is the name")
        print(f"{self._breed} is the breed")
        print(f"{self.__colour} is the colour")

    def get_colour(self):
        return self.__colour

    def set_colour(self,colour):
        self.__colour = colour

dog = Dog("Sulthan", "Pomerian", "White")
print(dog.get_colour())
dog.set_colour("Pink")
print(dog.get_colour())