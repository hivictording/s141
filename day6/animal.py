# Author: Victor Ding

#Python 多态

class Animal():
    @staticmethod
    def act(obj):
        obj.action()

class Bird(Animal):
    def __init__(self,type):
        self.type = type

    def action(self):
        print("{} 在飞翔".format(self.type))

class Fish(Animal):
    def __init__(self,type):
        self.type = type

    def action(self):
        print("{} 在游来游去".format(self.type))

parrot = Bird("Parrot")
flounder = Fish("Flounder")

Animal.act(parrot)
Animal.act(flounder)