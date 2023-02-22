import math

def f(a):
    return 10**a + math.sin(a) + 2*a

a, b, x = -1, 0, 1 
tol = 0.0001

while abs(f(x)) > tol:
    x = (a + b) / 2
    if f(a)*f(x) < 0:
        a = a
        b = x
        print(f"a = {a}\t\tb = {b}\t\tx = {x}")
    elif f(a)*f(x) > 0:
        a = x
        b = b
        print(f"a = {a}\t\tb = {b}\t\tx = {x}")
    elif f(a)*f(x) == 0:
        break


print(f"\n## THE ROOT IS ##\n{x}")




