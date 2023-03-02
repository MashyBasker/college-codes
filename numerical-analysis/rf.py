import math

def f(x):
    return math.cos(x) - x*(math.e**x)

def regula_falsi(a, b):
    s = (a*f(b) - b*f(a)) / (f(b) - f(a))
    return s 

a = 0
b = 1
c = 1
tol = 0.00000001

while abs(f(c)) > tol:
    c = regula_falsi(a, b)
    if f(a)*f(c) < 0:
        b = c
    elif f(a)*f(c) > 0:
        a = c
    elif f(a)*f(c) == 0:
        break

print("The root is: ", c)

