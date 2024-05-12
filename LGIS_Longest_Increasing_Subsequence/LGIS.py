"""
Longest Increasing Subsequence
url: http://rosalind.info/problems/lgis/

Given: A positive integer n≤10000 followed by a permutation π of length n.
Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
"""

import os
def lis(arr):
    n = len(arr)

    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = [1]*n

    prev = [0]*n
    for i in range(0, n):
        prev[i] = i

    # Compute optimized LIS values in bottom up manner
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1:
                lis[i] = lis[j]+1
                prev[i] = j

    # Initialize maximum to 0 to get the maximum of all
    # LIS
    maximum = 0
    idx = 0

    # Pick maximum of all LIS values
    for i in range(n):
        if maximum < lis[i]:
            maximum = lis[i]
            idx = i

    seq = [arr[idx]]
    while idx != prev[idx]:
        idx = prev[idx]
        seq.append(arr[idx])

    return (maximum, reversed(seq))


def lds(arr):
    n = len(arr)

    # Declare the list (array) for LDS and initialize LDS
    # values for all indexes
    lis = [1]*n

    prev = [0]*n
    for i in range(0, n):
        prev[i] = i

    # Compute optimized LDS values in bottom up manner
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] < arr[j] and lis[i]< lis[j] + 1:
                lis[i] = lis[j]+1
                prev[i] = j

    # Initialize maximum to 0 to get the maximum of all
    # LIS
    maximum = 0
    idx = 0

    # Pick maximum of all LDS values
    for i in range(n):
        if maximum < lis[i]:
            maximum = lis[i]
            idx = i

    seq = [arr[idx]]
    while idx != prev[idx]:
        idx = prev[idx]
        seq.append(arr[idx])

    return (maximum, reversed(seq))

with open(os.getcwd()+'/LGIS_Longest_Increasing_Subsequence/rosalind_lgis.txt', 'r') as data:
   n, pi = data.readlines()
n = int(n.strip())
arr = pi.split(' ')
pi = list(map(int, arr))

ans = lis(pi)
print (" ".join(str(x) for x in ans[1]))

print()

ans = lds(pi)
print (" ".join(str(x) for x in ans[1]))

