#!/bin/python3

def resolveMostFrequency(inputString):
    inputString = sorted(inputString)
    words = {}
    for letter in inputString:
        if letter in words:
            words[letter] = words[letter] + 1
        else:
            words[letter] = 1

    words = sorted(words.items(), key=lambda x: x[1], reverse=True)
    return words

def printFirstTree(resultList):
    print(str(resultList[0][0]) + " " + str(resultList[0][1]))
    print(str(resultList[1][0]) + " " + str(resultList[1][1]))
    print(str(resultList[2][0]) + " " +  str(resultList[2][1]))

if __name__ == '__main__':
    s = input()
    if 3 < len(s) <= 10**4:
        resultList = resolveMostFrequency(s)

    printFirstTree(resultList)
