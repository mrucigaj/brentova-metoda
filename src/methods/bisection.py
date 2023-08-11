import numpy as np
from src.utils import print_header, print_step

def bisection(f, a, b, N, tol, explain):
    fa = f(a)
    fb = f(b)

    if explain:
        print("\nBisection")
        print_header()
        print_step(0, b, a, fb, fa, 'initial')

    if np.sign(fa) == np.sign(fb):
        print("Signs match!")
        exit(1)

    for i in range(1, N+1):
        m = (a + b) / 2

        if abs(a - b) < 2*tol:
            return m

        fm = f(m)

        if np.sign(fm) != np.sign(fa):
            b = m
            fb = fm
        else:
            a = m
            fa = fm

        if explain:
            print_step(i, b, a, fb, fa, 'bisection')

    return m
  