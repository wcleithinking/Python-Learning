# -*- coding: utf-8 -*-

class MyClass:
    """A simple example class"""

    def __init__(self):
        self.data = []

    i = 12345

    def f(self):
        return 'hello world'

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

class Dog:
    
    # tricks = []             # mistaken use of a class variable

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        self.tricks = []    # create a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        print("Hello World")

    h = g

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclss(Mapping):

    def update(self, keys, values):
        # provide new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

class Employee:
    pass

john = Employee()   # create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

x = Complex(3.0, -4.5)
print('x =', x.r, '+', str(x.i)+'i')

y = MyClass()   # create class instance
print(y.__doc__)
print(y.i)
print(y.f())

y.counter = 1
while y.counter < 10:
    y.counter = y.counter * 2

print(y.counter)
del y.counter

yf = y.f
while False:
    print(yf())

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind, e.kind)
print(d.name, e.name)

d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

z = int(3)
print(isinstance(z, int))
print(issubclass(bool, int))
print(issubclass(float, int))
