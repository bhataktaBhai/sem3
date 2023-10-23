import math

def next_p(p, f):
    dx = 1e-4
    dfdx = (f(p+dx) - f(p)) / dx
    return p - f(p)/dfdx

if __name__ == '__main__':
    f = lambda x: -x**3 - math.cos(x)
    print(next_p(next_p(-1, f), f))

"""An initial guess of p0 = 0 cannot be used, since the derivative of f is zero at this point,
and there will be a large jump."""
