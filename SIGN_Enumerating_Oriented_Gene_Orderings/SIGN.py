"""
Enumerating Oriented Gene Orderings
url: http://rosalind.info/problems/sign/

Given: A positive integer n<=6.
Return: The total number of signed permutation of length n, followed by a list of all such permutations (you may list the signed permutations in any order).

Note: The output is given in the form of file 'out.txt' because listing all the permutations is too long for the output terminal.
"""
import os

def permutation(lst):
    l = []

    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]

        if int(m)>0:
            remLst.remove('-'+m)
        else:
            remLst.remove(m[1:])

        if len(remLst):
            for p in permutation(remLst):
                l.append([m] + p)
        else:
            l.append([m])

    return l

n = int(open(os.getcwd()+'/SIGN_Enumerating_Oriented_Gene_Orderings/rosalind_sign.txt', 'r').readline().strip())

perm = []
[perm.append(str(i+1)) for i in range(n)]
[perm.append('-'+str(i+1)) for i in range(n)]
out = open(os.getcwd()+'/SIGN_Enumerating_Oriented_Gene_Orderings/out.txt', 'w')

allPerm = permutation(perm)
out.write(str(len(allPerm))+'\n')
for p in allPerm:
    out.write(' '.join(p)+'\n')
out.close()
