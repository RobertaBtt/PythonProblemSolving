def prefix_sum(A):
    n = len(A)
    pre_sum = [0] * (n + 1)
    for k in range(1, n + 1):
        pre_sum[k] = pre_sum[k - 1] + A[k - 1]

    return pre_sum


print(prefix_sum([1,3,2,4,3,1,2,1,3,2]))
