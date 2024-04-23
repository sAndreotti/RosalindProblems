""""
Complementing a Strand of DNA
url: http://rosalind.info/problems/revc/

Given: A DNA string  of length at most 1000 bp.
Return: The reverse complement sc of s. .
"""
import os

dataset = open(os.getcwd()+"/REVC_Complement_DNA_Strand/rosalind_revc.txt", "r")
dna = dataset.readline().strip()

for i in range(len(dna)):
    if dna[i:i-1] == "A":
        dna[i:i-1] = "T"
    elif dna[i:i-1] == "T":
        dna[i:i-1] = "A"
    elif dna[i:i-1] == "C":
        dna[i:i-1] = "G"
    elif dna[i:i-1] == "G":
        dna[i:i-1] = "C"

reverse = dna[::-1]

print(reverse)