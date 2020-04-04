class Sample():
    pass

obj = Sample()
print(type(obj))    # <class '__main__.Sample'>


class Dog():

    # CLASS OBJECT ATTRIBUTE: the attributes that are always true for any Dog regardless of their breed or name
    # i.e. those attributes whose values did not depend on objects those are class objects
    # for example, here the value of breed or name can be different for different dogs
    # but the value for species is always "mammal" for any dog
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


dog = Dog("Lab", "Sammy")
print(dog.breed)
print(dog.name)
print(dog.species)


class Circle():

    pi = 3.14

    def __init__(self, radius = 1):     # here 1 is default value of radius if none provided
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2

    def set_radius(self, radius):
        self.radius = radius


circle = Circle(5)
print(circle.radius)    # 5
print(circle.area())    # 78.5

circle.set_radius(3)
print(circle.area())    # 28.26
