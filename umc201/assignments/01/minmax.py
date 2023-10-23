def minmax(A: list[int], B: list[int], C: list[int]) -> int:
    A, B, C = sorted([A, B, C], key=lambda x: x[-1])
    a, b, c = A[-1], B[-1], C[-1]
    w = max(abs(a - b), abs(b - c), abs(c - a))
    if len(A) == len(B) == len(C) == 1:
        return w
    assert a <= b <= c
    if len(C) > 1:
        c1 = C[-2]
        if c1 >= b:
            return minmax(A, B, C[:-1])
        for b in B[::-1]:
            if b <= a:
                break
            w = min(w, max(abs(a - b), abs(b - c), abs(c - a)))
        return min(w, minmax(A, B, C[:-1]))
    else:
        for b in B[::-1]:
            if b <= a:
                break
            w = min(w, max(abs(a - b), abs(b - c), abs(c - a)))
        return w

def minmaxi(A: list[int], B: list[int], C: list[int]) -> int:
    n = len(A)
    p, q, r = n, n, n
    A, B, C = sorted([A, B, C], key=lambda x: x[n-1])
    a, b, c = A[p-1], B[q-1], C[r-1]
    w = max(abs(a - b), abs(b - c), abs(c - a))
    while r > 1:
        r, c1 = r - 1, C[r - 1 - 1]
        if b <= c1:
            w = min(w, max(abs(a - b), abs(b - c), abs(c - a)))
            w = min(w, max(abs(a - b), abs(b - c1), abs(c1 - a)))
        else:
            while q - 1 > 0 and B[q - 1 - 1] > max(a, c1):
                q, b = q - 1, B[q - 1 - 1]
                w = min(w, max(abs(a - b), abs(b - c), abs(c - a)))
            X, Y, Z = sorted([(A, p), (B, q), (C, r)], key=lambda x: x[0][x[1] - 1])
            A, B, C = X[0], Y[0], Z[0]
            p, q, r = X[1], Y[1], Z[1]
        a, b, c = A[p-1], B[q-1], C[r-1]
    while q - 1 > 0 and B[q - 1 - 1] > a:
        q, b = q - 1, B[q - 1 - 1]
        w = min(w, max(abs(a - b), abs(b - c), abs(c - a)))
    return w

def minmaxii(A: list[int], B: list[int], C: list[int]) -> int:
    n = len(A)
    p, q, r = n, n, n
    A, B, C = sorted([A, B, C], key=lambda x: x[n-1])
    a, b, c = A[p-1], B[q-1], C[r-1]
    w = max(abs(a - b), abs(b - c), abs(c - a))
    while r > 1:
        w = min(w, max(abs(a - b), abs(b - c), abs(c - a)))
        r, c = r - 1, C[r - 1 - 1]
        X, Y, Z = sorted([(A, p), (B, q), (C, r)], key=lambda x: x[0][x[1] - 1])
        A, B, C = X[0], Y[0], Z[0]
        p, q, r = X[1], Y[1], Z[1]
        a, b, c = A[p-1], B[q-1], C[r-1]
    w = min(w, max(abs(a - b), abs(b - c), abs(c - a)))
    return w

def certain_minmax(A: list[int], B: list[int], C: list[int]) -> int:
    w = max(abs(A[0] - B[0]), abs(B[0] - C[0]), abs(C[0] - A[0]))
    for a in A:
        for b in B:
            for c in C:
                w = min(w, max(abs(a - b), abs(b - c), abs(c - a)))
    return w

def test():
    from random import choices

    A = sorted(choices(range(10000), k=3))
    B = sorted(choices(range(10000), k=3))
    C = sorted(choices(range(10000), k=3))
    passed = certain_minmax(A, B, C) == minmaxii(A, B, C)
    if not passed:
        print(A, B, C, certain_minmax(A, B, C), minmaxii(A, B, C), sep='\n')
    return passed

if __name__ == '__main__':
    for i in range(100):
        print(i)
        assert test()

