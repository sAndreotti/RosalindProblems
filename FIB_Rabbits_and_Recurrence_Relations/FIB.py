"""
Rabbits and Recurrence Relations
url:http://rosalind.info/problems/fib/

Given: Positive integers  and .
Return: The total number of rabbit pairs that will be present after  months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of  rabbit pairs (instead of only 1 pair).
"""
import os

def fibonacci(n, k):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1, k) + k* fibonacci(n-2, k)

dataset = open(os.getcwd()+"/FIB_Rabbits_and_Recurrence_Relations/rosalind_fib.txt", "r")
n, k = dataset.readline().strip().split(" ")

print(fibonacci(int(n),int(k)))