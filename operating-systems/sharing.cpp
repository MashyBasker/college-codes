#include <unistd.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <iostream>

#define SHM_SIZE 1024


int main() {

    int shmid;
    int *shm_ptr;
    key_t key = ftok(".", 'z');

    if (key < 0) {
        perror("ftok error");
        exit(1);
    }

    int n = 3; // setting the matrix sizes
    int ele = 1; // temp variable to store elements in the matrices

    // create the child process
    pid_t pid = fork();

    if (pid < 0) {
        perror("fork error");
        exit(1);
    }

    if (pid == 0) { // child process Q

        sleep(2); // waiting 2 sec for parent to write matrix A in shm 

        shmid = shmget(key, SHM_SIZE, 0666);
        if (shmid < 0) {
            perror("shmget error");
            exit(1);
        }

        shm_ptr = (int*) shmat(shmid, NULL, 0);

        if (shm_ptr == (int*) -1) {
            perror("shmat error");
            exit(1);
        }

        // read the matrix A from shared memory
        int A_r[n][n];
        int *A_ptr = shm_ptr;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A_r[i][j] = A_ptr[i * n + j];
            }
        }

        // write the matrix B to shared memory
        int B[n][n];
        int *B_ptr = shm_ptr + (n*n);
        ele = 2;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                B[i][j] = ele;
                ele = ele++;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                B_ptr[i * n + j] = B[i][j];
            }
        }

        // compute D = B x A_r
        int D[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                D[i][j] = 0;
                for (int k = 0; k < n; k++) {
                    D[i][j] += B[i][k] * A_r[k][j];
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                std::cout << A_r[i][j] << "\t";
            }
            std::cout << "\n";
        }

        std::cout << "\nD = B x A_r:\n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                std::cout << D[i][j] << "\t";
            }
            std::cout << "\n";
        }

        // detach from shared memory
        shmdt(shm_ptr);
    }
    else { // parent process P

        shmid = shmget(key, SHM_SIZE, 0666 | IPC_CREAT);
        if (shmid < 0) {
            perror("shmget error");
            exit(1);
        }

        shm_ptr = (int*) shmat(shmid, NULL, 0);

        if (shm_ptr == (int*) -1) {
            perror("shmat error");
            exit(1);
        }

        // create and write the matrix A to shared memory
        int A[n][n];
        int *A_ptr = shm_ptr;
        ele = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
               A[i][j] = ele;
               ele = ele++;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
               A_ptr[i * n + j] = A[i][j];
            }
        }

        // wait for child process to finish
        wait(NULL);

        // read the matrix B from shared memory
        int B_r[n][n];
        int *B_ptr = shm_ptr + (n*n);  // n*n for matrix A's size
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                B_r[i][j] = B_ptr[i * n + j];
            }
        }

        // compute C = A x B_r
        int C[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                C[i][j] = 0;
                for (int k = 0; k < n; k++) {
                    C[i][j] += A[i][k] * B_r[k][j];
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                std::cout << B_r[i][j] << "\t";
            }
            std::cout << "\n";
        }

        std::cout << "C = A x B_r:\n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                std::cout << C[i][j] << "\t";
            }
            std::cout << "\n";
        }

        // detach from shared memory
        shmdt(shm_ptr);

        // destroy shared memory
        shmctl(shmid, IPC_RMID, NULL);
    }

    return 0;
}