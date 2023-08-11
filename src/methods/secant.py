from src.utils import print_header, print_step

def secant(f, a, b, N, tol, explain):
    fa = f(a)
    fb = f(b)

    if explain:
        print("\nSecant")
        print_header()
        print_step(0, b, a, fb, fa, 'initial')

    for i in range(1, N+1):
        if abs(a - b) < 2*tol:
            return b
        
        b_new = b - fb*(b - a)/(fb - fa)
        a = b
        b = b_new

        fa = fb
        fb = f(b)

        if explain:
            print_step(i, b, a, fb, fa, 'secant')

    return b