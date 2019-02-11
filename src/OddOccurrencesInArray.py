__author__ = 'roby'

class OddOccurencyInArray:


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

print(OddOccurencyInArray.solution([9, 3, 9, 3, 9, 7, 9]))

