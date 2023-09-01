"""You have an array di interi di dimensione n

   1< =n< = 100000
   [2,3,7,5,1,3,9]

   We have also the start position, for example k=4

   The picker should perform 6 moves.
   We use prefix sum to know the maximum number of mushrooms that can be collected.

"""
"""Lesson Prefix Sum"""
def prefix_sum(A):
    n = len(A)
    P =  [0] * (n+1)
    for k in range(1,n+1):
        P[k] = P[k-1] + A[k-1]
    return P
"""Count the total from position x to position y"""
def count_total(P, x, y):
    return P[y+1] - P[x]

A = [2,3,4,5,4,3,2,3,4]
P = prefix_sum(A)
print(count_total(P, 3, 5))

def mushrooms(A, k, m):
    n = len(A)
    result = 0
    pref = prefix_sum(A)
    for p in range (min(m,k) + 1):
        left_pos = k - p
        right_pos = min (n-1, max(k,k+m-2*p))
        result = max(result, count_total(pref, left_pos, right_pos))

    for p in range(min(m + 1, n-k)):
        right_pos = k + p
        left_pos = max(0, min(k,k-(m-2*p)))
        result = max(result, count_total(pref, left_pos, right_pos))

    return result

B = [2,3,7,5,1,3,9]
print(mushrooms(B, 4, 6))