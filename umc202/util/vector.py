from numbers import Number

class vector(tuple):
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Cannot add vectors of different dimensions")
        return vector(a+b for a,b in zip(self, other))

    def __neg__(self):
        return vector(-a for a in self)
    
    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, other):
        if not isinstance(other, Number):
            raise TypeError("Can only multiply vectors by scalars")
        return vector(a*other for a in self)
    __rmul__ = __mul__

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError("Cannot divide vector by zero")
        return self * (1/other)

    def __bool__(self):
        return any(self)
