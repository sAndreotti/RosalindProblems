"""
Finding a Shared Motif
url: http://rosalind.info/problems/lcsm/

Given:  A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""

import os
from Bio import SeqIO

def shortest_seq(seq):
    min_len = 10000
    shortest_seq = ''
    for i in seq.keys():
        if len(seq[i]) < min_len:
            min_len = len(seq[i])
            shortest_seq = seq[i]
    return shortest_seq

records=[]
sequences=[]
sample = []
with open(os.getcwd()+'/LCSM_Finding_a_Shared_Motif/rosalind_lcsm.txt', 'r') as data:
    for line in data.readlines():
        if line.startswith('>') == False:
            if sample != "":
                sample += line.strip()
            else:
                sample = line.strip()
        else:
            records.append(line.strip())
            if sample != "":
                sequences.append(sample)
                sample = ""
    if sample != "":
        sequences.append(sample)

sequences.pop(0)

seq = {records[i]:sequences[i] for i in range(len(sequences))}

s_seq = shortest_seq(seq)
motif = set()
for i in range(len(s_seq)):
    for j in range(i+1,len(s_seq)+1):
        motif.add(s_seq[i:j])
for s in seq.values():
    update_motif = list(motif)
    for m in update_motif:
        if m not in s:
            motif.remove(m)
n = 0
longest_motif = ''
for i in motif:
    if len(i) > n:
        longest_motif = i
        n = len(i)
print(longest_motif)
