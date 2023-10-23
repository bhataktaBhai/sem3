def newton(x, f, tolerance=1e-6, iter=0):
    if iter > 100:
        return None, (x,)
    dfdx = (f(x + tolerance) - f(x)) / tolerance
    x1 = x - f(x) / dfdx
    if abs(x1 - x) < tolerance:
        return x, (x,)
    solution, path = newton(x1, f, tolerance, iter + 1)
    return solution, (x,) + path

if __name__ == '__main__':
    def f(x):
        return x ** (2 / 3) if x >= 0 else - (-x) ** (2 / 3)
    print(newton(float(input('Initial guess? ')), f))

"""
p |-> p  - 3/2 p = - 1/2 p
p[n+1] - p = p[n+1]
p[n] - p = p[n]
p[n+1] / p[n] = - 1/2
=> Order of convergence is 1
"""
