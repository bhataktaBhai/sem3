import math
from typing import Literal
from vector import Vector
from numbers import Number
from itertools import zip_longest

class Polynomial(Vector):
    degree: int | Literal[-math.inf]
    # def __init__(self, coeffs=None):
    #     if coeffs is None:
    #         self.coeffs = (0,)
    #     elif isinstance(coeffs, Number):
    #         self.coeffs = (coeffs,)
    #     else:
    #         coeffs = tuple(coeffs)
    #         length = len(coeffs)
    #         while length > 1 and coeffs[length - 1] == 0:
    #             length -= 1
    #         self.coeffs = coeffs[:length]
    #     self.degree = len(self.coeffs) - 1
    # def __init__(self, *args):
    #     super().__init__(*args)
    #     self.degree = -math.inf if len(self) == 0 else len(self) - 1
    def __new__(cls, iterable, /):
        ls = list(iterable)
        while ls and ls[-1] == 0:
            ls.pop()
        poly = super().__new__(cls, ls)
        poly.degree = -math.inf if len(poly) == 0 else len(poly) - 1
        return poly

    @staticmethod
    def __wrap(x: 'Number | Polynomial') -> 'Polynomial':
        if isinstance(x, Number):
            return Polynomial((x,))
        return x
        
    def __call__(self, x):
        s = 0
        for c in reversed(self):
            s = s * x + c
        return s
    
    def __add__(self, other):
        other = self.__wrap(other)
        return Polynomial(a + b for a, b in
            zip_longest(self, other, fillvalue=0))

    def __neg__(self):
        return Polynomial(-c for c in self)
    #
    # def __sub__(self, other):
    #     return self + (-other)
    # def __rsub__(self, other):
    #     return -self + other
    # 
    # def __mul__(self, other):
    #     other = self.__wrap(other)
    #     degree = self.degree + other.degree
    #     coeffs = [0] * (degree + 1)
    #     for i, a in enumerate(self.coeffs):
    #         for j, b in enumerate(other.coeffs):
    #             coeffs[i + j] += a * b
    #     return Polynomial(coeffs)
    #
    # def __pow__(self, n):
    #     if int(n) != n or n < 0:
    #         raise ValueError('Exponent must be a non-negative integer')
    #     if n == 0:
    #         return Polynomial((1,))
    #     return self * self ** (n - 1)
    #
    # def __divmod__(self, divisor):
    #     if self == 0:
    #         return self, self
    #     divisor = self.__wrap(divisor)
    #     if self.degree < divisor.degree:
    #         return Polynomial(), self
    #     power = self.degree - divisor.degree
    #     coefficient = self.coeffs[-1] / divisor.coeffs[-1]
    #     quotient = Polynomial((0,) * power + (coefficient,))
    #     remainder = self - divisor * quotient
    #     d, m = divmod(remainder, divisor)
    #     return quotient + d, m
    #
    # def __floordiv__(self, divisor):
    #     return divmod(self, divisor)[0]
    #
    # def __mod__(self, divisor):
    #     return divmod(self, divisor)[1]
    #
    # def __truediv__(self, divisor):
    #     d, m = divmod(self, divisor)
    #     if m:
    #         raise ValueError(str(divisor) + ' does not divide ' + str(self))
    #     return d
    #
    # def __repr__(self):
    #     return 'Polynomial ' + str(self.coeffs)
    #
    # def __str__(self):
    #     out = ''
    #     for i in range(self.degree, 1, -1):
    #         if self.coeffs[i] == 1:
    #             out += f' + x^{i}'
    #         elif self.coeffs[i] > 0:
    #             out += f' + {self.coeffs[i]}x^{i}'
    #         elif self.coeffs[i] < 0:
    #             # out += ' - ' + str(-self.coeffs[i]) + 'x^' + str(i)
    #             out += f' - {-self.coeffs[i]}x^{i}'
    #     if self.coeffs[1] == 1:
    #         out += ' + x'
    #     elif self.coeffs[1] > 0:
    #         out += f' + {self.coeffs[1]}x'
    #     elif self.coeffs[1] < 0:
    #         out += f' - {-self.coeffs[1]}x'
    #     if self.coeffs[0] > 0:
    #         out += f' + {self.coeffs[0]}'
    #     elif self.coeffs[0] < 0:
    #         out += f' - {-self.coeffs[0]}'
    #     return out.lstrip(' +').lstrip(' -') or '0'
    
    # __radd__ = __add__
    # __rmul__ = __mul__

if __name__ == '__main__':
    p1 = Polynomial((1, 2, 3))
    print(f'{p1=}')
    print(f'{p1(2)=}')

    p2 = Polynomial((2, 1))
    print(f'{p2=}')
    print(f'{p2(2)=}')

    # print(f'{p1 + p2=}')
    # print(f'{p1 - p2=}')
    # print(f'{p1 * p2=}')
    # print(f'{p1 ** 2=}')
    # print(f'{p1 // p2=}')
    # print(f'{p1 % p2=}')
    # print(f'{p1 + 2=}')
    # print(f'{p1 - 2=}')
    # print(f'{p1 * 2=}')
    # print(f'{2 + p1=}')
    # print(f'{2 - p1=}')
    # print(f'{2 * p1=}')
