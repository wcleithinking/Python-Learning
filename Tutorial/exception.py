import sys

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attribute:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not allowed.

    Attribute:
        previous -- state at beginning of the transition
        next -- attepted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


try:
    f = open('workfile.js')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print("cannot open", arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print('x=',x)
    print('y=',y)

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print("Handing run-time error:", err)


def divide(x, y):
    try:
        result  = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2,1)
divide(2,0)
divide("2","1")

with open("workfile.js") as f:
    for line in f:
        print(line, end="")


try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')


try:
    raise NameError('HiThere')
except NameError:
    print("An exception flew by!")
    raise

raise ValueError    # shorthand for 'raise ValueError()'

raise NameError('HiThere')

