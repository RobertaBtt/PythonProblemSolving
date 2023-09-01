"""Compute number of integers divisible by k in range [a..b]."""

# Explanations here: https://app.codility.com/demo/results/trainingW92E84-XPZ/
# Results here: https://app.codility.com/demo/results/trainingX3RY3Z-TQU/

def solution(A,B,K):
    if 0 <= A <= 2000000000 and 0 <= B <= 2000000000 and 1 <= K <= 2000000000:
        if A % K == 0:
            return (B - A) // K + 1
        else:
            return (B - (A - A % K)) // K


#Minimal
A, B, K = 0,1,11
print(solution(A,B,K))

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