function isDiag = checkDiagonal(A)
    isDiag = 1
    for i = 1:size(A, 1)
        D = abs(A(i, i))
        S = sum(abs(A(i, :))) - D
        if D <= S
            isDiag = 0
            break
        end
    end
endfunction

function x = gauss_jacobi(A, b, x0, tol, maxiter)
    // initialize variables
    n = size(A, 1);
    x = x0;
    iter = 0;
    err = tol + 1;

    // loop until convergence or maximum number of iterations is reached
    while iter < maxiter & err > tol
        x_old = x;
        for i = 1:n
            sigma = 0;
            for j = 1:n
                if j ~= i
                    sigma = sigma + A(i, j) * x_old(j);
                end
            end
            x(i) = (b(i) - sigma) / A(i, i);
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

printf("Provide matrix A:")
A = input("")
printf("Provide the matrix b")
b = input("")
printf("Provide initial value: ")
x0 = input("")
tol = 1e-6
maxiter = 100
isDiag = checkDiagonal(A)

if isDiag == 1 then
    gauss_jacobi(A, b, x0, tol, maxiter)
else
    printf("Not a diagonal matrix\n")
end


