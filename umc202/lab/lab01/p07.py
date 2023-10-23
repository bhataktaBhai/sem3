from p05 import newton

if __name__ == '__main__':
    f = lambda x: x * x
    dx = 1e-6
    dfdx = lambda x: (dx, f(x + dx) - f(x))
    dot = lambda x: (x - 1) * dfdx(x)[0] + f(x) * dfdx(x)[1]
    x = newton(1, dot, 1e-4)
    print((x, f(x)))
    # dist = lambda x: (x - 1) ** 2 + f(x) ** 2
    # dx = 1e-6
    # dv_dist = lambda x: (dist(x + dx) - dist(x)) / dx
    # print(newton(1, dv_dist, 1e-4))
