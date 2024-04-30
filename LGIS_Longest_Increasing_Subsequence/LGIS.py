"""
Longest Increasing Subsequence
url: http://rosalind.info/problems/lgis/

Given: A positive integer n≤10000 followed by a permutation π of length n.
Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
"""

import os

def increasing(pi: list):
    tmp = [int(pi[0])]
    for e in range(1, len(pi)):
        if int(pi[e]) < tmp[len(tmp)-1]:
            tmp.append(int(pi[e]))

    return tmp

with open(os.getcwd()+'/LGIS_Longest_Increasing_Subsequence/rosalind_lgis.txt', 'r') as data:
    n, pi = data.readlines()
n = int(n.strip())
pi = pi.split(' ')
[int(e) for e in pi]
pi_cp = pi

incr_lists = []
m = len(pi_cp)
for i in range(m):
    incr_lists.append(increasing(pi_cp))
    pi_cp.pop(0)

print(incr_lists)