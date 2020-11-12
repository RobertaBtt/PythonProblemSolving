# This is a demo task.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

class PigeonHoleProblem:
    # Pigeon hole Problem:
    # Find the missing number, in this case the "smallest" missing number.
    def solution(A):

        if 1 <= len(A) <= 100000:
            m = max(A)
            if m < 1:
                return 1
            A = set(A)
            n = len(A) + 1
            result = n * (n + 1) // 2

            return result - sum(A)
        else:
            return None

    def solutionB(A):
        a = frozenset(sorted(A))
        m = max(a)
        if m > 0:
            for i in range(1, m):
                if i not in a:
                    return i
            else:
                return m + 1
        else:
            return 1

print(PigeonHoleProblem.solution(([1, 3, 6, 4, 1, 2])))
print(PigeonHoleProblem.solution(([1, 2, 3])))
print(PigeonHoleProblem.solution(([-1, -3])))
print(PigeonHoleProblem.solutionB([4, 5, 6, 2]))
print(PigeonHoleProblem.solution([3, 4, 6]))
print(PigeonHoleProblem.solution([-10, -3]))
print(PigeonHoleProblem.solution([-2, 1]))
print(PigeonHoleProblem.solution([2]))
print(PigeonHoleProblem.solution([1]))
print(PigeonHoleProblem.solution([1,2,4]))
print(PigeonHoleProblem.solution([1,2,3]))

'''
[1, 3, 6, 4, 1, 2]
[1, 2, 3]
[-1, -3]
[4, 5, 6, 2, 3]
[3, 4, 6]
[-10, -3]
[-2, 1]
[2]
[1]
[1,2,4]
[1,2,3]'''