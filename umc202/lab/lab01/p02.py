import math
from p01 import bisect

if __name__ == '__main__':
    print(bisect(0, 1, lambda x: math.exp(-x) - x, 1e-4))
