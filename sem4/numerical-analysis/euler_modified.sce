function g = f(x, y)
    g = -2*y - x
endfunction

/* Parameter initialisation */
y0 = 1
x0 = 0
xn = 1
h = 0.001
N = (xn - x0) / h
xk = x0
yk = y0

for i = 1:N
    y = yk + h * f(xk, yk) 
    x = xk + h
    y = y0 + 0.5 * h * [f(x0, y0) + f(x, y)]
    printf("y%d: %f\t\tx%d: %f\n", i, y, i, x)
    yk = y
    xk = x
    
end 
