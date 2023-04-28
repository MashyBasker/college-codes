#include <vector>
#include <iostream>
#include <pthread.h>
#include <stdbool.h>

#define N 3

std::vector<std::vector<int>> A(N, std::vector<int> (N, 0));
std::vector<std::vector<int>> B(N, std::vector<int> (N, 0));
std::vector<std::vector<int>> C(N, std::vector<int> (N, 0));
std::vector<std::vector<int>> D(N, std::vector<int> (N, 0));
std::vector<std::vector<int>> E(N, std::vector<int> (N, 0));

bool isEqualDimension(std::vector<std::vector<int>> A, std::vector<std::vector<int>> B) {
  int rowA = A.size();
  int rowB = B.size();
  int colA = A[0].size();
  int colB = B[0].size();

  return (rowA == rowB) && (colA == colB);
}

void *matrixSum(void *args) {
  if(isEqualDimension(A, B) == false) {
    exit(EXIT_FAILURE);
  }
  int rowC = A.size();
  int colC = B.size();
  for(int i = 0; i < rowC; i++) {
    for(int j = 0; j < colC; j++) {
      C[i][j] = A[i][j] + B[i][j];
    }
  }
  pthread_exit(NULL);
}

void *matrixSubtraction(void *args) {
  if(isEqualDimension(C, D) == false) {
    exit(EXIT_FAILURE);
  }
  int rowC = C.size();
  int colD = D[0].size();
  for(int i = 0; i < rowC; i++) {
    for(int j = 0; j < colD; j++) {
      D[i][j] = A[i][j] - B[i][j];
    }
  }
  pthread_exit(NULL);
}

void matrixMultiplication(std::vector<std::vector<int>> C, std::vector<std::vector<int>> D) {
  int rowC = C.size();
  int colC = C[0].size();
  int rowD = D.size();
  int colD = D[0].size();

  if(colC != rowD) {
    exit(EXIT_FAILURE);
  }
  for(int i = 0; i < rowC; i++) {
    for(int j = 0; j < colD; j++) {
      E[i][j] = 0;
      for(int k = 0; k < rowD; k++) {
        E[i][j] += C[i][k] * D[k][j];
      }
    }
  }
}

void printMatrix(std::vector<std::vector<int>> M) {
  int r = M.size();
  int c = M[0].size();
  for(int i = 0; i < r; i++) {
    for(int j = 0; j < c; j++) {
      std::cout << M[i][j] << " ";
      
    }
    std::cout << std::endl;
  }
  std::cout << std::endl;
}

void getMatrix() {
  std::cout << "Get Matrix A:\n";
  for(int i = 0; i < N; i++) {
    for(int j = 0; j < N; j++) {
      std::cin >> A[i][j];
    }
  }
  std::cout << "Get Matrix B:\n";
  for(int i = 0; i < N; i++) {
    for(int j = 0; j < N; j++) {
      std::cin >> B[i][j];
    }
  }
}

int main() {
  pthread_t th1, th2;
  getMatrix();
  std::cout << std::endl;
  pthread_create(&th1, NULL, matrixSum, NULL);
  pthread_create(&th2, NULL, matrixSubtraction, NULL);

  pthread_join(th1, NULL);
  pthread_join(th2, NULL);

  std::cout << "Matrix C after addition of A and B\n";
  std::cout << "----------------------------------\n";
  printMatrix(C);
  std::cout << "Matrix D after subtration of A and B\n";
  std::cout << "------------------------------------\n";
  printMatrix(D);
  matrixMultiplication(C, D);
  std::cout << "Matrix E after multiplication of C and D\n";
  std::cout << "----------------------------------------\n";
  printMatrix(E);
  
}