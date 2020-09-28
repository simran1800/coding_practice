###TASK: Calculate the hourglass sum for every hourglass in the array.
 print the maximum hourglass sum.

#!/bin/python3

import math
import os
import random
import re
import sys

# number of hourglass patterns are:(R-2)(C-2)
#R=no of rows
#c=no of columns

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))


def sum_calculate(arr, row, col):
    sum = 0
    sum += arr[row - 1][col - 1]
    sum += arr[row - 1][col]
    sum += arr[row - 1][col + 1]
    sum += arr[row][col]
    sum += arr[row + 1][col - 1]
    sum += arr[row + 1][col]
    sum += arr[row + 1][col + 1]
    # print(sum)
    return sum



largest=-63
for k in range(1,5): #first and last row is not counted
    # print("loooooop")
    for v in range(1,5):
        curr_sum = sum_calculate(arr,k,v)#first and last column is not counted 
        if curr_sum>largest:
            largest=curr_sum
print(largest)
