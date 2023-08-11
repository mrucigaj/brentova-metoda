import numpy as np
from src.utils import sign, print_header, print_step


def dekker(f, a, b, N, tol, explain):
    fa = f(a)
    fb = f(b)

    if np.sign(fa) == np.sign(fb):
        print("Signs match!")
        exit(1)

    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa

    if explain:
        print("\nDekker")
        print_header()
        print_step(0, b, a, fb, fa, 'initial')

    c = a
    fc = fa

    for i in range(1, N+1):
        if abs(c - b) < 2*tol:
            return b

        m = (b + c) / 2
        s = b - (fb * (b - a)) / (fb - fa)

        a = b 
        fa = fb

        if abs(s - b) < tol:
            b = b + sign(c - b) * tol
            mtd = 'min'

        elif (s <= b and s >= m) or (s >= b and s <= m):
            b = s 
            mtd = 'secant'

        else:
            b = m
            mtd = 'bisection'

        fb = f(b)

        if sign(fb) == sign(fc):
            c = a
            fc = fa

        if abs(fc) < abs(fb):
            a = b
            b = c
            c = a
            fa = fb
            fb = fc
            fc = fa

        if explain:
            print_step(i, b, c, fb, fc, mtd)

    return b


