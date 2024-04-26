"""
Locating Restricitoin Sites
url: http://rosalind.info/problems/revp/

Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and lenght of every reverse palindrome in the string having length between 4 and 12.
"""
import os

def reverse_complement(dna):
    ret = ""
    for i in dna[::-1]:
        if i=="A":
            ret += "T"
        elif i=="T":
            ret += "A"
        elif i=="C":
            ret += "G"
        elif i=="G":
            ret += "C"

    return ret

with open(os.getcwd()+"/REVP_Locating_Restriction_Sites/rosalind_revp.txt", "r") as data:
    lines = data.readlines()
    dna = ""
    if len(lines)>2:
        for line in lines:
            if line.startswith('>') == False:
                if line.endswith('\n'):
                    line = line[:-1]
                dna = dna + line

    else:
        if lines[1].endswith('\n'):
            dna = lines[1][:-1]
        else:
            dna = lines[1]

tup = [0, 0]
for i in range(len(dna)):
    for j in range(4, 13):
        if i+j <= len(dna):
            if dna[i:i+j] == reverse_complement(dna[i:i+j]):
                print(i+1,j)



