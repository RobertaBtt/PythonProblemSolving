#!/bin/python3

def most_frequent(List):
    return max(set(List), key = List.count)

def findLeader(inputString):
    inputString = sorted(inputString)
    numbers = {}
    for number in inputString:
        if number in numbers:
            numbers[number] = numbers[number] + 1
        else:
            numbers[number] = 1

    numbers = sorted(numbers.items(), key=lambda x: x[1], reverse=True)
    return numbers

def printFirstTree(resultList):
    print(str(resultList[0][0]) + " " + str(resultList[0][1]))
    print(str(resultList[1][0]) + " " + str(resultList[1][1]))
    print(str(resultList[2][0]) + " " +  str(resultList[2][1]))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    if 3 < len(arr) <= 10**4:
        resultList = findLeader(arr)

    printFirstTree(resultList)
