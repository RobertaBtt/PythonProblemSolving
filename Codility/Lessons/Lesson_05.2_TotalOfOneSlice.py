# Total of one Slice
def prefix_sum(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]

    return P

def count_total(A, x, y):
    P = prefix_sum(A)
    return P[y+1] - P[x]


print(count_total([6,3,2,4,3], 2,3)) #6
print(count_total([6,3,2,4,3], 0,4)) #18
