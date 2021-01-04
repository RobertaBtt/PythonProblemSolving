__author__ = 'RobertaBtt'

class TestPrefixSum:
    def prefix_sums(A):
        n = len(A)

        # Builds the Array of dimension n+1
        P = [0] * (n + 1)

        for k in range(1, n + 1):
            P[k] = P[k - 1] + A[k - 1]
        return P


    def count_total(P, x, y):
        return P[y + 1] - P[x]

print(TestPrefixSum.prefix_sums([1,2,2,1,2,3,4,5,4,3,4,5]))

print(TestPrefixSum.count_total(TestPrefixSum.prefix_sums([1,2,2,1,2,3,4,5,4,3,4,5]), 3, 6))