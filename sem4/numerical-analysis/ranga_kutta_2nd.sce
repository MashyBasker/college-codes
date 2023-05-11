function g = f(y, x)
    g = x * y
endfunction

y0 = 2
x0 = 0
h = 0.2
b = 0.8
N = 4
yn = y0
x = x0

/// Second order Ranga Kutta method

printf("////////// RANGA-KUTTA SECOND ORDER ////////////\n")
for i = 1:N
    k1 = h * f(yn, x)
    k2 = h * f(yn + k1, x + h)
    x0 = x + h
    x = x0
    yn = y0 + 0.5 * (k1 + k2)
    y0 = yn
    printf("[%d] Iteration: %.5f\n", i, yn)
end

printf("Second order Ranga Kutta solution: %.5f", yn)

/// Fourth order Ranga Kutta method

printf("\n\n///////// RANGA KUTTA FOURTH ORDER ////////////\n")
y0 = 2
x0 = 0
h = 0.2
b = 0.8
N = 4
yn = y0
xn = x0

for i = 1:N
    k1 = h * f(yn, xn)
    k2 = h * f(yn + k1/2, xn + h/2)
    k3 = h * f(yn + k2/2, xn + h/2)
    k4 = h * f(yn + k3, xn + h)
    
    yn = y0 +  (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    x0 = xn + h
    xn = x0
    y0 = yn
    printf("[%d] Iteration: %.5f\n", i, yn)
end

printf("Fourth order Ranga Kutta Solution: %.5f", yn)
