from abc import ABC, abstractmethod
class Animal():
    self.hunger = 0
    def __init__(self,name):
        self.name = name
        self.is_alive = True
        #defines the eat method(replenishes hunger!)
    def eat(self):
        self.hunger -= 1
        print(f"{self.name} is eating")
    #Defines the sleep method(replenishes energy!)
    def sleep(self):
        self.energy += 100
        print(f"{self.name} is asleep")