#!/usr/bin/python3


################# SMALLER CODE #####################
import random

def quickselect(arr, k):
    """
    Find the k-th smallest element in the array (0-indexed).
    """
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)

    # Partition array into three parts
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)  # k-th smallest is in the lows
    elif k < len(lows) + len(pivots):
        return pivots[0]  # k-th smallest is a pivot element
    else:
        # k-th smallest is in the highs
        return quickselect(highs, k - len(lows) - len(pivots))
#####################################################


from typing import List
import random

def partition(lst: List[int], left: int, right: int, pivotIndex: int) -> int:
    pivotValue = lst[pivotIndex]
    swap(lst, pivotIndex, right)
    storeIndex = left
    for i in range(left, right):
        if lst[i] < pivotValue:
            swap(lst, storeIndex, i)
            storeIndex += 1
    swap(lst, right, storeIndex)
    return storeIndex

def swap(lst: List, first: int, second: int):
    temp = lst[first]
    lst[first] = lst[second]
    lst[second] = temp

def select(lst: List[int], left: int, right: int, k: int):
    if left == right:
        return lst[left]
    pivotIndex = random.randint(left, right)
    pivotIndex = partition(lst, left, right, pivotIndex)
    if k == pivotIndex:
        return lst[k]
    elif k < pivotIndex:
        return select(lst, left, pivotIndex - 1, k)
    else:
        return select(lst, pivotIndex + 1, right, k)

def median(lst: List) -> int:
    N = len(lst)
    if N % 2 == 1:
        return select(lst, 0, N-1, N//2)
    else:
        mid1 = select(lst, 0, N-1, N//2)
        mid2 = select(lst, 0, N-1, N//2 - 1)
        return (mid1 + mid2) // 2

if __name__ == "__main__":
    arr = [ 10, 4, 5, 8, 6, 11, 26 ]
    k = 3
    n = len(arr)
    print(f"{k}-th smallest element is: {select(arr, 0, n - 1, k - 1)}")



