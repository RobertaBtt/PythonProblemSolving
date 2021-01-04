__author__ = 'RobertaBtt'

import functools
import collections

# def sockMerchant(n, ar):
#     counter = collections.Counter(ar)
#     return counter
import math

#Write a function that, given a string S of legth N and an integer K,
#returns the shortest possible length of the compressed representation of S
# after removing exactly K consecutive characters from S
# N is in the range 1, 100000
# K is in the range 0,100000
# K <= N
#string S consists only of uppercase letters.
import re

class CompressString:
    def solution(S,K):
        size = len(S)
        counters = collections.Counter(S)
        consecutives = (re.findall(r'((\w)\2{2,})', S))
        counters.most_common()

        for consecutive in consecutives:
            str.find(consecutive[0])

            print(consecutive[1])
        # for n in range(size):
        #     current_letter = S[n]
        #     #Avoid to to out of index
        #     if n <= size -3:
        #         #This is not triple to eliminate
        #         if not(S[n] == S[n+1] == S[n+2]):
        #             print(S[n]+S[n+1]+S[n+2])
        #
        #     current_letter = S[n]
        #     print(current_letter)
        #
        print("")

S = "ABBBCCDDCCC"
print(CompressString.solution(S,3))

S = "AAAAAABXXAAA"
print(CompressString.solution(S,3))