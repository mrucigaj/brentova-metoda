import math

def f1(x):
    return x**3 - 2*x - 5
    # zero at x = 2.0945515

def f2(x):
    return 1 - 1 / (x**2)
    # zero at x = 1, -1

def f3(x):
    return (x - 3)**3
    # zero at x = 3

def f4(x):
    return x**2 + 3*x - 3
    # zero at 0.791

def f6(x):
    return math.cos(2*x)
    # zero on (0,1)

def f7(x):
    return x**3 - x**2 - x - 1
    # zero at 1.83928

def f8(x):
    return 1 / (x-3) - 6
    #zero at 3.16667

def f9(x):
    return x**3

def f10(x):
    return x**2 + 2*x - 1

def f11(x):
    return 5*x**4 - 4*x - 1

def f12(x):
    return (x**3 - x - 1) / x
    # zero at 1.3
    # pole at 0

def f13(x):
    return x**9

def f14(x):
    return (x - 3)**5


### functions used in my thesis ###

def test_f1(x):
    return x**3 + x**2 - 2*x - 1

def test_f2(x):
    return math.sin(x**2)**3 + x - 1

def test_f3(x):
    return (x - 2)**3

def test_f4(x):
    return (x - 2)**5

def test_f5(x):
    return (x - 2)**9


### special functions

def test_fx(x):
    delta = 1e-1
    if x >= delta and x <= 3:
        return 2**(x/delta)
    if x == 0:
        return -((3 - delta)/delta) * 2**(3/delta)
    return 1