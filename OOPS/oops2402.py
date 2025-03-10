
class Fruit:

    print("Class level Print - 1")
    #variable
    value = 100 #Class variable
    pieces = "default Pieces"

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



    def getPiece(self,pieces):
        print(f"{self.fruitName} is divided into {pieces} pieces")
        print(f"{self.fruitName} has {self.pieces} ")

    
    print("Class level Print - 2")

apple = Fruit("apple","Red") #Object creation
guava = Fruit("guava") #Object creation

apple.getColour()
guava.getColour()
apple.getPiece(5)
guava.getPiece(6)

print(apple.value)