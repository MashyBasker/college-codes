#include <sys/types.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <utmp.h>
#include <sys/shm.h>
#include <stdio.h>
#include <iostream>
#include <unistd.h>
#include <vector>
#include <algorithm>

int arr[6] = {2, 1, 6, 8, 9, 0};
int brr[6] = {2, 1, 6, 8, 9, 0};

struct arguments
{
  int start;
  int end;
};


void merge(int arr[], int l, int m, int r)
{
  auto lindex = m - l + 1;
  auto rindex = r - m;

  // Create temp arraysctor <
  auto *leftArray = new int[lindex],
       *rightArray = new int[rindex];

  // Copy data to temp arrays leftArray[] and rightArray[]
  for (auto i = 0; i < lindex; i++)
    leftArray[i] = arr[l + i];
  for (auto j = 0; j < rindex; j++)
    rightArray[j] = arr[m + 1 + j];

  auto indexOfSubArrayOne = 0,   // Initial index of first sub-array
      indexOfSubArrayTwo = 0;    // Initial index of second sub-array
  int indexOfMergedArray = l; // Initial index of merged array

  // Merge the temp arrays back into array[left..right]
  while (indexOfSubArrayOne < lindex && indexOfSubArrayTwo < rindex)
  {
    if (leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo])
    {
      arr[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
      indexOfSubArrayOne++;
    }
    else
    {
      arr[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
      indexOfSubArrayTwo++;
    }
    indexOfMergedArray++;
  }
  // Copy the remaining elements of
  // left[], if there are any
  while (indexOfSubArrayOne < lindex)
  {
    arr[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
    indexOfSubArrayOne++;
    indexOfMergedArray++;
  }
  // Copy the remaining elements of
  // right[], if there are any
  while (indexOfSubArrayTwo < rindex)
  {
    arr[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
    indexOfSubArrayTwo++;
    indexOfMergedArray++;
  }
}

// begin is for left index and end is
// right index of the sub-array
// of arr to be sorted */
void mergeSort(int array[], int start, int end)
{
  if (start >= end)
    return; // Returns recursively

  auto mid = start + (end - start) / 2;
  mergeSort(array, start, mid);
  mergeSort(array, mid + 1, end);
  merge(array, start, mid, end);
}

void *sort_thread(void *args)
{
  struct arguments *a = (struct arguments *)(args);
  int start = a->start;
  int end = a->end;
  mergeSort(arr, start, end);
  pthread_exit(NULL);
}

int main()
{
  pthread_t th1, th2, th3;
  struct arguments a1, a2;
  a1.start = 0, a1.end = 2;
  a2.start = 3, a2.end = 5;

  if (pthread_create(&th1, NULL, sort_thread, &a1) != 0)
  {
    perror("Thread 1 creation error");
    exit(1);
  }

  if (pthread_create(&th2, NULL, sort_thread, &a2) != 0)
  {
    perror("Thread 2 creation error");
    exit(1);
  }

  pthread_join(th1, NULL);
  pthread_join(th2, NULL);
  struct arguments a3;
  a3.start=0, a3.end=5;

  if (pthread_create(&th3, NULL, sort_thread, &a3) != 0)
  {
    perror("Thread 2 creation error");
    exit(1);
  }
  pthread_join(th3, NULL);
  std::cout<<"Initial Unsorted Array\n";
//   printArray(arrayB, 6);
  for(int i = 0; i < 6; i++) {
    std::cout << brr[i] << " ";
  }
  std::cout << "\n";
  std::cout<<"\nFinal Sorted Array\n";
//   printArray(
  for(int i = 0; i < 6; i++) {
    std::cout << arr[i] << " ";
  }
  std::cout<<std::endl;

  return 0;

}