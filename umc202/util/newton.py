def newton(f, x0, df=None, target=0, tolerance=1e-6, maxiter=100):
    if df is None:
        df = lambda x: (f(x + tolerance // 2) - f(x - tolerance // 2)) / tolerance
    for _ in range(maxiter):
        x1 = x0 + (target - f(x0)) /df(x0)
        if abs(x1 - x0) < tolerance:
            return x1
        x0 = x1
    return None
