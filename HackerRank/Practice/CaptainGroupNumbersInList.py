#!/bin/python3

if __name__ == '__main__':


    numberOfGroups = int(input())
    # # Input una lista
    arr = list(map(int, input().split()))
    elementsSet = set(arr)
    sumSet = sum(elementsSet)
    print(((sumSet * numberOfGroups) - (sum(arr)))//(numberOfGroups-1))

    # Shorter way to acquire input
    #k, arr = int(input()), list(map(int, input().split()))

'''
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

'''