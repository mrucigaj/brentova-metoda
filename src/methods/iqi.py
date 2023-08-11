from src.utils import print_header, print_step

def iqi(f, a, b, c, N, tol, explain):
    fa = f(a)
    fb = f(b)
    fc = f(c)

    if explain:
        print("\nInverse quadratic interpolation")
        print_header()
        print_step(0, c, 0, fc, 0, 'initial')

    for i in range(1, N+1): 
        l02 = (fb * fc) / ((fa - fb) * (fa - fc))
        l12 = (fa * fc) / ((fb - fa) * (fb - fc))
        l22 = (fa * fb) / ((fc - fa) * (fc - fb))

        new = a * l02 + b * l12 + c * l22

        a, b, c = b, c, new
        fa, fb, fc = fb, fc, f(new)

        if explain:
            print_step(i, c, 0, fc, 0, 'iqi')

    return b


