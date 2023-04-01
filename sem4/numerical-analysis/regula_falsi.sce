function y = f(x)
    y = cos(x) - x*(%e^x)
endfunction

printf("a\t\tb\t\tc\t\tf(x)\n")
printf("---------------------------------------------------------\n")

a = 0, b = 1, c = 1
tol = 0.00000001


while abs(f(c)) > tol
    c = (a*f(b) - b*f(a)) / (f(b) - f(a))
    if f(a)*f(c) < 0
        b = c
        printf("%.7f\t%.7f\t%.7f\t%.7f\n", a, b, c, f(c))
    elseif f(a)*f(c) > 0
        a = c
        printf("%.7f\t%.7f\t%.7f\t%.7f\n", a, b, c, f(c))
    elseif f(a)*f(c) == 0
        break
    end
end

printf("\nTHE ROOT OF THE EQUATION IS: %.7f\n", c)
