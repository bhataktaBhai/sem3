# Find the smallest exponent of a number that begins with a number of your choice. The output would be the exponent value.
import math
print("This program is meant to find the smallest exponent of a number that begins with a number of your choice.")
k = int(input("Choose the starting digits: "))
l = int(input("Choose the digit to give the exponent of : "))
if l != 1:
    a = k
    b = k + 1
    while math.floor(math.log(a, l) + 1) != math.floor(math.log(b, l)):
        a = 10 * a
        b = 10 * b
    print(math.floor(math.log(a, l)) + 1)
elif k != 1:
    print("Impossible.")
else:
    print(1)
