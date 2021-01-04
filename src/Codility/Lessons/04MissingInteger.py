__author__ = 'RobertaBtt'

class FindMissingElement:

    def solution_simplier(A):
        A.sort()
        N = len(A)

        i = 0
        previous = 0
        while i < N:
            current = A[i]
            if current > 0:
                if current > previous + 1:  # breaks numbers
                    return previous + 1
                else:
                    previous = current
            i += 1

        return max(previous + 1, current + 1)

print(FindMissingElement.solution_simplier([1,2,3,5,6,7,8])) #Expected 4
print(FindMissingElement.solution_simplier([1,2,3])) #Expected 4
print(FindMissingElement.solution_simplier([1, 3, 6, 4, 1, 2])) #expected 5
print(FindMissingElement.solution_simplier([-1, -3])) #Expected 1
print(FindMissingElement.solution_simplier([4, 5, 6, 2])) #Expected 1
print(FindMissingElement.solution_simplier([0]))
print(FindMissingElement.solution_simplier([-10, 10])) # Expected 1
print(FindMissingElement.solution_simplier([-1000000, 1000000])) # Expected 1