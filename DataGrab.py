class Vehicles:
    def __init__(self):
        self.color = None
        self.engine_type = None
        self.cost = None
    def setVehicles(self):
        self.color = input("Color: ")
        self.Engine_type = input("Engine Type: ")
        self.cost = input("Cost: ")

class Cars(Vehicles):
    def __init__(self):
        Vehicles.__init__(self)
        self.doors = None
        self.mileage = None
    def setCars(self):
        self.doors = input("Number of Doors: ")
        self.mileage = input("Miles per Gallon: ")
class Trucks(Vehicles):
    def __init__(self):
        Vehicles.__init__(self)
        self.doors = None
        self.mileage = None
        self.fourwheel_drive = None
        self.tow_package = None
    def setTrucks(self):
        self.doors = input("Number of Doors: ")
        self.mileage = input("Miles per Gallon: ")
        self.fourwheel_drive = input("Is it four wheel drive: ")
        self.tow_package = input("Does it have tow package: ")
class Boats(Vehicles):
    def __init__(self):
        Vehicles.__init__(self)
        self.type = None
        self.length = None
    def setBoats(self):
        self.type = input("What type of Boat is it: ")
        self.length = input("Length of the boat: ")

car = Cars()
car.setVehicles()
car.setCars()
truck = Trucks()
truck.setVehicles()
truck.setTrucks()
boat = Boats()
boat.setVehicles()
boat.setBoats()
