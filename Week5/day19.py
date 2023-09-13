"""
Weifeng Zhao
August 31: Python classes
"""
print("\n ------- class Person ----------")
print("\n ---------------------------- \n")


# create a class. Class name is always capitalized
class Myclass:
    num = 5

# create an object for class MyClass
p1 = Myclass()
print(p1)
print(f"\nObject num = {p1.num}")

#: The __init__() function is called automatically every time the class is being
# used to create a new object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # object method
    def printObject(self):
        print(f"Hello! my name is {self.name}")

# create an object and initialize values:
person1 = Person("John", 30)
print(f"Object nane = {person1.name}")
print(f"Object age is {person1.age}")

# printing an object method
print(f"\n{person1.printObject()}")

# delete properties using del keyword
del person1.name


# pass statement is used to pass an empty class
class House:
    pass

print(f"print {House}")
print("\n ------- class Chair -------\n")
print("\n ---------------------------- \n")


class Chair:
    # accessible properties
    chair_color = "brown"

    def __init__(self, height, width, length):
        self.height = height
        self.__width = width  # __ make it very private properties
        self.length = length
        self.length *= 2

    # define a method to print result
    def print_result(self):
        print(f"The length of the chair is: {self.length}")

    # pass the height
    def get_height(self):
        return self.height

    # pass the accesssible property
    def get_color(self):
        return self.chair_color

    # update class values
    def set_price(self, price):
        self._price = price # _ makes a private property

# initialize an obejct for class chair
chair1 = Chair(20, 10, 30)
chair1.print_result()

print(f'The chair height {chair1.get_height()}')
print(f'\nThe chair color is {chair1.chair_color} ')
# update price data
chair1.set_price(25)
print(f'Chair price is {chair1._price}')
# print(f'\nVery private width = {chair1.__width}')
