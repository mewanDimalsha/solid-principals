from abc import ABC, abstractmethod
from shutil import move

class Vehicle(ABC):
    @abstractmethod
    def move():
        pass

class VehicleWithEngine(Vehicle):
    @abstractmethod
    def start_engine():
        pass

class FlyingVehicle(Vehicle):
    @abstractmethod
    def fly():
        pass


class Bicycle(Vehicle):
    def move():
        print("I like to move it move it!")


class Car(VehicleWithEngine):
    def move():
        print("move!")

    def start_engine():
        print("Starting!")

class Plane(VehicleWithEngine, FlyingVehicle):
    def move():
        print("I can move")
    
    def start_engine():
        print("Staring")

    def fly():
        print("Flying")

