__author__ = 'RobertaBtt'

"""Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively.
 The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides 
 contained in the DNA sequence between positions P[K] and Q[K] (inclusive).
 """


# My first attempt
# 100% correct, Performance 0 :(
# https://app.codility.com/demo/results/training5WZKTJ-QM5/

DNA = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

def solution(S, P, Q):

    result = []
    for p in enumerate(P):
        current_index = p[0]

        result.append(min([DNA[i] for i in S[p[1]:Q[current_index] + 1]]))

    return result


# second attempt
# again 62% of validity (Performance is 0)
# https://app.codility.com/demo/results/training5WZKTJ-QM5/
def solution2(S, P, Q):
    result = []

    for r in [ slice(start, end+1) for start,end in zip(P,Q)]:
        result.append(DNA[min(S[r])])

    return result


S = "CAGCCTA"
P = [2, 5, 0]
Q = [4, 5, 6]

solution2(S, P, Q)
