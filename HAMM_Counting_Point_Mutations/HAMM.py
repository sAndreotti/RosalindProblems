"""
Counting Point Mutations
url: https://rosalind.info/problems/hamm/

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
"""
import os

dataset = open(os.getcwd()+"/HAMM_Counting_Point_Mutations/rosalind_hamm.txt", "r")
dnas = dataset.readlines()
dh = 0

dnas[0] = dnas[0].replace('/n', '')
dnas[1] = dnas[1].replace('/n', '')

for i in range(len(dnas[0])-1):
    if dnas[0][i:i+1] != dnas[1][i:i+1]:
        dh = dh+1

print(dh)