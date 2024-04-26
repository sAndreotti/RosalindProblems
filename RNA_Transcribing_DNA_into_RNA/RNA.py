"""
Transcribing DNA into RNA 
url: http://rosalind.info/problems/rna/

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""
import os

dataset = open(os.getcwd()+"/RNA_Transcribing_DNA_into_RNA/rosalind_rna.txt", "r")
dna = dataset.readline().strip()

rna = dna.replace("T", "U")
print(rna)