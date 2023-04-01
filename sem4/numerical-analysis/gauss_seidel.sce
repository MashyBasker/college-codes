function isDiag = isDiagonal(A)
    isDiag = 1;
    for i = 1:size(A, 1)
        D = abs(A(i, i));
        S = sum(abs(A(i, :))) - D;
        if D <= S
            isDiag = 0;
            break;
        end
    end
endfunction

function x = gauss_seidel(A, b, x0, tol, maxiter)
    // initialize variables
    n = size(A, 1);
    x = x0;
    iter = 0;
    err = tol + 1;

    // loop until convergence or maximum number of iterations is reached
    while iter < maxiter & err > tol
        x_old = x;
        for i = 1:n
            sigma1 = 0;
            sigma2 = 0;
            for j = 1:i-1
                sigma1 = sigma1 + A(i, j) * x(j);
            end
            for j = i+1:n
                sigma2 = sigma2 + A(i, j) * x_old(j);
            end
            x(i) = (b(i) - sigma1 - sigma2) / A(i, i);
        end
        iter = iter + 1;
        err = norm(x - x_old) / norm(x);

        // display current iteration and error
        printf("Iteration: %d\n", iter);
        printf("Error: %f\n", err);
    end
    printf("SOLUTION\n")
    disp(x)
endfunction

printf("Provide matrix A: ")
A = input("");
printf("Provide vector b")
b = input("");
printf("Provide initial value: ")
x0 = input("");
tol = 1e-6;
maxiter = 100;
isDiag = isDiagonal(A);

if isDiag == 1 then
    x = gauss_seidel(A, b, x0, tol, maxiter);
else
    disp("Not a diagonal matrix");
end
