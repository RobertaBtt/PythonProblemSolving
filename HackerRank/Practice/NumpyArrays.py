import numpy

# Saimple input
# 1 4
# 1 2 3 4
# 5 6 7 8

if __name__ == '__main__':

    line_input_1 = input().rstrip().split()
    N = int(line_input_1[0])
    M = int(line_input_1[1])

    if N > 0 and M > 0:
        a, b = (numpy.array([input().split() for _ in range(N)], dtype=int) for _ in range(2))

        print(a + b, a - b, a * b, a // b, a % b, a ** b, sep='\n')
