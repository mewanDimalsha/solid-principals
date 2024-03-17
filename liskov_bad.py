from abc import ABC, abstractmethod, override
from typing import List

class Bird(ABC):
    @abstractmethod
    def fly():
        pass
    
    @abstractmethod
    def walk():
        pass

class Eagle(Bird):
    def walk():
        print("Eagles can walk!")

    def fly():
        print("Eagles can fly!")


class Penguin(Bird):

    def walk():
        print("Penguins can walk!")

    def fly():
        raise Exception("Penguins can't fly!")


def shoo_shoo(birds: List[Bird]):
    for bird in birds:
        bird.walk()
        bird.fly()

shoo_shoo([Eagle(), Penguin()])