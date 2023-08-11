import numpy as np

def sign(num):
    sgn = np.sign(num)
    if sgn == 0:
        return 1
    return sgn

def print_header():
    print(f'i \t b \t\t\t c \t\t\t f(b) \t\t f(c) \t\t diff \t\t method')

def print_step(i, b, c, fb, fc, method):
    fb = format_num(fb)
    fc = format_num(fc)
    diff = format_num(abs(b - c))        
    print(f'{i} \t {"%.15f" % b} \t {"%.15f" % c} \t {fb} \t {fc} \t {diff} \t' + method)

def format_num(num):
    if abs(num) > 1e-5:
        n = '{:.8f}'.format(num)
    else:
        n = '{:.5e}'.format(num)

    if num < 0:
        return n
    else:
        return ' ' + n