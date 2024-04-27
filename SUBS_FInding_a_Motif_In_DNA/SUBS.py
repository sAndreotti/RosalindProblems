"""
Finding a Motif in DNA 
url: http://rosalind.info/problems/subs/

Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
"""
import os

def searching(text, pattern):
    N=len(text)
    M=len(pattern)
 
    phi = [0]*M
    j = 0

    processing(pattern, M, phi)
 
    i = 0
    occurrence=""

    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
 
        if j == M:
            occurrence = occurrence + str(i-j+1) + " "
            j = phi[j-1]
 
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = phi[j-1]
            else:
                i += 1

    print(occurrence)

def processing(pattern, M, phi):
    len = 0
    phi[0]
    i = 1

    while i < M:
        if pattern[i]== pattern[len]:
            len += 1
            phi[i] = len
            i += 1
        else:
            if len != 0:
                len = phi[len-1]
            else:
                phi[i] = 0
                i += 1

data = open(os.getcwd()+"/SUBS_Finding_a_Motif_In_DNA/rosalind_subs.txt", "r")
text, pattern = data.readlines()
searching(text.strip(), pattern.strip())