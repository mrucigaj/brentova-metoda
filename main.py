from src.zero import zero
from src.functions.functions import *


# function name from functions.py
f = f1

# max. number of steps
N = 200

# absolute tolerance
abstol = 1e-8

# relative tolerance
reltol = 1e-10

# method used <bisection, secant, iqi, dekker, brent>
# note: methods 'secant' and 'iqi' may not converge.
method = 'brent'

# intial approximation
a, b = -3, 3


x = zero(method, f, (a, b), N, abstol=abstol, reltol=reltol)

print(x)