__author__ = 'RobertaBtt'

"""An array A consisting of N different integers is given. 
The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
Your goal is to find that missing element.

Write a function:

    def solution(A)

that, given an array A, returns the value of the missing element.
"""

"""Here we are using the solution of Gauss for the triangular numbers.

(1/2) * (n+1) * n

that is

n * (n+1)
----------
    2
 
Example of the beans: 101*100 = 10.100
Only one triagle has the half of these beans
10.100 / 2 = 5050

 """
class PermMissingElem:

    def solution(A):

        n = len(A)+1
        result = n * (n + 1)//2

        return result - sum(A)


print(PermMissingElem.solution([1,2,4,5,6,7,8]))
print(PermMissingElem.solution([2,3,1,5]))
