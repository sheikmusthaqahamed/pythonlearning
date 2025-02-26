from car import Car

class Audi_A4(Car):
    def __init__(self, year):
        super().__init__("Audi", "A4", year, 4)