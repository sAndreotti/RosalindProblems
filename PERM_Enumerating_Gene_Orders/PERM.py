"""
Enumerating Gene Orders
url: http://rosalind.info/problems/perm/

Given: A positive integer n <= 7.
Return: The total number of permutations of length n, followed by a list of such permutations (in nay order).
"""
import os
import math

def permute(a, l, r): 
    if l == r: 
        print(' '.join(a)) 
    else: 
        for i in range(l, r): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l]  # backtrack 

n = int(open(os.getcwd()+'/PERM_Enumerating_Gene_Orders/rosalind_perm.txt', 'r').readline().strip())
print(math.factorial(n))

perm = []
[perm.append(str(i+1)) for i in range(n)]

permute(perm, 0, n) 