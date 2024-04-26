"""
Translating RNA into Protein 
url: http://rosalind.info/problems/prot/

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
"""
import os

codon_table = {"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V",
               "UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V",
               "UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V",
               "UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V",
               "UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A",
               "UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
               "UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
               "UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
               "UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D",
               "UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
               "UAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E",
               "UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E",
               "UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G",
               "UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
               "UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G",
               "UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"}

data = open(os.getcwd()+"/PROT_Translating_RNA_To_Protein/rosalind_prot.txt", "r")
rna = data.readline().strip()

proteins = [rna[i:i+3] for i in range(0, len(rna), 3)]
final_protein=""
for protein in proteins:
    if codon_table[protein] != "Stop":
        final_protein = final_protein + codon_table[protein]
    else:
        break

print(final_protein)