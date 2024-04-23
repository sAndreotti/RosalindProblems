"""
Transcribing DNA into RNA 
url: http://rosalind.info/problems/rna/

Given: A DNA string  having length at most 1000 nt.
Return: The transcribed RNA string of .
"""
import os

dataset = open(os.getcwd()+"/2_Transcribing_DNA_into_RNA/rosalind_rna.txt", "r")
dna = dataset.readline().strip()

rna = dna.replace("T", "U")
print(rna)