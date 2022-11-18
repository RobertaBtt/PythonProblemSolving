__author__ = 'RobertaBtt'


class BinaryGap:

    def __init__(self):
        pass

    @staticmethod
    def solution(n):
        started = False
        count = 0
        numbers = [0]
        binary_array = [int(digit) for digit in bin(n)[2:]]

        for bit in binary_array:
            if bit == 1:
                if not started:
                    started = True
                else:
                    numbers.append(count)
                    count = 0
            else:
                if started:
                    count += 1

        return max(numbers)


print(BinaryGap.solution(1041))
