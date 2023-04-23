#include <iostream>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <cstdbool>
#include <cstdlib>
#include <unistd.h>

#define SIZE 5 // buffer size
bool flag[2] = { false, false };
int turn = 0;

typedef struct queue {
  int data[SIZE];
  int front;
  int rear;
  int size;
} queue;

void producer(queue *buff);
void consumer(queue *buff);

int main() {
  key_t key = 558;
  int shmid = shmget(key, sizeof(queue), 0666 | IPC_CREAT);
  queue *buff = (queue*)shmat(shmid, NULL, 0);
  buff->front = 0;
  buff->rear = 0;
  buff->size = SIZE;
  pid_t n = fork();
  if(n == 0) {
    producer(buff);
  } else if(n > 0) {
    consumer(buff);
  } else {
    perror("[ERROR] Could not fork");
  }
  shmdt(buff);
  shmctl(shmid, IPC_RMID, NULL);
}

void producer(queue *buff) {
  do {
    flag[0] = true;
    turn = 1;
    while(flag[1] == true && turn == 1) {
      ;
    }
    int nextp = rand() % 300;
    while(true) {
      sleep(1);
      while((buff->front + 1) % buff->size == buff->rear) {
        ;
      }
      buff->data[buff->front] = nextp;
      std::cout << "[Log] Data " << nextp << " was produced successfully" << std::endl;
      buff->front = (buff->front + 1) % buff->size;
    }
    flag[0] = false;
  } while(true);
}

void consumer(queue *buff) {
  do {
    flag[1] = true;
    turn = 0;
    while(flag[0] == true && turn == 0) {
      ;
    }
    int nextc = 0;
    while(true) {
      sleep(1);
      while(buff->front == buff->rear) {
        nextc  = buff->data[buff->rear];
        std::cout << "[Log] Data " << nextc << " was consumed successfully" << std::endl;
        buff->rear = (buff->rear + 1) % buff->size;
      }
    }
    flag[1] = false;
  } while(true);
}
