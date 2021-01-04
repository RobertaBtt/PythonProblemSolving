#!/bin/python3


def findSecondLowestGradeAndNames(sortedList, N):

    secondLowestNames = []
    secondLowestN = None
    maximum = sortedList[n-1]
    minimum = sortedList[0]

    for i in sortedList:
        if secondLowestN is None:

            if i[1] != minimum[1]:
                secondLowestN = i[1]
                secondLowestNames.append(i[0])
        else:
            if i[1] == secondLowestN:
                secondLowestNames.append(i[0])
    return secondLowestNames

def Sort(sub_li):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    sub_li.sort(key=lambda x: x[1])
    return sub_li

if __name__ == '__main__':

    people = []
    n = int(input())
    if 1<= n <=5:
        for _ in range(n):
            name = input()
            score = float(input())
            element = [name, score]
            people.append(element)

    sortedList = Sort(people)
    print(*sorted(findSecondLowestGradeAndNames(sortedList, n)), sep = "\n")


'''

Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

'''

#Input number 2
'''

Harsh
20
Beria
20
Varun
19
Kakunami
19
Vikas
21

'''