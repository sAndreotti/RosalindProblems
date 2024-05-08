"""
Longest Increasing Subsequence
url: http://rosalind.info/problems/lgis/

Given: A positive integer n≤10000 followed by a permutation π of length n.
Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
"""

import os

def LIS(nums, n):
    dp = [] 
    dp_list = [] 

    for i in range(n):
        dp.append(1)
        dp_list.append([nums[i]])
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                if len(dp_list[i]) <= len(dp_list[j]):
                    dp_list[i] = dp_list[j] + [nums[i]]
    print(' '.join(dp_list[dp.index(max(dp))]))
    return dp, dp_list

# Longest Decreasing Subsequence
def LDS(nums, n):
    dp = []
    dp_list = []

    for i in range(n):
        dp.append(1)
        dp_list.append([nums[i]])
        for j in range(i):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                if len(dp_list[i]) <= len(dp_list[j]):
                    dp_list[i] = dp_list[j] + [nums[i]]
    print(' '.join(dp_list[dp.index(max(dp))]))
    return dp, dp_list

with open(os.getcwd()+'/LGIS_Longest_Increasing_Subsequence/rosalind_lgis.txt', 'r') as data:
    n, pi = data.readlines()
n = int(n.strip())
pi = pi.split(' ')
[int(e) for e in pi]

len_min, least_increment = LIS(pi, n)
len_max, max_increment = LDS(pi, n)

out = open(os.getcwd()+'/LGIS_Longest_Increasing_Subsequence/out.txt', 'w')

out.write(' '.join(least_increment[len_min.index(max(len_min))]))
out.write('\n')
out.write(' '.join(max_increment[len_max.index(max(len_max))]))

out.close()
