import math
from p05 import newton

if __name__ == '__main__':
    f = lambda x: math.tan(x) - x
    print(newton(4, f, 1e-3))
    print(newton(4.6, f, 1e-3))
