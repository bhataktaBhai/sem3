def fixed_point_iteration(a, f):
    x = a
    c = 0
    while c < 20:
        x = f(x)
        if abs(x - f(x)) < 1e-2:
            return x
        c += 1

if __name__ == '__main__':
    print(fixed_point_iteration(1, lambda x: x**3 - 3 * x**2 + x - 3))
