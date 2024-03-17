from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on():
        pass
    
    @abstractmethod
    def turn_off():
        pass

class LightBulb(Switchable):
    def turn_on():
        print("Turning on")
    def turn_off():
        print("turning off")

class TV(Switchable):
    def turn_on():
        print("Turning on TV")
    def turn_off():
        print("turning off TV")

class Switch:
    def __init__(self, device: Switchable) -> None:
        self.on = False
        self.device = device

    def press(self):
        if self.on:
            self.bulb.turn_off()  
        else:
            self.bulb.turn_on()
        
        self.on = not self.on

bulb = LightBulb()
tv = TV()

switch1 = Switch(device=bulb)
switch1.press()
switch1.press()

switch2 = Switch(device=tv)
switch2.press()
switch2.press()