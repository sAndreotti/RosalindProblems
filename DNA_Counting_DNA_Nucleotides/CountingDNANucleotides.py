"""
Counting DNA Nucleotides
url: http://rosalind.info/problems/dna/

Given: A DNA string  of length at most 1000 nt
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in
"""
import os

dataset = open(os.getcwd()+"/DNA_Counting_DNA_Nucleotides/rosalind_dna.txt", "r")
dna = dataset.readline().strip()

number_a = dna.count("A")
number_c = dna.count("C")
number_g = dna.count("G")
number_t = dna.count("T")

print(f"{number_a} {number_c} {number_g} {number_t}")