__author__ = 'RobertaBtt'

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

class BinaryGap:
    def solution(N):
        started = False
        conta = 0
        list = []
        list.append(0)
        binary_array = [int(digit) for digit in bin(N)[2:]]

        for bit in binary_array :
            if bit == 1:
                if not started:
                    started = True
                else:
                    list.append(conta)
                    conta = 0
            else:
                if started:
                    conta += 1

        return max(list)




print(BinaryGap.solution(32))