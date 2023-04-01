function y = f(x)
    y = cos(x) - x*(%e^x)
endfunction

function y = g(x)
    y = -sin(x) - %e^x - x*(%e^x)
endfunction

a = 0, b = 1
tol = 0.00000001

printf("a\t\tb\t\tf(a)\t\tf(a)\n")
while abs(f(a)) > tol
    printf("%.7f\t%.7f\t%.7f\t%.7f\n", a, b, f(a), g(a))
    b = a - (f(a) / g(a))
    a = b
end
printf("\nTHE ROOT IS: %.7f\n", b)
