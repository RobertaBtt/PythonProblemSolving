import numpy


#Your task is to print an array of size NXM with its main diagonal elements as 1 and 0 everywhere else.

#Input Format
# A single line containing the space separated values of  N and M

def print_matrix(N,M):
    numpy.set_printoptions(legacy='1.13')
    print(numpy.eye(N,M))
if __name__ == '__main__':
    line_input = input().rstrip().split()

    N = int(line_input[0])
    M = int(line_input[1])

    if N>0 and M>0:
        print_matrix(N,M)
