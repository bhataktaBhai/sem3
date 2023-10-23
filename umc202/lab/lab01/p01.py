def bisect(a, b, f, tolerance):
    if abs(a - b) < tolerance:
        return a
    c = (a + b) / 2
    if f(c) == 0:
        return c
    if f(c) * f(a) < 0:
        return bisect(a, c, f, tolerance)
    else:
        return bisect(c, b, f, tolerance)

if __name__ == '__main__':
    print(bisect(0, 1, lambda x: x**3 - 7 * x**2 + 14 * x - 6, 1e-4))
