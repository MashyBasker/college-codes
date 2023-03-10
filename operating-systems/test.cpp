#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> matmul(vector<vector<int>> A, vector<vector<int>> B) {
        // get the dimensions of A and B vectors
        int row_a = A.size();
        int row_b = B.size();
        int col_a = A[0].size();
        int col_b = B[0].size();

        // initialize the vector that will store the matrix product
        vector<vector<int>> product(row_a, vector<int> (col_b, 0));

        // checking dimension compatibility
        if(row_a != col_b) {
            std::cout << "[ERROR] matrices are not compatible\n";
            EXIT_FAILURE;
        }
            // apply naive algorithm for matrix multiplication
        for(int i = 0; i < row_a; i++) {
            for(int j = 0; j < col_b; j++) {
                for(int k = 0; k < col_a; k++) {
                    product[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        return product;
    }
vector<vector<int>> getmatrix() {
        int r, c;
        std::cout << "Row size: ";
        std::cin >> r;
        std::cout << "Column size: ";
        std::cin >> c;
        vector<vector<int>> mat(r, vector<int>(c, 0));
        int val;
        for(int i = 0; i < r; i++) {
            for(int j = 0; j < c; j++) {
                std::cin >> val;
                mat[i][j] = val;
            }
        }
        return mat;
}

int main() {
    vector<vector<int>> s = getmatrix();
    vector<vector<int>> k = getmatrix();
    vector<vector<int>> f = matmul(s, k);

    for(int i = 0; i < s.size(); i++) {
        for(int j = 0; j < s[0].size(); j++) {
            cout << f[i][j] << " ";
        }
        cout << "\n";
    }
}
    