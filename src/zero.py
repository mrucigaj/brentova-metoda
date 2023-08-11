import numpy as np
from src.methods.bisection import bisection
from src.methods.secant import secant
from src.methods.iqi import iqi
from src.methods.dekker import dekker
from src.methods.brent import brent

def seek_sign_change(f, a, width, explain):
    fa = f(a)
    sgn = np.sign(fa)
    margin = a/50
    if abs(a) < 0.0001:
        margin = 1/50
    sqrt2 = np.sqrt(2)

    if explain:
        print("\nIskanje\na = %.10f, f(a) = %.10f" % (a, fa))
        print(f'x \t\t a-x \t\t a+x \t\t f(a-x) \tf(a+x)')

    while margin < width:
        if explain:
            print(f'{"%.10f" % margin} \t {"%.10f" % (a - margin)} \t {"%.10f" % (a + margin)} \t {"%.10f" % f(a - margin)} \t {"%.10f" % f(a + margin)}')
        if np.sign(f(a - margin)) != sgn:
            return a - margin
        if np.sign(f(a + margin)) != sgn:
            return a + margin

        margin *= sqrt2

    return None

def zero(metoda, f, prb, N, abstol, reltol, explain=True):
    if type(prb) is tuple and len(prb) == 2:
        a = prb[0]
        b = prb[1]
    else:
        a = prb
        b = seek_sign_change(f, a, 100, explain)
    
    if metoda == 'bisection':
        return bisection(f, a, b, N, abstol, explain)    
    if metoda == 'secant':
        return secant(f, a, b, N, abstol, explain)    
    if metoda == 'iqi':
        return iqi(f, -0.5, 1, 1.5, N, abstol, explain)
    if metoda == 'dekker':
        return dekker(f, a, b, N, abstol, explain)    
    if metoda == 'brent':
        return brent(f, a, b, N, abstol, reltol, explain)

    print("Unknown method!")