"""Compute number of integers divisible by k in range [a..b]."""

import math

def solution(A,B,K):
    div = 0
    if 0 <= A <= 2000000000 and 0 <= B <= 2000000000 and 1 <= K <= 2000000000:
        if A <= B:
            total_numbers = (B - A) +1

            if total_numbers %K == 0:
                div = total_numbers / K
            else:
                div = math.ceil(total_numbers / K)


    if div == 0:
        return 1

    return int(div)

A,B,K = 6,11,2 #Expected 3
print(solution(A,B,K))

A,B,K = 11,345,17 #Expected 20
print(solution(A,B,K))

A,B,K = 0,0,11 #Expected 1
print(solution(A,B,K))

A,B,K = 10,10,5 #Expected 1
print(solution(A,B,K))

A,B,K = 10,10,7 #Expected 1
print(solution(A,B,K))

A,B,K = 10,10,20 #Expected 1
print(solution(A,B,K))

print(solution(A,B,K))