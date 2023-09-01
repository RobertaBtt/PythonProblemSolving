__author__ = 'RobertaBtt'

"""A non-empty array A consisting of N integers is given. The array contains an odd number of elements, 
and each element of the array can be paired with another element that has the same value, 
except for one element that is left unpaired."""


"""Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, 
returns the value of the unpaired element.
"""


class OddOccurrencyInArray:

    def __init__(self):
        pass

    @staticmethod
    def solution(A):
        values_map = dict()

        for a in A:
            if a in values_map:
                values_map[a] += 1
            else:
                values_map[a] = 1
        values_map.items()
        # List comprehension
        # [expression(i) for i in list if condition]
        # num[1] means the value in the tuple of items (key,value)
        result_list = [num for num in values_map.items() if num[1] % 2 == 1]

        # I take the first element (position 0) and the key (position 0)
        result = result_list[0][0]
        return result


print(OddOccurrencyInArray.solution([9, 3, 9, 3, 9, 7, 9, 7, 8, 1, 8]))
print(OddOccurrencyInArray.solution([9, 3, 9, 3, 9, 7, 9]))
