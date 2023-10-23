def newton(x, f, tolerance, iter = 0):
    if iter > 10:
        return None, x
    dfdx = (f(x + tolerance) - f(x)) / tolerance
    x1 = x - f(x) / dfdx
    if abs(x1 - x) < tolerance:
        return x
    return newton(x1, f, tolerance, iter + 1)

if __name__ == '__main__':
    print(newton(1, lambda x: x ** 2 - 2, 0.0001))
