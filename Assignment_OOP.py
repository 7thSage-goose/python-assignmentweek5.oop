from parent_classes import Animal
class Dog(Animal):  #The dog class will inherit all the Animal attributes
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")  #This method is different for each class

dog = Dog("Arcanine")
cat = Cat("Evee")
