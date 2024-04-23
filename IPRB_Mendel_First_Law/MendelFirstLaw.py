"""
Mendel's First Law
url: http://rosalind.info/problems/iprb/

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""
import os

with open(os.getcwd()+"/IPRB_Mendel_First_Law/rosalind_iprb.txt", "r") as f:
    # m: heterozygous
    # n: homozygous recessive
    # k: homozygous dominant
    k, m, n = map(int, f.readline().strip().split(" "))
    population = k+m+n

    # Good combinations
    i = m*m + 4*n*n + 4*m*n - 4*n-m

    # All combinations
    j = 4*population*(population-1)

    prob = 1-i/j
    print(prob)

