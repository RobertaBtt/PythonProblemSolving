
class TestSwapElement:

    def slow_solution(A, B):
        n = len(A)
        sum_a = sum(A)
        sum_b = sum(B)
        for i in range(n):
            for j in range(n):
                change = B[j] - A[i]
                sum_a += change
                sum_b -= change
                if sum_a == sum_b:
                    return True
                sum_a -= change
                sum_b += change
        return False



#4.3: Swap the elements — O(n + m).
    def fast_solution(A, B, m):
        n = len(A)
        sum_a = sum(A)
        sum_b = sum(B)
        d = sum_b - sum_a
        if d % 2 == 1:
            return False
        d //= 2
        count = list.count(A, m)
        for i in range(n):
            if 0 <= B[i] - d and B[i] - d <= m and count[B[i] - d] > 0:
                return True
        return False


#TestSwapElement.slow_solution([1,2,3], [3,2,2])

TestSwapElement.fast_solution([1,2,5,0], [3,2,4,1], 3)