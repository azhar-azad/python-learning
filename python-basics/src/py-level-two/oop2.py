# Inheritance

class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")


animal = Animal()
animal.who_am_i()
animal.eat()

print("######################")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)   # Calling Base class constructor
        print("DOG CREATED")

    def eat(self):          # Method Overriding
        print("DOG EATING")

    def bark(self):
        print("WOOF!!")


dog = Dog()
dog.who_am_i()
dog.eat()
dog.bark()

print("######################")

# Special Methods of Classes

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {},\nAuthor: {},\nPages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return "The length of the book is {}".format(self.pages)

    def __del__(self):
        print("The book is destroyed")



book = Book("Python", "Azad", 200)
print(book)
print(len(book))
del book


