from abc import ABC, override
from typing import List

class Bird(ABC):
    def walk():
        pass

class FlyingBird(ABC):
    def walk():
        pass
    def fly():
        pass


class Eagle(Bird, FlyingBird):
    def walk():
        print("Eagles can walk!")

    def fly():
        print("Eagles can fly!")


class Penguin(Bird):

    def walk():
        print("Penguins can walk!")


def shoo_shoo(birds: List[FlyingBird]):
    for bird in birds:
        bird.walk()
        bird.fly()

shoo_shoo([Eagle()])