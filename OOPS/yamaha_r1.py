from bike import Bike

class Yamaha_R1(Bike):
    def __init__(self, year):
        super().__init__("Yamaha", "R1", year, "Sport")