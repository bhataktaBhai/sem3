import math

def mul(a, b):
    result = a * b
    print('->', int(math.log2(result)))
    return result

def preasant(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:
        r = preasant(mul(a, a), n // 2)
        return r
    else:
        r = preasant(mul(a, a), n // 2)
        r = mul(r, a)
        return r

def peasant(a, n):
    x = a
    y = 1
    while n > 1:
        if n % 2 == 0:
            x = mul(x, x)
            n //= 2
        else:
            y = mul(y, x)
            x = mul(x, x)
            n //= 2
    return mul(y, x)

def shishir(a, n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = mul(result, a)
        a = mul(a, a)
        n //= 2
    return result

def pringala(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:
        r = pringala(a, n // 2)
        r = mul(r, r)
        return r
    else:
        r = pringala(a, n // 2)
        r = mul(r, r)
        r = mul(r, a)
        return r

def pingala(a, n):
    x = a
    y = 1
    while n > 1:
        if n % 2 == 1:
            y = mul(y, x)
            n -= 1
        while n % 2 == 0:
            x = mul(x, x)
            n //= 2
    return mul(y, x)

def nagasai(a, n):
    if n == 0:
        return 1
    exp = n
    i = 0
    b = a
    if exp % 2 == 1:
        r = b
    else:
        r = 1
    exp //= 2
    while exp > 0:
        i += 1
        b = mul(b, b)
        if exp % 2 == 1:
            r = mul(r, b)
        exp //= 2
    return r

def gupta(a, n):
    def gp2(n):
        result = 1
        while result << 1 <= n:
            result <<= 1
        return result << 1
    # N = n
    if n == 0:
        return 1
    result = 1
    mask = gp2(n)
    while mask > 1:
        # print((result ** (mask << 1)) * (a ** n))
        # print(result ** mask * a ** n == a ** N, n < mask)
        result = mul(result, result)
        mask >>= 1
        if n & mask != 0:
            result = mul(result, a)
            n = n ^ mask
    return result

print("""Which algorithm would you like to use?
(1) Peasant, recursive
(2) Peasant, iterative
(3) Shishir, iterative
(4) Pingala, recursive
(5) Pingala, iterative
(6) NagaSai, peasant, iterative
(7) Gupta, iterative""")
choice = int(input())
print("Enter a number and its power, separated by a space:")
a, n = (int(x) for x in input().split())
funcs = [preasant, peasant, shishir, pringala, pingala, nagasai, gupta]
print(funcs[choice - 1](a, n))
