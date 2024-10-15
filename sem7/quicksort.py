#!/usr/bin/env python

from quickselect import median, swap
from typing import List
import random
import time
import sys

sys.setrecursionlimit(100000)

def partition_basic(A: List[int], lo: int, hi: int) -> int:
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] <= pivot:
            swap(A, i, j)
            i += 1
    swap(A, i, hi)
    return i

def partition_median(A: List[int], lo: int, hi: int) -> int:
    pivot = median(A)
    i = lo
    for j in range(lo, hi):
        if A[j] <= pivot:
            swap(A, i, j)
            i += 1
    swap(A, i, hi)
    return i

def qs_basic(A: List[int], lo: int, hi: int):
    if lo >= hi  or lo < 0:
        return
    p = partition_basic(A, lo, hi)
    qs_basic(A, lo, p - 1)
    qs_basic(A, p+1, hi)

def qs_median(A: List[int], lo: int, hi: int):
    if lo >= hi  or lo < 0:
        return
    p = partition_median(A, lo, hi)
    qs_median(A, lo, p - 1)
    qs_median(A, p+1, hi)


def benchmark_sorting_function(sort_func, size, num_trials=1):
    total_time = 0
    for _ in range(num_trials):
        arr = [random.randint(0, 1000000) for _ in range(size)]  # Generate random list
        start_time = time.time()  # Start timing
        sort_func(arr, 0, size-1)  # Sort the array using the provided function
        end_time = time.time()  # End timing
        total_time += (end_time - start_time)
    
    avg_time = total_time / num_trials
    return avg_time

# Function to compare two sorting functions on multiple array sizes
def compare_sorting_functions(func1, func2, sizes, num_trials=1):
    for size in sizes:
        time_func1 = benchmark_sorting_function(func1, size, num_trials)
        time_func2 = benchmark_sorting_function(func2, size, num_trials)
        print(f"Array size: {size}, {func1.__name__}: {time_func1:.6f} seconds, {func2.__name__}: {time_func2:.6f} seconds")


if __name__ == "__main__":
    #sizes = [1000, 5000, 10000, 20000, 50000, 100000]
    sizes = [20000]
    compare_sorting_functions(qs_basic, qs_median, sizes)

