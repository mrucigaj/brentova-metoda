import numpy as np
from src.utils import print_header, print_step

def brent(f, a, b, N=100, abstol=1e-5, reltol=1e-10, explain=True):
    fa = f(a)
    fb = f(b)

    if np.sign(fa) == np.sign(fb):
        print("Signs match!")
        exit(1)

    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa

    if explain:
        print("\nBrent")
        print_header()
        print_step(0, b, a, fb, fa, 'initial')

    c = a
    fc = fa

    d = b - a
    e = b - a

    for j in range(1, N+1):
        #tol = 2 * reltol * abs(b) + 0.5 * abstol
        tol = abstol

        if fb == 0:
            return b

        m = (c - b) / 2

        if abs(m) < tol:
            return b        
        
        if abs(e) < tol or abs(fa) <= abs(fb):
            d = m
            e = m
            mtd = 'bisection**'

        else:
            s = fb / fa
            
            if a == c:
                s = fb / fa
                p = (a - b) * s
                q = s - 1
                mtd = 'interpolation (linear)'
            else:
                r1 = fa / fc
                r2 = fb / fc
                p = s * ((c - b) * r1 * (r1 - r2) - (b - a) * (r2 - 1))
                q = - (r1 - 1) * (r2 - 1) * (s - 1)
                mtd = 'interpolation (iqi)'

            if 2 * abs(p) < 3 * abs(m * q):
                if abs(p/q) >= 0.5 * abs(e):
                    d = m
                    e = m
                    mtd = 'bisection*'
                else:
                    e = d
                    d = p/q
            else:
                d = m
                e = m
                mtd = 'bisection'

        a = b
        fa = fb        

        if abs(d) > tol:
            b = b + d
        else:
            b = b + np.sign(m) * tol
            mtd = 'min'

        fb = f(b)

        if np.sign(fb) == np.sign(fc):
            c = a
            fc = fa

        if abs(fc) < abs(fb):
            a = b
            fa = fb
            b = c
            fb = fc
            c = a
            fc = fa            

        if explain:
            print_step(j, b, c, fb, fc, mtd)


    return b