class Vehicle:
    licenseNumber = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On: Air")

class Car(Vehicle):
    def sayhello(self):
        print("Hello world.")

class Van(Vehicle):
    pass

class Pickup(Vehicle):
    pass

class Estatecar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirConditioner()
car1.sayhello()

pickup1 = Pickup()
pickup1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

estatecar1 = Estatecar()
estatecar1.turnOnAirConditioner()