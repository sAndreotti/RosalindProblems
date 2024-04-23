"""
Computing GC Content
url: http://rosalind.info/problems/gc/

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""
import os

dna = []
sample = ""
dataset = open(os.getcwd()+"/5_Computing_GC_Content/rosalind_gc.txt", "r")
trimmered = open(os.getcwd()+"/5_Computing_GC_Content/rosalind.txt", "w")
for line in dataset.readlines():
    if line[:1] == ">":
        if sample != "":
            sample = sample
            dna.append(sample)
            dna.append("\n")
        dna.append(line)
        sample = ""
    else:
        sample = sample + line[:-1]

if sample != "":
    sample = sample
    dna.append(sample)

trimmered.writelines(dna)
trimmered.close()
dataset.close()

dataset = open(os.getcwd()+"/Computing_GC_Content/rosalind.txt", "r")
samples = {}
sample = ""
for line in dataset.readlines():
    if line[:1] == ">":
        sample = line[1:-1]
    else:
        line.replace('\n', '')
        average = ((line.count("G")+line.count("C"))/(len(line)-1))*100
        samples[sample] = average

id = ""
max = 0
for sample in samples:
    if samples[sample] > max:
        max = samples[sample]
        id = sample

print(id)
print(max)