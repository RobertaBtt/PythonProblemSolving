__author__ = 'RobertaBtt'

class OddOccurrencyInArray:

    #Given   an    array    A consisting    of    N    integers    fulfilling
    # the    above    conditions, returns    the    value    of    the    unpaired    element.

    def __init__(self):
        pass

    @staticmethod
    def solution(A):
        # write your code in Python 3.6

        values_map = dict()

        for a in A:
            if a in values_map:
                values_map[a] += 1
            else:
                values_map[a] = 1

        result = [num for num in values_map.items() if num[1] % 2 == 1][0][0]
        return result

print(OddOccurrencyInArray.solution([9, 3, 9, 3, 9, 7, 9,7,8,1,8]))
print(OddOccurrencyInArray.solution([9, 3, 9, 3, 9, 7, 9]))
