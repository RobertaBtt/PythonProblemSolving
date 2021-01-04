"""A non-empty array A consisting of N integers is given.
The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
"""
# https://app.codility.com/demo/results/trainingXVF6NX-6SQ/

#O(N ** 2)
#def badsolution(A):


#https://app.codility.com/demo/results/trainingPK29EJ-8GA/
#O(N)
def solution(A):
    car = 0
    tuples = 0
    for a in A:
        if a == 0:
            car += 1
        else:
            tuples += car
            if tuples > 1000000000:
                return -1
    return tuples

A=[0,1,0,1,1]
print(solution(A))