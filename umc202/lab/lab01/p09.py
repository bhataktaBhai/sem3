import math
from p05 import newton

if __name__ == '__main__':
    f = lambda x: x**2 - 2
    g = lambda x: math.cos(x)
    x = newton(1.5, lambda x: f(x) - g(x), 1e-10)
    print((x, f(x)))
