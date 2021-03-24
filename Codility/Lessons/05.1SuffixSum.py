# Sum of the k last values
def suffix_sum(A):
    n = len(A)
    suffix_sum = [0] * (n)
    for k in range(0, n):
        suffix_sum[k] = A[n-1-k]+suffix_sum[k-1]
    return suffix_sum


print(suffix_sum([6,3,2,4,3]))
