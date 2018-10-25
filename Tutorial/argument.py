# -*- coding: utf-8 -*-

def cheeseshop(kind,*arguments,**keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw,":",keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def concat(*args, sep="/"):
    return sep.join(args)

print(concat('earth','mars','venus'))

print(concat('earth','mars','venus',sep="."))

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage":"four million", "state":"bleedin's demised", "action":"VOOM"}

parrot(**d)


def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(42)
print(f(0))
print(f(1))

pairs = [(1,'one'), (2,'two'),(3,'three'),(4,'four')]
key = lambda  pair:pair[1]
print(key(pairs[0]))
pairs.sort(key=lambda pair:pair[1])
print(pairs)


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

def f(ham: str, eggs: str='eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

print(f('spam'))
