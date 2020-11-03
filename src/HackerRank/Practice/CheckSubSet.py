#!/bin/python3
if __name__ == '__main__':

    tests = int(input())
    if 0 < tests < 21:
        for _ in range(tests):
            sizeA, A, sizeB, B = input(), set(input().split()), input(), set(input().split())
            print(A.issubset(B))

'''
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
'''
