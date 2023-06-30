#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    c=0
    for i in range(len(a)):
        
        for y in range(len(a)-1):
            if(a[y]>a[y+1]):
                a[y],a[y+1]=a[y+1],a[y]
                c+=1
    print(f"Array is sorted in {c} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
