
A = [1, 2, 1, 0; 0, 1, 2, 1; 0, 0, 100, 200; 0, 0, 0.04, 0.03]
B = [1; 4; 800; 0.12]

function [x] = GaussElimination(A, b)
    C = [A b];
    [m, n] = size(A);
    [r, s] = size(b);
    if(m <> r) then
        error("[ERROR]: matrix A and vector b have incompatible sizes");
    end
    
    for k = 1:m-1
        // pivoting step
        [dummy,p] = max(abs(C(k:m,k)));
        p = p+k-1;
        if C(p,k) == 0
            error("[ERROR]: matrix is singular");
        end
        if p <> k then
            C([k,p],:) = C([p,k],:);
        end
        
        // elimination step
        for i = k+1:m
            mult = C(i,k) / C(k,k);
            C(i,k+1:$) = C(i,k+1:$) - mult * C(k,k+1:$);
            C(i,k) = 0;
        end
    end
    
    // back substitution
    x = zeros(m,1);
    x(m) = C(m,n+1) / C(m,m);
    for k = m-1:-1:1
        x(k) = (C(k,n+1) - C(k,k+1:m)*x(k+1:m)) / C(k,k);
    end
    
    disp(x);
endfunction


printf("THE SOLUTION:\n")
GaussElimination(A, B)
