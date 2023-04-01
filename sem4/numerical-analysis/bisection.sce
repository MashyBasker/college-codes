function y = f(x)
    y = cos(x) - x*(%e ^ x)
endfunction

a = 0, b = 1, x = 1
tol = 0.000001

printf("a\t\tb\t\tx\t\tf(x)\n")

while abs(f(x)) > tol
    x = (a + b) / 2
    if f(a)*f(x) < 0
        a = a
        b = x
        printf("%.7f\t%.7f\t%.7f\t%.7f\n", a, b, x, f(x))
    elseif f(a)*f(x) > 0
        a = x
        b = b
        printf("%.7f\t%.7f\t%.7f\t%.7f\n", a, b, x, f(x))
    elseif f(x)*f(a) == 0
        break
    end 
end
