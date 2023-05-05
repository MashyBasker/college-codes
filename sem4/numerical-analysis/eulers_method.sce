function g = f(x, y)
    g = -2*y - x
endfunction

y0 = 1
x0 = 0
xn = 1
h = 0.001
N = (xn - x0) / h


for i = 1:N
    m = f(x0, y0)
    y = y0 + h * m
    x = x0 + h
    printf("x%d: %f\t\ty%d: %f\n", i, x, i, y)
    y0 = y
    x0 = x
end

printf("\nAnswer:\t%f", y)
