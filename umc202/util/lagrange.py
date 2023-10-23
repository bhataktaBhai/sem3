from polynomial import Polynomial

def interpolate(points) -> Polynomial:
    """Interpolate a polynomial from the given points."""
    product = Polynomial(1)
    for x, _ in points:
        product *= Polynomial((-x, 1))
    result = Polynomial()
    for x, y in points:
        subproduct = product // Polynomial((-x, 1))
        result += subproduct // subproduct(x) * y
    return result

if __name__ == '__main__':
    points = [(0, 1), (1, 2), (2, 4)]
    print(interpolate(points))
