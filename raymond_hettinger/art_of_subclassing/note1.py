class Animal:
    "Generic animal class"

    def __init__(self, name):
        self.name = name

    def walk(self):
        print("{} is WALKING".format(self.name))


class Dog(Animal):
    "Man's best friend"

    def bark(self):
        "this is an example of ADDING a new method to the sub-class"
        print("{} is BARKING".format(self.name))


class Snake(Animal):
    "A very dangerous animal"

    def walk(self):
        "this is an example of OVERRIDING a method in the sub-class"
        print("{} is SLITHERING".format(self.name))


class Cat(Animal):
    "A very cute animal"

    def walk(self):
        "this is an example of EXTENDING a method in the sub-class"

        # step-1: delegates the walking behavior to the super() class
        self.super().walk()

        # step-2: extends the behavior of the walk() method by adding more behavior
        print("{} is SWISHING the tail".format(self.name))
