class Animal:
    "Generic animal class"

    def __init__(self, name):
        self.name = name

    def walk(self):
        print("{} is WALKING".format(self.name))


class Dog(Animal):
    """Man's best friend"""

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
        super().walk()

        # step-2: extends the behavior of the walk() method by adding more behavior
        print("{} is SWISHING the tail".format(self.name))


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} with radius = {self.radius} and area = {self.area()}"


class Donut(Circle):
    def __init__(self, outer_radius, inner_radius):
        Circle.__init__(self, outer_radius)
        self.inner_radius = inner_radius

    def area(self):
        # !TODO: `outer_radius` will now hold value of the Circle's `radius`
        outer_radius = self.radius  # !TODO: very interesting
        inner_radius = self.inner_radius

        return Circle(outer_radius).area() - Circle(inner_radius).area()


if __name__ == "__main__":
    dog = Dog("Rover")
    dog.walk()
    dog.bark()

    snake = Snake("Python")
    snake.walk()

    cat = Cat("Fluffy")
    cat.walk()

    donut = Donut(10, 5)
    print(donut)
