from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine():
        pass
    
    @abstractmethod
    def move():
        pass

    @abstractmethod
    def fly():
        pass

class Bicycle(Vehicle):
    def move():
        print("I like to move it move it!")

    def start_engine():
        pass

class Plane(Vehicle):
    def fly():
        print("I believe I can fly!")

