from vehicle import Vehicle
from car import Car
from bike import Bike
from audi_a4 import Audi_A4
from yamaha_r1 import Yamaha_R1

# Creating instances of each class
vehicle = Vehicle("Generic", "Model", 2020)
car = Car("Toyota", "Camry", 2021, 4)
bike = Bike("Honda", "CBR", 2022, "Sport")
audi_a4 = Audi_A4(2023)
yamaha_r1 = Yamaha_R1(2024)

# Displaying information
vehicle.display_info()
print()
car.display_info()
print()
bike.display_info()
print()
audi_a4.display_info()
print()
yamaha_r1.display_info()