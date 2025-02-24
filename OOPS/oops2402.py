
class Fruit:

    print("Class level Print - 1")
    #variable
    value = 100 #Class variable

    #constructor - Used to declare and initialize instance variables
    def __init__(self,name,colour = "Neutral Colour"):

        print("I will be automatically called when the object is set") 

        self.fruitColour = colour #instance variable
        self.fruitName = name #instance variable
    
    #methods
    def cutFruit(self):
        print("Fruit is cut")

    def getColour(self):
        print(f"Colour for {self.fruitName} is {self.fruitColour}")
        print(f"My class value is {Fruit.value}")
    
    print("Class level Print - 2")

apple = Fruit("apple","Red") #Object creation
guava = Fruit("guava") #Object creation

apple.getColour()
guava.getColour()

print(apple.value)