__author__ = 'RobertaBtt'

#Problem: You are given an integer n.
# Count the total of 1+2+ ... + n.

from timeit import default_timer as timer

class GaussSum:
    def count_total(n):
        total = 0

        for i in range(n, 0, -1):
            total +=i

        return total

    def model_solution(n):

        result = n * (n + 1)//2

        return result

start = timer()
print("FIRST", GaussSum.count_total(100))
end = timer()
print((end - start)*100)# Time in seconds, e.g. 5.3809195

start = timer()
print("SECOND", GaussSum.model_solution(100))
end = timer()
print((end - start)*100) # Time in seconds, e.g. 5.3809195

#I print *100 just to compare "human readable" numbers, without the exponential notation.
